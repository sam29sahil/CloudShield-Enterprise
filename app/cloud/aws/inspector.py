"""
CloudShield Enterprise
AWS Inspector Scanner
"""

import boto3
from botocore.exceptions import NoCredentialsError, ClientError, NoRegionError


class InspectorScanner:

    def __init__(self):

        self.client = boto3.client("inspector2", region_name="ap-south-1")

    def scan(self):

        try:

            findings = self.client.list_findings()

            return {
                "success": True,
                "service": "Inspector",
                "total_findings": len(findings.get("findings", [])),
                "findings": findings.get("findings", []),
            }

        except NoCredentialsError:

            return {
                "success": False,
                "service": "Inspector",
                "error": "AWS credentials are not configured.",
            }

        except NoRegionError:

            return {
                "success": False,
                "service": "Inspector",
                "error": "AWS region is not configured.",
            }

        except ClientError as e:

            return {"success": False, "service": "Inspector", "error": str(e)}

        except Exception as e:

            return {"success": False, "service": "Inspector", "error": str(e)}
