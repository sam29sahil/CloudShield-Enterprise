"""
CloudShield Enterprise
AWS S3 Scanner
"""

from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

from app.cloud.aws.client import AWSClient, aws_region


class S3Scanner:

    def __init__(self, region=None, client_factory=None):
        self.region = aws_region(region)
        self._client_factory = client_factory or AWSClient(self.region)
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = self._client_factory.client("s3")
        return self._client

    def scan(self):

        try:

            buckets = self.client.list_buckets()["Buckets"]

            data = []
            findings = []

            for bucket in buckets:

                versioning = "Unknown"
                public_access_block = None
                try:
                    versioning = self.client.get_bucket_versioning(Bucket=bucket["Name"]).get("Status", "Disabled")
                except ClientError:
                    pass
                try:
                    public_access_block = self.client.get_public_access_block(Bucket=bucket["Name"]).get("PublicAccessBlockConfiguration")
                except ClientError:
                    pass
                data.append(
                    {
                        "name": bucket["Name"],
                        "region": self.region,
                        "versioning": versioning,
                        "encryption": "Unknown",
                        "public_access_block": public_access_block,
                        "created": str(bucket["CreationDate"]),
                    }
                )
                if versioning == "Disabled":
                    findings.append({"title": "S3 bucket versioning disabled", "description": "Object versioning is disabled for the bucket.", "severity": "Low", "category": "Storage Security", "service": "S3", "resource": bucket["Name"], "region": self.region, "evidence": data[-1], "recommendation": "Enable versioning where recovery from accidental deletion is required."})

            return {"success": True, "total_buckets": len(data), "buckets": data, "findings": findings, "region": self.region}

        except NoCredentialsError:

            return {"success": False, "error": "AWS credentials not configured."}

        except (ClientError, BotoCoreError) as e:

            return {"success": False, "service": "S3", "region": self.region, "error": "S3 permission is unavailable.", "findings": []}

        except Exception as e:

            return {"success": False, "error": str(e)}
