"""
CloudShield Enterprise
AWS Inspector Scanner
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


class InspectorScanner:

    def __init__(self):

<<<<<<< HEAD
        self.client = boto3.client("inspector2", region_name="ap-south-1")
=======
        self.client = boto3.client(
            "inspector2",
            region_name="ap-south-1"
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def scan(self):

        try:

            findings = self.client.list_findings()

            return {
<<<<<<< HEAD
                "success": True,
                "service": "Inspector",
                "total_findings": len(findings.get("findings", [])),
                "findings": findings.get("findings", []),
=======

                "success": True,

                "service": "Inspector",

                "total_findings": len(
                    findings.get(
                        "findings",
                        []
                    )
                ),

                "findings": findings.get(
                    "findings",
                    []
                )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except NoCredentialsError:

            return {
<<<<<<< HEAD
                "success": False,
                "service": "Inspector",
                "error": "AWS credentials are not configured.",
=======

                "success": False,

                "service": "Inspector",

                "error": "AWS credentials are not configured."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except NoRegionError:

            return {
<<<<<<< HEAD
                "success": False,
                "service": "Inspector",
                "error": "AWS region is not configured.",
=======

                "success": False,

                "service": "Inspector",

                "error": "AWS region is not configured."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except ClientError as e:

<<<<<<< HEAD
            return {"success": False, "service": "Inspector", "error": str(e)}

        except Exception as e:

            return {"success": False, "service": "Inspector", "error": str(e)}
=======
            return {

                "success": False,

                "service": "Inspector",

                "error": str(e)

            }

        except Exception as e:

            return {

                "success": False,

                "service": "Inspector",

                "error": str(e)

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
