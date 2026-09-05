"""
CloudShield Enterprise
AWS EC2 Scanner
"""

from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError, NoRegionError

from app.cloud.aws.client import AWSClient, aws_region


class EC2Scanner:

    def __init__(self, region=None, client_factory=None):
        self.region = aws_region(region)
        self._client_factory = client_factory or AWSClient(self.region)
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = self._client_factory.client("ec2")
        return self._client

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
                            "availability_zone": instance.get("Placement", {}).get("AvailabilityZone"),
                            "vpc_id": instance.get("VpcId"),
                            "subnet_id": instance.get("SubnetId"),
                            "security_group_ids": [group.get("GroupId") for group in instance.get("SecurityGroup", [])],
                            "ami_id": instance.get("ImageId"),
                            "public_ip": instance.get("PublicIpAddress"),
                            "private_ip": instance.get("PrivateIpAddress"),
                            "launch_time": str(instance.get("LaunchTime")),
                            "platform": instance.get("Platform", "linux"),
                            "architecture": instance.get("Architecture"),
                            "monitoring": instance.get("Monitoring", {}).get("State"),
                        }
                    )

            return {
                "success": True,
                "service": "EC2",
                "total_instances": len(instances),
                "instances": instances,
                "region": self.region,
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

        except (ClientError, BotoCoreError) as e:

            return {"success": False, "service": "EC2", "region": self.region, "error": str(e), "findings": []}

        except Exception as e:

            return {"success": False, "service": "EC2", "error": str(e)}
