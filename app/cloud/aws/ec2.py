"""
CloudShield Enterprise
AWS EC2 Scanner
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


class EC2Scanner:

    def __init__(self):

<<<<<<< HEAD
        self.client = boto3.client("ec2", region_name="ap-south-1")
=======
        self.client = boto3.client(
            "ec2",
            region_name="ap-south-1"
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def scan(self):
        """
        Scan EC2 instances.
        """

        try:

            response = self.client.describe_instances()

<<<<<<< HEAD
            reservations = response.get("Reservations", [])
=======
            reservations = response.get(
                "Reservations",
                []
            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            instances = []

            for reservation in reservations:

<<<<<<< HEAD
                for instance in reservation.get("Instances", []):

                    instances.append(
                        {
                            "instance_id": instance.get("InstanceId"),
                            "state": instance.get("State", {}).get("Name"),
                            "instance_type": instance.get("InstanceType"),
                            "public_ip": instance.get("PublicIpAddress"),
                            "private_ip": instance.get("PrivateIpAddress"),
                            "launch_time": str(instance.get("LaunchTime")),
                        }
                    )

            return {
                "success": True,
                "service": "EC2",
                "total_instances": len(instances),
                "instances": instances,
=======
                for instance in reservation.get(
                    "Instances",
                    []
                ):

                    instances.append({

                        "instance_id": instance.get(
                            "InstanceId"
                        ),

                        "state": instance.get(
                            "State",
                            {}
                        ).get(
                            "Name"
                        ),

                        "instance_type": instance.get(
                            "InstanceType"
                        ),

                        "public_ip": instance.get(
                            "PublicIpAddress"
                        ),

                        "private_ip": instance.get(
                            "PrivateIpAddress"
                        ),

                        "launch_time": str(
                            instance.get(
                                "LaunchTime"
                            )
                        )

                    })

            return {

                "success": True,

                "service": "EC2",

                "total_instances": len(instances),

                "instances": instances

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except NoCredentialsError:

            return {
<<<<<<< HEAD
                "success": False,
                "service": "EC2",
                "error": "AWS credentials are not configured.",
=======

                "success": False,

                "service": "EC2",

                "error": "AWS credentials are not configured."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except NoRegionError:

            return {
<<<<<<< HEAD
                "success": False,
                "service": "EC2",
                "error": "AWS region is not configured.",
=======

                "success": False,

                "service": "EC2",

                "error": "AWS region is not configured."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except ClientError as e:

<<<<<<< HEAD
            return {"success": False, "service": "EC2", "error": str(e)}

        except Exception as e:

            return {"success": False, "service": "EC2", "error": str(e)}
=======
            return {

                "success": False,

                "service": "EC2",

                "error": str(e)

            }

        except Exception as e:

            return {

                "success": False,

                "service": "EC2",

                "error": str(e)

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
