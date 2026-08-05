"""
CloudShield Enterprise
AWS Config Scanner
"""

import boto3
from botocore.exceptions import NoCredentialsError, ClientError, NoRegionError


class ConfigScanner:

    def __init__(self):

        self.client = boto3.client("config", region_name="ap-south-1")

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
