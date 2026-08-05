"""
CloudShield Enterprise
AWS GuardDuty Scanner
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


class GuardDutyScanner:

    def __init__(self):

<<<<<<< HEAD
        self.client = boto3.client("guardduty", region_name="ap-south-1")
=======
        self.client = boto3.client(
            "guardduty",
            region_name="ap-south-1"
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def scan(self):

        try:

            detectors = self.client.list_detectors()

<<<<<<< HEAD
            detector_ids = detectors.get("DetectorIds", [])

            return {
                "success": True,
                "service": "GuardDuty",
                "enabled": len(detector_ids) > 0,
                "detectors": detector_ids,
=======
            detector_ids = detectors.get(
                "DetectorIds",
                []
            )

            return {

                "success": True,

                "service": "GuardDuty",

                "enabled": len(detector_ids) > 0,

                "detectors": detector_ids

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except NoCredentialsError:

            return {
<<<<<<< HEAD
                "success": False,
                "service": "GuardDuty",
                "error": "AWS credentials are not configured.",
=======

                "success": False,

                "service": "GuardDuty",

                "error": "AWS credentials are not configured."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except NoRegionError:

            return {
<<<<<<< HEAD
                "success": False,
                "service": "GuardDuty",
                "error": "AWS region is not configured.",
=======

                "success": False,

                "service": "GuardDuty",

                "error": "AWS region is not configured."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except ClientError as e:

<<<<<<< HEAD
            return {"success": False, "service": "GuardDuty", "error": str(e)}

        except Exception as e:

            return {"success": False, "service": "GuardDuty", "error": str(e)}
=======
            return {

                "success": False,

                "service": "GuardDuty",

                "error": str(e)

            }

        except Exception as e:

            return {

                "success": False,

                "service": "GuardDuty",

                "error": str(e)

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
