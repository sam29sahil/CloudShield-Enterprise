"""
CloudShield Enterprise
AWS CloudTrail Scanner
"""

from botocore.exceptions import NoCredentialsError, ClientError, NoRegionError
from app.cloud.aws.client import AWSClient, aws_region


class CloudTrailScanner:

    def __init__(self, region=None, client_factory=None):
        self.region = aws_region(region)
        self._client_factory = client_factory or AWSClient(self.region)
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = self._client_factory.client("cloudtrail")
        return self._client

    def scan(self):

        try:

            trails = self.client.describe_trails()

            return {
                "success": True,
                "service": "CloudTrail",
                "total_trails": len(trails.get("trailList", [])),
                "trails": trails.get("trailList", []),
            }

        except NoCredentialsError:

            return {
                "success": False,
                "service": "CloudTrail",
                "error": "AWS credentials not configured.",
            }

        except NoRegionError:

            return {
                "success": False,
                "service": "CloudTrail",
                "error": "AWS region not configured.",
            }

        except ClientError as e:

            return {"success": False, "service": "CloudTrail", "error": str(e)}

        except Exception as e:

            return {"success": False, "service": "CloudTrail", "error": str(e)}
