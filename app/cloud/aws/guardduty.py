"""
CloudShield Enterprise
AWS GuardDuty Scanner
"""

import boto3
from botocore.exceptions import NoCredentialsError, ClientError, NoRegionError


class GuardDutyScanner:

    def __init__(self):

        self.client = boto3.client("guardduty", region_name="ap-south-1")

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
