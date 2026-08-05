"""
CloudShield Enterprise
AWS IAM Scanner
"""

import boto3
from botocore.exceptions import NoCredentialsError, ClientError


class IAMScanner:

    def __init__(self):

<<<<<<< HEAD
        self.client = boto3.client("iam", region_name="ap-south-1")
=======
        self.client = boto3.client(
            "iam",
            region_name="ap-south-1"
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def scan(self):

        try:

            users = self.client.list_users()["Users"]

            data = []

            for user in users:

<<<<<<< HEAD
                data.append(
                    {
                        "user_name": user["UserName"],
                        "arn": user["Arn"],
                        "created": str(user["CreateDate"]),
                    }
                )

            return {"success": True, "total_users": len(data), "users": data}

        except NoCredentialsError:

            return {"success": False, "error": "AWS credentials not configured."}

        except ClientError as e:

            return {"success": False, "error": str(e)}

        except Exception as e:

            return {"success": False, "error": str(e)}
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
