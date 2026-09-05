"""Canonical, lazy AWS connectivity check."""

from botocore.exceptions import (
    BotoCoreError,
    ClientError,
    EndpointConnectionError,
    NoCredentialsError,
    NoRegionError,
    PartialCredentialsError,
)

from app.cloud.aws.client import AWSClient, aws_region


class AWSConnection:
    def __init__(self, region=None, client_factory=None):
        self.region = aws_region(region)
        self._client_factory = client_factory or AWSClient(self.region)

    def check(self):
        try:
            identity = self._client_factory.client("sts").get_caller_identity()
            return {
                "connected": True,
                "status": "CONNECTED",
                "account_id": identity.get("Account"),
                "arn": identity.get("Arn"),
                "region": self.region,
                "message": "AWS connection verified.",
            }
        except (NoCredentialsError, NoRegionError):
            return self._result("NOT_CONFIGURED", "AWS credentials are not configured.")
        except PartialCredentialsError:
            return self._result("INVALID_CREDENTIALS", "AWS credentials are invalid or incomplete.")
        except ClientError as error:
            code = error.response.get("Error", {}).get("Code", "")
            if code in {"InvalidClientTokenId", "SignatureDoesNotMatch", "ExpiredToken", "UnrecognizedClientException"}:
                return self._result("INVALID_CREDENTIALS", "AWS credentials are invalid or expired.")
            if code in {"AccessDenied", "AccessDeniedException"}:
                return self._result("PERMISSION_LIMITED", "AWS credentials cannot call STS GetCallerIdentity.")
            return self._result("UNAVAILABLE", "AWS is temporarily unavailable.")
        except EndpointConnectionError:
            return self._result("UNAVAILABLE", "AWS is temporarily unavailable.")
        except BotoCoreError:
            return self._result("UNAVAILABLE", "AWS is temporarily unavailable.")

    def _result(self, status, message):
        return {
            "connected": False,
            "status": status,
            "account_id": None,
            "arn": None,
            "region": self.region,
            "message": message,
        }