"""
CloudShield Enterprise
AWS Security Service
"""

from app.cloud.aws.ec2 import EC2Scanner
from app.cloud.aws.s3 import S3Scanner
from app.cloud.aws.iam import IAMScanner
from app.cloud.aws.security_groups import SecurityGroupScanner
from app.cloud.aws.cloudtrail import CloudTrailScanner
from app.cloud.aws.guardduty import GuardDutyScanner
from app.cloud.aws.inspector import InspectorScanner
from app.cloud.aws.config import ConfigScanner


class AWSScanner:
    """
    Central AWS Security Scanner
    """

    def __init__(self):

        self.scanners = {
            "ec2": EC2Scanner,
            "s3": S3Scanner,
            "iam": IAMScanner,
            "security_groups": SecurityGroupScanner,
            "cloudtrail": CloudTrailScanner,
            "guardduty": GuardDutyScanner,
            "inspector": InspectorScanner,
            "config": ConfigScanner,
        }
        self._instances = {}

    # --------------------------------------------------
    # Run Every Scanner
    # --------------------------------------------------

    def scan(self):

        results = {}

        for name in self.scanners:

            try:

                results[name] = self.scan_service(name)

            except Exception as e:

                results[name] = {"success": False, "service": name, "error": str(e)}

        return results

    # --------------------------------------------------
    # Generic Scanner
    # --------------------------------------------------

    def scan_service(self, service):

        scanner_class = self.scanners.get(service)

        if scanner_class is None:

            return {
                "success": False,
                "service": service,
                "error": "Unknown AWS service.",
            }

        try:

            scanner = self._instances.setdefault(service, scanner_class())
            return scanner.scan()

        except Exception as e:

            return {"success": False, "service": service, "error": str(e)}

    # --------------------------------------------------
    # Individual Services
    # --------------------------------------------------

    def scan_ec2(self):

        return self.scan_service("ec2")

    def scan_s3(self):

        return self.scan_service("s3")

    def scan_iam(self):

        return self.scan_service("iam")

    def scan_security_groups(self):

        return self.scan_service("security_groups")

    def scan_cloudtrail(self):

        return self.scan_service("cloudtrail")

    def scan_guardduty(self):

        return self.scan_service("guardduty")

    def scan_inspector(self):

        return self.scan_service("inspector")

    def scan_config(self):

        return self.scan_service("config")
