"""
CloudShield Enterprise
AWS Security Groups Scanner
"""

import boto3
from botocore.exceptions import (
    NoCredentialsError,
    ClientError,
    NoRegionError
)


class SecurityGroupScanner:

    def __init__(self):

        self.client = boto3.client(
            "ec2",
            region_name="ap-south-1"
        )

    def scan(self):

        try:

            response = self.client.describe_security_groups()

            groups = response.get(
                "SecurityGroups",
                []
            )

            return {

                "success": True,

                "service": "Security Groups",

                "total_groups": len(groups),

                "groups": groups

            }

        except NoCredentialsError:

            return {

                "success": False,

                "service": "Security Groups",

                "error": "AWS credentials not configured."

            }

        except NoRegionError:

            return {

                "success": False,

                "service": "Security Groups",

                "error": "AWS region not configured."

            }

        except ClientError as e:

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