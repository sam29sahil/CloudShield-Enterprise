"""
CloudShield Enterprise
Cloud Services
"""

from app.models.asset import Asset
from app.models.finding import Finding
from app.models.security_scan import SecurityScan

from app.cloud.aws.services import AWSScanner
<<<<<<< HEAD
from app.cloud.azure.services import AzureService
=======
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
from app.cloud.findings_engine import CloudFindingsEngine


aws = AWSScanner()
<<<<<<< HEAD
azure = AzureService()
=======
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40


class CloudService:
    """
    Enterprise Cloud Service
    """

    # --------------------------------------------------
    # Service Status
    # --------------------------------------------------

    def service_status(self, result):
<<<<<<< HEAD
=======
        """
        Return enterprise status for AWS services.
        """
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40

        if result.get("success"):

            return {
<<<<<<< HEAD
                "label": "Connected",
                "color": "success"
            }

        error = str(result.get("error", "")).lower()
=======

                "label": "Connected",

                "color": "success"

            }

        error = str(
            result.get(
                "error",
                ""
            )
        ).lower()
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40

        if "credential" in error:

            return {
<<<<<<< HEAD
                "label": "Waiting",
                "color": "warning"
=======

                "label": "Waiting",

                "color": "warning"

>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
            }

        if "region" in error:

            return {
<<<<<<< HEAD
                "label": "Configuration",
                "color": "warning"
            }

        return {
            "label": "Error",
            "color": "danger"
=======

                "label": "Configuration",

                "color": "warning"

            }

        return {

            "label": "Error",

            "color": "danger"

>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
        }

    # --------------------------------------------------
    # Dashboard
    # --------------------------------------------------

    def dashboard(self):
<<<<<<< HEAD

        # ---------------- AWS ----------------
=======
        """
        Enterprise Cloud Dashboard
        """
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40

        ec2 = aws.scan_ec2()

        s3 = aws.scan_s3()

        iam = aws.scan_iam()

        security_groups = aws.scan_security_groups()

        cloudtrail = aws.scan_cloudtrail()

        guardduty = aws.scan_guardduty()

        inspector = aws.scan_inspector()

<<<<<<< HEAD
        # ---------------- Azure ----------------

        azure_summary = azure.summary()

        # ---------------- Results ----------------

=======
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
        results = {

            "ec2": ec2,

            "s3": s3,

            "iam": iam,

            "security_groups": security_groups,

            "cloudtrail": cloudtrail,

            "guardduty": guardduty,

            "inspector": inspector

        }

        score = self.calculate_score(results)

        engine = CloudFindingsEngine()

        cloud_findings = engine.generate(results)

        return {

<<<<<<< HEAD
            "provider": "Multi Cloud",
=======
            "provider": "AWS",
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40

            "region": "ap-south-1",

            "score": score,

            "resources": Asset.query.count(),

            "assets": Asset.query.count(),

            "findings": Finding.query.count(),

            "scans": SecurityScan.query.count(),

            "cloud_findings": cloud_findings,

<<<<<<< HEAD
            # ---------------- AWS ----------------

=======
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
            "ec2": ec2.get(
                "total_instances",
                0
            ),

            "s3": s3.get(
                "total_buckets",
                0
            ),

            "iam": iam.get(
                "total_users",
                0
            ),

            "security_groups": security_groups.get(
                "total_groups",
                0
            ),

            "cloudtrail": cloudtrail.get(
                "total_trails",
                0
            ),

            "guardduty": len(
                guardduty.get(
                    "detectors",
                    []
                )
            ),

            "inspector": inspector.get(
                "total_findings",
                0
            ),

<<<<<<< HEAD
            # ---------------- Azure ----------------

            "azure": azure_summary,

            # ---------------- Status ----------------

            "service_status": {

                "ec2": self.service_status(ec2),

                "s3": self.service_status(s3),

                "iam": self.service_status(iam),
=======
            "service_status": {

                "ec2": self.service_status(
                    ec2
                ),

                "s3": self.service_status(
                    s3
                ),

                "iam": self.service_status(
                    iam
                ),
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40

                "security_groups": self.service_status(
                    security_groups
                ),

                "cloudtrail": self.service_status(
                    cloudtrail
                ),

                "guardduty": self.service_status(
                    guardduty
                ),

                "inspector": self.service_status(
                    inspector
                )

            }

        }
<<<<<<< HEAD
        # --------------------------------------------------
    # AWS Services
=======

    # --------------------------------------------------
    # EC2
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
    # --------------------------------------------------

    def ec2(self):

        return aws.scan_ec2()

<<<<<<< HEAD
=======
    # --------------------------------------------------
    # S3
    # --------------------------------------------------

>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
    def s3(self):

        return aws.scan_s3()

<<<<<<< HEAD
=======
    # --------------------------------------------------
    # IAM
    # --------------------------------------------------

>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
    def iam(self):

        return aws.scan_iam()

<<<<<<< HEAD
=======
    # --------------------------------------------------
    # Security Groups
    # --------------------------------------------------

>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
    def security_groups(self):

        return aws.scan_security_groups()

<<<<<<< HEAD
=======
    # --------------------------------------------------
    # CloudTrail
    # --------------------------------------------------

>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
    def cloudtrail(self):

        return aws.scan_cloudtrail()

<<<<<<< HEAD
=======
    # --------------------------------------------------
    # GuardDuty
    # --------------------------------------------------

>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
    def guardduty(self):

        return aws.scan_guardduty()

<<<<<<< HEAD
=======
    # --------------------------------------------------
    # Inspector
    # --------------------------------------------------

>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
    def inspector(self):

        return aws.scan_inspector()

<<<<<<< HEAD
=======
    # --------------------------------------------------
    # AWS Config
    # --------------------------------------------------

>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
    def config(self):

        return aws.scan_config()

<<<<<<< HEAD
    def full_scan(self):

        return aws.scan()

    # --------------------------------------------------
    # Azure Dashboard
    # --------------------------------------------------

    def azure_dashboard(self):

        return azure.summary()

    # --------------------------------------------------
    # Azure Virtual Machines
    # --------------------------------------------------

    def azure_virtual_machines(self):

        return azure.virtual_machines.list()

    # --------------------------------------------------
    # Azure Storage
    # --------------------------------------------------

    def azure_storage(self):

        return azure.storage.list()

    # --------------------------------------------------
    # Azure Resource Groups
    # --------------------------------------------------

    def azure_resource_groups(self):

        return azure.resource_groups.list()

    # --------------------------------------------------
    # Azure Key Vault
    # --------------------------------------------------

    def azure_keyvault(self):

        return azure.keyvault.list()

    # --------------------------------------------------
    # Azure Monitor
    # --------------------------------------------------

    def azure_monitor(self):

        return azure.monitor.overview()

    # --------------------------------------------------
    # Azure Defender
    # --------------------------------------------------

    def azure_defender(self):

        return azure.defender.overview()

    # --------------------------------------------------
    # Azure Identity
    # --------------------------------------------------

    def azure_identity(self):

        return azure.identity.information()

        # --------------------------------------------------
    # Enterprise Cloud Security Score
    # --------------------------------------------------

=======
    # --------------------------------------------------
    # Full AWS Scan
    # --------------------------------------------------

    def full_scan(self):

        return aws.scan()
    
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
    def calculate_score(self, results):
        """
        Calculate Enterprise Cloud Security Score.
        """

        weights = {

            "ec2": 15,

            "s3": 20,

            "iam": 20,

            "security_groups": 15,

            "cloudtrail": 10,

            "guardduty": 10,

            "inspector": 10

        }

        score = 0

        for service, weight in weights.items():

            result = results.get(service, {})

            if result.get("success"):

                score += weight

            else:

                error = str(
                    result.get(
                        "error",
                        ""
                    )
                ).lower()

                if "credential" in error:

                    score += weight * 0.5

        return round(score)