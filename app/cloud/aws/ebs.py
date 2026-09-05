"""Read-only EBS inventory and findings."""

from botocore.exceptions import BotoCoreError, ClientError

from app.cloud.aws.client import AWSClient, aws_region


class EBSScanner:
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
            volumes = self.client.describe_volumes().get("Volumes", [])
            data = []
            findings = []
            for volume in volumes:
                attachments = volume.get("Attachments", [])
                item = {
                    "volume_id": volume.get("VolumeId"),
                    "size": volume.get("Size"),
                    "volume_type": volume.get("VolumeType"),
                    "state": volume.get("State"),
                    "encrypted": volume.get("Encrypted", False),
                    "availability_zone": volume.get("AvailabilityZone"),
                    "attachments": attachments,
                }
                data.append(item)
                if not item["encrypted"]:
                    findings.append({"title": "Unencrypted EBS volume", "description": "The EBS volume is not encrypted.", "severity": "High", "category": "Storage Security", "service": "EBS", "resource": item["volume_id"], "region": self.region, "evidence": item, "recommendation": "Encrypt the volume through an approved change process."})
            return {"success": True, "service": "EBS", "region": self.region, "total_volumes": len(data), "volumes": data, "findings": findings}
        except (ClientError, BotoCoreError):
            return {"success": False, "service": "EBS", "region": self.region, "error": "EBS permission is unavailable.", "findings": []}