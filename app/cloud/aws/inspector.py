"""
CloudShield Enterprise
AWS Inspector Scanner
"""

from botocore.exceptions import NoCredentialsError, ClientError, NoRegionError
from app.cloud.aws.client import AWSClient, aws_region


class InspectorScanner:

    def __init__(self, region=None, client_factory=None):
        self.region = aws_region(region)
        self._client_factory = client_factory or AWSClient(self.region)
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = self._client_factory.client("inspector2")
        return self._client

    def scan(self):

        try:

            findings = self.client.list_findings()

            return {
                "success": True,
                "service": "Inspector",
                "total_findings": len(findings.get("findings", [])),
                "findings": findings.get("findings", []),
            }

        except NoCredentialsError:

            return {
                "success": False,
                "service": "Inspector",
                "error": "AWS credentials are not configured.",
            }

        except NoRegionError:

            return {
                "success": False,
                "service": "Inspector",
                "error": "AWS region is not configured.",
            }

        except ClientError as e:

            return {"success": False, "service": "Inspector", "error": str(e)}

        except Exception as e:

            return {"success": False, "service": "Inspector", "error": str(e)}
