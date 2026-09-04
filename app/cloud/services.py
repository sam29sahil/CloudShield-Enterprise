"""
CloudShield Enterprise
Cloud Services
"""

from app.models.asset import Asset
from app.models.finding import Finding
from app.models.security_scan import SecurityScan

from app.cloud.aws.services import AWSScanner
from app.cloud.azure.services import AzureService
from app.cloud.findings_engine import CloudFindingsEngine
from app.cloud.azure.analyzer import AzureAnalyzer
from app.cloud.azure.risk import AzureRiskEngine
from app.cloud.azure.recommendations import RecommendationEngine
from app.cloud.azure.client import AzureConfigurationError


# ==================================================
# Provider Services
# ==================================================

aws = AWSScanner()

class LazyAzureService:

    def __init__(self):
        self._service = None

    def _get_service(self):
        if self._service is None:
            self._service = AzureService()
        return self._service

    def __getattr__(self, name):
        return getattr(self._get_service(), name)


azure = LazyAzureService()

analyzer = AzureAnalyzer()
risk_engine = AzureRiskEngine()
recommendations = RecommendationEngine()


class CloudService:
    """
    Enterprise Cloud Service
    """

    # ==================================================
    # Service Status
    # ==================================================

    def service_status(self, result):
        """
        Return service connection status.
        """

        if result.get("success"):
            return {
                "label": "Connected",
                "color": "success",
            }

        error = str(result.get("error", "")).lower()

        if "credential" in error:
            return {
                "label": "Waiting",
                "color": "warning",
            }

        if "region" in error:
            return {
                "label": "Configuration",
                "color": "warning",
            }

        return {
            "label": "Error",
            "color": "danger",
        }

    # ==================================================
    # Enterprise Cloud Dashboard
    # ==================================================

    def dashboard(self):
        """
        Enterprise Cloud Dashboard.
        """

        # ------------------------------
        # AWS Services
        # ------------------------------

        ec2 = aws.scan_ec2()
        s3 = aws.scan_s3()
        iam = aws.scan_iam()
        security_groups = aws.scan_security_groups()
        cloudtrail = aws.scan_cloudtrail()
        guardduty = aws.scan_guardduty()
        inspector = aws.scan_inspector()

        # ------------------------------
        # Azure Summary
        # ------------------------------

        azure_summary = azure.summary()

        # ------------------------------
        # Results
        # ------------------------------

        results = {
            "ec2": ec2,
            "s3": s3,
            "iam": iam,
            "security_groups": security_groups,
            "cloudtrail": cloudtrail,
            "guardduty": guardduty,
            "inspector": inspector,
        }

        score = self.calculate_score(results)

        findings_engine = CloudFindingsEngine()

        cloud_findings = findings_engine.generate(results)

        dashboard = {
            "provider": "Azure",
            "region": "Central India",
            "score": score,
            "resources": Asset.query.count(),
            "assets": Asset.query.count(),
            "findings_count": Finding.query.count(),
            "scans": SecurityScan.query.count(),
            "cloud_findings": cloud_findings,
            "aws": {
                "ec2": ec2.get("total_instances", 0),
                "s3": s3.get("total_buckets", 0),
                "iam": iam.get("total_users", 0),
                "security_groups": security_groups.get(
                    "total_groups",
                    0,
                ),
            },

            "cloudtrail": cloudtrail.get(
                "total_trails",
                0,
            ),

            "guardduty": len(
                guardduty.get(
                    "detectors",
                    [],
                )
            ),

            "inspector": inspector.get(
                "total_findings",
                0,
            ),

            "azure": azure_summary,

            "service_status": {
                "ec2": self.service_status(ec2),
                "s3": self.service_status(s3),
                "iam": self.service_status(iam),
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
                ),
            },
        }

        return dashboard

    # ==================================================
    # AWS Services
    # ==================================================

    def ec2(self):
        return aws.scan_ec2()

    def s3(self):
        return aws.scan_s3()

    def iam(self):
        return aws.scan_iam()

    def security_groups(self):
        return aws.scan_security_groups()

    def cloudtrail(self):
        return aws.scan_cloudtrail()

    def guardduty(self):
        return aws.scan_guardduty()

    def inspector(self):
        return aws.scan_inspector()

    def config(self):
        return aws.scan_config()

    # ==================================================
    # Full AWS Scan
    # ==================================================

    def full_scan(self):
        return aws.scan()

    # ==================================================
    # Azure Dashboard
    # ==================================================

    def azure_dashboard(self):
        """
        Generate Azure dashboard data using
        the existing Azure security scanner.
        """

        if azure.configuration_error():
            return azure.summary()

        summary = azure.summary()

        security_scan = azure.security_scan()

        score = security_scan.get(
            "score",
            {},
        )

        risk = security_scan.get(
            "risk",
            {},
        )

        findings = security_scan.get(
            "findings",
            [],
        )

        summary.update(
            {
                "subscription_name": azure.client.subscription(),
                "region": summary.get(
                    "region",
                    "Central India",
                ),
                "secure_score": score.get(
                    "security_score",
                    0,
                ),
                "risk_level": risk.get(
                    "risk_level",
                    "Unknown",
                ),
                "findings": findings,
                "security": security_scan,
            }
        )

        return summary

    # ==================================================
    # Azure Compute
    # ==================================================

    def azure_virtual_machines(self):
        return azure.virtual_machines.list()

    def azure_vm_scale_sets(self):
        return azure.vm_scale_sets()

    def azure_managed_disks(self):
        return azure.managed_disks()

    def azure_snapshots(self):
        return azure.snapshots()

    def azure_images(self):
        return azure.images()

    def azure_availability_sets(self):
        return azure.availability_sets()

    # ==================================================
    # Azure Storage
    # ==================================================

    def azure_storage(self):
        return azure.storage.list()

    def azure_blob_containers(self):
        return azure.blob_containers()

    def azure_file_shares(self):
        return azure.file_shares()

    def azure_queues(self):
        return azure.queues()

    def azure_tables(self):
        return azure.tables()

    # ==================================================
    # Azure Resource Groups
    # ==================================================

    def azure_resource_groups(self):
        return azure.resource_groups.list()

    # ==================================================
    # Azure Networking
    # ==================================================

    def azure_virtual_networks(self):
        return azure.virtual_networks()

    def azure_network_security_groups(self):
        return azure.network_security_groups()

    def azure_network_interfaces(self):
        return azure.network_interfaces()

    def azure_public_ips(self):
        return azure.public_ips()

    def azure_route_tables(self):
        return azure.route_tables()

    def azure_load_balancers(self):
        return azure.load_balancers()

    def azure_firewalls(self):
        return azure.firewalls()

    def azure_nat_gateways(self):
        return azure.nat_gateways()

    def azure_application_gateways(self):
        return azure.application_gateways()

    def azure_vpn_gateways(self):
        return azure.vpn_gateways()

    def azure_express_routes(self):
        return azure.express_routes()

    def azure_private_endpoints(self):
        return azure.private_endpoints()

    def azure_bastion_hosts(self):
        return azure.bastion_hosts()

    # ==================================================
    # Azure Identity / Governance
    # ==================================================

    def azure_managed_identity(self):
        return azure.managed_identity()

    def azure_identity(self):
        return azure.identity.information()

    def azure_rbac(self):
        return azure.rbac()

    def azure_policies(self):
        return azure.policies()

    # ==================================================
    # Azure Security
    # ==================================================

    def azure_keyvault(self):
        return azure.keyvault.list()

    def azure_monitor(self):
        return azure.monitor.overview()

    def azure_defender(self):
        return azure.defender.overview()

    def azure_advisor(self):
        return azure.advisor()

    def azure_log_analytics(self):
        return azure.log_analytics()

    # ==================================================
    # Azure Databases
    # ==================================================

    def azure_sql_databases(self):
        return azure.sql_databases()

    def azure_cosmos_db(self):
        return azure.cosmos_db()

    # ==================================================
    # Azure Security Scan
    # ==================================================

    def azure_security_scan(
        self,
        user_id=None,
        project_id=None,
    ):
        if azure.configuration_error():
            raise AzureConfigurationError(azure.configuration_error())

        return azure.security_scan(
            user_id=user_id,
            project_id=project_id,
        )

    # ==================================================
    # Enterprise Cloud Security Score
    # ==================================================

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
            "inspector": 10,
        }

        score = 0

        for service, weight in weights.items():

            result = results.get(
                service,
                {},
            )

            if result.get(
                "success",
                False,
            ):
                score += weight

            else:
                error = str(
                    result.get(
                        "error",
                        "",
                    )
                ).lower()

                if "credential" in error:
                    score += weight * 0.5

        return round(score)

    # ==================================================
    # Azure Summary
    # ==================================================

    def azure_summary(self):
        """
        Return Azure dashboard summary.
        """

        return azure.summary()

    # ==================================================
    # Health Check
    # ==================================================

    def health(self):
        """
        Basic service health.
        """

        return {
            "aws": True,
            "azure": azure.client.is_connected(),
        }
