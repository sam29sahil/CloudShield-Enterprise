"""
CloudShield Enterprise
AWS IAM Scanner
"""

from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

from app.cloud.aws.client import AWSClient, aws_region


class IAMScanner:

    def __init__(self, region=None, client_factory=None):
        self.region = aws_region(region)
        self._client_factory = client_factory or AWSClient(self.region)
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = self._client_factory.client("iam")
        return self._client

    def scan(self):

        try:

            users = self.client.list_users()["Users"]

            data = []
            findings = []

            for user in users:

                user_name = user["UserName"]
                item = {"user_name": user_name, "arn": user["Arn"], "created": str(user["CreateDate"]), "mfa_enabled": None, "access_keys": []}
                try:
                    item["mfa_enabled"] = bool(self.client.list_mfa_devices(UserName=user_name).get("MFADevices"))
                    if not item["mfa_enabled"]:
                        findings.append({"title": "IAM user without MFA", "description": "The IAM user has no configured MFA device.", "severity": "High", "category": "Identity Security", "service": "IAM", "resource": user_name, "region": self.region, "evidence": item, "recommendation": "Require MFA for interactive IAM users."})
                except ClientError:
                    pass
                try:
                    item["access_keys"] = [{"id": key.get("AccessKeyId"), "status": key.get("Status"), "created": str(key.get("CreateDate"))} for key in self.client.list_access_keys(UserName=user_name).get("AccessKeyMetadata", [])]
                except ClientError:
                    pass
                data.append(item)

            return {"success": True, "total_users": len(data), "users": data, "findings": findings, "region": self.region}

        except NoCredentialsError:

            return {"success": False, "error": "AWS credentials not configured."}

        except (ClientError, BotoCoreError) as e:

            return {"success": False, "service": "IAM", "region": self.region, "error": "IAM permission is unavailable.", "findings": []}

        except Exception as e:

            return {"success": False, "error": str(e)}
