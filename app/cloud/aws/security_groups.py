"""
CloudShield Enterprise
AWS Security Groups Scanner
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


class SecurityGroupScanner:

    def __init__(self):

<<<<<<< HEAD
        self.client = boto3.client("ec2", region_name="ap-south-1")
=======
        self.client = boto3.client(
            "ec2",
            region_name="ap-south-1"
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def scan(self):

        try:

            response = self.client.describe_security_groups()

<<<<<<< HEAD
            groups = response.get("SecurityGroups", [])

            return {
                "success": True,
                "service": "Security Groups",
                "total_groups": len(groups),
                "groups": groups,
=======
            groups = response.get(
                "SecurityGroups",
                []
            )

            return {

                "success": True,

                "service": "Security Groups",

                "total_groups": len(groups),

                "groups": groups

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except NoCredentialsError:

            return {
<<<<<<< HEAD
                "success": False,
                "service": "Security Groups",
                "error": "AWS credentials not configured.",
=======

                "success": False,

                "service": "Security Groups",

                "error": "AWS credentials not configured."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except NoRegionError:

            return {
<<<<<<< HEAD
                "success": False,
                "service": "Security Groups",
                "error": "AWS region not configured.",
=======

                "success": False,

                "service": "Security Groups",

                "error": "AWS region not configured."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except ClientError as e:

<<<<<<< HEAD
            return {"success": False, "service": "Security Groups", "error": str(e)}

        except Exception as e:

            return {"success": False, "service": "Security Groups", "error": str(e)}
=======
            return {

                "success": False,

                "service": "Security Groups",

                "error": str(e)

            }

        except Exception as e:

            return {

                "success": False,

                "service": "Security Groups",

                "error": str(e)

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
