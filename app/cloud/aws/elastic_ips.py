"""Read-only Elastic IP inventory and findings."""

from botocore.exceptions import BotoCoreError, ClientError

from app.cloud.aws.client import AWSClient, aws_region


class ElasticIPScanner:
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
            addresses = self.client.describe_addresses().get("Addresses", [])
            data = [{
                "allocation_id": item.get("AllocationId"),
                "public_ip": item.get("PublicIp"),
                "instance_id": item.get("InstanceId"),
                "network_interface_id": item.get("NetworkInterfaceId"),
                "associated": bool(item.get("InstanceId") or item.get("NetworkInterfaceId")),
            } for item in addresses]
            findings = [{"title": "Unused Elastic IP address", "description": "An Elastic IP is allocated but not associated with a resource.", "severity": "Low", "category": "Network Security", "service": "Elastic IP", "resource": item["public_ip"], "region": self.region, "evidence": item, "recommendation": "Release unused addresses through an approved change process."} for item in data if not item["associated"]]
            return {"success": True, "service": "Elastic IPs", "region": self.region, "total_addresses": len(data), "addresses": data, "findings": findings}
        except (ClientError, BotoCoreError):
            return {"success": False, "service": "Elastic IPs", "region": self.region, "error": "Elastic IP permission is unavailable.", "findings": []}