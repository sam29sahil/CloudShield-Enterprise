"""
CloudShield Enterprise
AWS Security Groups Scanner
"""

from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError, NoRegionError

from app.cloud.aws.client import AWSClient, aws_region


class SecurityGroupScanner:

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

        try:

            response = self.client.describe_security_groups()

            groups = response.get("SecurityGroups", [])
            findings = []
            sensitive_ports = {22, 3389, 3306, 5432, 1433, 6379, 27017}
            for group in groups:
                for permission in group.get("IpPermissions", []):
                    from_port = permission.get("FromPort")
                    to_port = permission.get("ToPort", from_port)
                    ports = set(range(from_port, to_port + 1)) if from_port is not None and to_port is not None else set()
                    public = any(item.get("CidrIp") == "0.0.0.0/0" for item in permission.get("IpRanges", []))
                    public = public or any(item.get("CidrIpv6") == "::/0" for item in permission.get("Ipv6Ranges", []))
                    if public and (not ports or ports & sensitive_ports):
                        findings.append({
                            "title": "Unrestricted security group ingress",
                            "description": "Inbound traffic is allowed from the public internet.",
                            "severity": "High" if ports & sensitive_ports else "Medium",
                            "category": "Network Security",
                            "service": "Security Groups",
                            "resource": group.get("GroupId"),
                            "region": self.region,
                            "evidence": permission,
                            "recommendation": "Restrict inbound CIDR ranges and ports to required sources.",
                        })

            return {
                "success": True,
                "service": "Security Groups",
                "total_groups": len(groups),
                "groups": groups,
                "findings": findings,
                "region": self.region,
            }

        except NoCredentialsError:

            return {
                "success": False,
                "service": "Security Groups",
                "error": "AWS credentials not configured.",
            }

        except NoRegionError:

            return {
                "success": False,
                "service": "Security Groups",
                "error": "AWS region not configured.",
            }

        except (ClientError, BotoCoreError) as e:

            return {"success": False, "service": "Security Groups", "region": self.region, "error": str(e), "findings": []}

        except Exception as e:

            return {"success": False, "service": "Security Groups", "error": str(e)}
