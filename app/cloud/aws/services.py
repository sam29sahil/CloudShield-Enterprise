"""
CloudShield Enterprise
AWS Security Service
"""

from app.cloud.aws.iam import IAMScanner
from app.cloud.aws.s3 import S3Scanner
from app.cloud.aws.ec2 import EC2Scanner
from app.cloud.aws.inspector import InspectorScanner
from app.cloud.aws.guardduty import GuardDutyScanner
from app.cloud.aws.security_groups import SecurityGroupScanner
from app.cloud.aws.cloudtrail import CloudTrailScanner
from app.cloud.aws.config import ConfigScanner


class AWSScanner:

    def __init__(self):

        self.iam = IAMScanner()

        self.s3 = S3Scanner()

        self.ec2 = EC2Scanner()

        self.inspector = InspectorScanner()

        self.guardduty = GuardDutyScanner()

        self.security_groups = SecurityGroupScanner()

        self.cloudtrail = CloudTrailScanner()

        self.config = ConfigScanner()

    def scan(self):
        """
        Run all AWS security scans.
        """

        return {

            "iam": self.iam.scan(),

            "s3": self.s3.scan(),

            "ec2": self.ec2.scan(),

            "inspector": self.inspector.scan(),

            "guardduty": self.guardduty.scan(),

            "security_groups": self.security_groups.scan(),

            "cloudtrail": self.cloudtrail.scan(),

            "config": self.config.scan()

        }

    def scan_iam(self):

        return self.iam.scan()

    def scan_s3(self):

        return self.s3.scan()

    def scan_ec2(self):

        return self.ec2.scan()

    def scan_inspector(self):

        return self.inspector.scan()

    def scan_guardduty(self):

        return self.guardduty.scan()

    def scan_security_groups(self):

        return self.security_groups.scan()

    def scan_cloudtrail(self):

        return self.cloudtrail.scan()

    def scan_config(self):

        return self.config.scan()