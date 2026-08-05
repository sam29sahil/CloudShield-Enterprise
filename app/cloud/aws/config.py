"""
CloudShield Enterprise
AWS Config Scanner
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


class ConfigScanner:

    def __init__(self):

<<<<<<< HEAD
        self.client = boto3.client("config", region_name="ap-south-1")
=======
        self.client = boto3.client(
            "config",
            region_name="ap-south-1"
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def scan(self):

        try:

            response = self.client.describe_configuration_recorders()

<<<<<<< HEAD
            recorders = response.get("ConfigurationRecorders", [])

            return {
                "success": True,
                "service": "AWS Config",
                "configured": len(recorders) > 0,
                "recorders": recorders,
=======
            recorders = response.get(
                "ConfigurationRecorders",
                []
            )

            return {

                "success": True,

                "service": "AWS Config",

                "configured": len(recorders) > 0,

                "recorders": recorders

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except NoCredentialsError:

            return {
<<<<<<< HEAD
                "success": False,
                "service": "AWS Config",
                "error": "AWS credentials not configured.",
=======

                "success": False,

                "service": "AWS Config",

                "error": "AWS credentials not configured."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except NoRegionError:

            return {
<<<<<<< HEAD
                "success": False,
                "service": "AWS Config",
                "error": "AWS region not configured.",
=======

                "success": False,

                "service": "AWS Config",

                "error": "AWS region not configured."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except ClientError as e:

<<<<<<< HEAD
            return {"success": False, "service": "AWS Config", "error": str(e)}

        except Exception as e:

            return {"success": False, "service": "AWS Config", "error": str(e)}
=======
            return {

                "success": False,

                "service": "AWS Config",

                "error": str(e)

            }

        except Exception as e:

            return {

                "success": False,

                "service": "AWS Config",

                "error": str(e)

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
