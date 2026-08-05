"""
CloudShield Enterprise
AWS CloudTrail Scanner
"""

import boto3
<<<<<<< HEAD
from botocore.exceptions import NoCredentialsError, ClientError, NoRegionError
=======
from botocore.exceptions import (
    NoCredentialsError,
    ClientError,
    NoRegionError
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


class CloudTrailScanner:

    def __init__(self):

<<<<<<< HEAD
        self.client = boto3.client("cloudtrail", region_name="ap-south-1")
=======
        self.client = boto3.client(
            "cloudtrail",
            region_name="ap-south-1"
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def scan(self):

        try:

            trails = self.client.describe_trails()

            return {
<<<<<<< HEAD
                "success": True,
                "service": "CloudTrail",
                "total_trails": len(trails.get("trailList", [])),
                "trails": trails.get("trailList", []),
=======

                "success": True,

                "service": "CloudTrail",

                "total_trails": len(
                    trails.get("trailList", [])
                ),

                "trails": trails.get(
                    "trailList",
                    []
                )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except NoCredentialsError:

            return {
<<<<<<< HEAD
                "success": False,
                "service": "CloudTrail",
                "error": "AWS credentials not configured.",
=======

                "success": False,

                "service": "CloudTrail",

                "error": "AWS credentials not configured."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except NoRegionError:

            return {
<<<<<<< HEAD
                "success": False,
                "service": "CloudTrail",
                "error": "AWS region not configured.",
=======

                "success": False,

                "service": "CloudTrail",

                "error": "AWS region not configured."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except ClientError as e:

<<<<<<< HEAD
            return {"success": False, "service": "CloudTrail", "error": str(e)}

        except Exception as e:

            return {"success": False, "service": "CloudTrail", "error": str(e)}
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
