"""
CloudShield Enterprise
AWS Config Scanner
"""

from botocore.exceptions import NoCredentialsError, ClientError, NoRegionError
from app.cloud.aws.client import AWSClient, aws_region


class ConfigScanner:

    def __init__(self, region=None, client_factory=None):
        self.region = aws_region(region)
        self._client_factory = client_factory or AWSClient(self.region)
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = self._client_factory.client("config")
        return self._client

    def scan(self):

        try:

            response = self.client.describe_configuration_recorders()

            recorders = response.get("ConfigurationRecorders", [])

            return {
                "success": True,
                "service": "AWS Config",
                "configured": len(recorders) > 0,
                "recorders": recorders,
            }

        except NoCredentialsError:

            return {
                "success": False,
                "service": "AWS Config",
                "error": "AWS credentials not configured.",
            }

        except NoRegionError:

            return {
                "success": False,
                "service": "AWS Config",
                "error": "AWS region not configured.",
            }

        except ClientError as e:

            return {"success": False, "service": "AWS Config", "error": str(e)}

        except Exception as e:

            return {"success": False, "service": "AWS Config", "error": str(e)}
