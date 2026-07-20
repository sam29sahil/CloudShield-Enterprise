"""
CloudShield Enterprise
AWS IAM Scanner
"""

import boto3
from botocore.exceptions import NoCredentialsError, ClientError


class IAMScanner:

    def __init__(self):

        self.client = boto3.client(
            "iam",
            region_name="ap-south-1"
        )

    def scan(self):

        try:

            users = self.client.list_users()["Users"]

            data = []

            for user in users:

                data.append({

                    "user_name": user["UserName"],

                    "arn": user["Arn"],

                    "created": str(user["CreateDate"])

                })

            return {

                "success": True,

                "total_users": len(data),

                "users": data

            }

        except NoCredentialsError:

            return {

                "success": False,

                "error": "AWS credentials not configured."

            }

        except ClientError as e:

            return {

                "success": False,

                "error": str(e)

            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }