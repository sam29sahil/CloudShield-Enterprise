"""
CloudShield Enterprise
AWS S3 Scanner
"""

import boto3
from botocore.exceptions import NoCredentialsError, ClientError


class S3Scanner:

    def __init__(self):

<<<<<<< HEAD
        self.client = boto3.client("s3", region_name="ap-south-1")
=======
        self.client = boto3.client(
            "s3",
            region_name="ap-south-1"
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def scan(self):

        try:

            buckets = self.client.list_buckets()["Buckets"]

            data = []

            for bucket in buckets:

<<<<<<< HEAD
                data.append(
                    {
                        "name": bucket["Name"],
                        "region": "...",
                        "versioning": "Enabled",
                        "encryption": "Enabled",
                        "public": False,
                        "created": str(bucket["CreationDate"]),
                    }
                )

            return {"success": True, "total_buckets": len(data), "buckets": data}

        except NoCredentialsError:

            return {"success": False, "error": "AWS credentials not configured."}

        except ClientError as e:

            return {"success": False, "error": str(e)}

        except Exception as e:

            return {"success": False, "error": str(e)}
=======
                data.append({

                    "name": bucket["Name"],
                    "region": "...",
                    "versioning": "Enabled",
                    "encryption": "Enabled",
                    "public": False,
                    "created": str(bucket["CreationDate"])

                })

            return {

                "success": True,

                "total_buckets": len(data),

                "buckets": data

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
