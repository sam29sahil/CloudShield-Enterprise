"""
CloudShield Enterprise
AWS CloudTrail Scanner
"""

import boto3
from botocore.exceptions import (
    NoCredentialsError,
    ClientError,
    NoRegionError
)


class CloudTrailScanner:

    def __init__(self):

        self.client = boto3.client(
            "cloudtrail",
            region_name="ap-south-1"
        )

    def scan(self):

        try:

            trails = self.client.describe_trails()

            return {

                "success": True,

                "service": "CloudTrail",

                "total_trails": len(
                    trails.get("trailList", [])
                ),

                "trails": trails.get(
                    "trailList",
                    []
                )

            }

        except NoCredentialsError:

            return {

                "success": False,

                "service": "CloudTrail",

                "error": "AWS credentials not configured."

            }

        except NoRegionError:

            return {

                "success": False,

                "service": "CloudTrail",

                "error": "AWS region not configured."

            }

        except ClientError as e:

            return {

                "success": False,

                "service": "CloudTrail",

                "error": str(e)

            }

        except Exception as e:

            return {

                "success": False,

                "service": "CloudTrail",

                "error": str(e)

            }