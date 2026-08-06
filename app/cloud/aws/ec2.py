"""
CloudShield Enterprise
AWS EC2 Scanner
"""

import boto3
from botocore.exceptions import NoCredentialsError, ClientError, NoRegionError


class EC2Scanner:

    def __init__(self):

        self.client = boto3.client("ec2", region_name="ap-south-1")

    def scan(self):
        """
        Scan EC2 instances.
        """

        try:

            response = self.client.describe_instances()

            reservations = response.get("Reservations", [])

            instances = []

            for reservation in reservations:

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
            }

        except NoCredentialsError:

            return {
                "success": False,
                "service": "EC2",
                "error": "AWS credentials are not configured.",
            }

        except NoRegionError:

            return {
                "success": False,
                "service": "EC2",
                "error": "AWS region is not configured.",
            }

        except ClientError as e:

            return {"success": False, "service": "EC2", "error": str(e)}

        except Exception as e:

            return {"success": False, "service": "EC2", "error": str(e)}
