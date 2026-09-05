"""
CloudShield Enterprise
AWS GuardDuty Scanner
"""

from botocore.exceptions import NoCredentialsError, ClientError, NoRegionError
from app.cloud.aws.client import AWSClient, aws_region


class GuardDutyScanner:

    def __init__(self, region=None, client_factory=None):
        self.region = aws_region(region)
        self._client_factory = client_factory or AWSClient(self.region)
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = self._client_factory.client("guardduty")
        return self._client

    def scan(self):

        try:

            detectors = self.client.list_detectors()

            detector_ids = detectors.get("DetectorIds", [])

            return {
                "success": True,
                "service": "GuardDuty",
                "enabled": len(detector_ids) > 0,
                "detectors": detector_ids,
            }

        except NoCredentialsError:

            return {
                "success": False,
                "service": "GuardDuty",
                "error": "AWS credentials are not configured.",
            }

        except NoRegionError:

            return {
                "success": False,
                "service": "GuardDuty",
                "error": "AWS region is not configured.",
            }

        except ClientError as e:

            return {"success": False, "service": "GuardDuty", "error": str(e)}

        except Exception as e:

            return {"success": False, "service": "GuardDuty", "error": str(e)}
