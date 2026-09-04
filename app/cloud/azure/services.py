"""
CloudShield Enterprise
Azure Services
"""

from typing import Any

from app.cloud.azure.client import AzureClient, AzureConfigurationError

from app.cloud.azure.firewall import AzureFirewall
from app.cloud.azure.route_tables import AzureRouteTables
from app.cloud.azure.virtual_machines import AzureVirtualMachines
from app.cloud.azure.storage import AzureStorage
from app.cloud.azure.resource_groups import AzureResourceGroups
from app.cloud.azure.keyvault import AzureKeyVault
from app.cloud.azure.monitor import AzureMonitor
from app.cloud.azure.defender import AzureDefender
from app.cloud.azure.identity import AzureIdentity
from app.cloud.azure.network import AzureNetwork
from app.cloud.azure.load_balancers import AzureLoadBalancers
from app.cloud.azure.analyzer import AzureAnalyzer
from app.cloud.azure.risk import AzureRiskEngine
from app.cloud.azure.public_ips import AzurePublicIPs
from app.cloud.azure.nat_gateway import AzureNATGateway
from app.cloud.azure.application_gateway import AzureApplicationGateway
from app.cloud.azure.vpn_gateway import AzureVPNGateway
from app.cloud.azure.expressroute import AzureExpressRoute
from app.cloud.azure.private_endpoints import AzurePrivateEndpoints
from app.cloud.azure.bastion import AzureBastion
from app.cloud.azure.vm_scale_sets import AzureVMScaleSets
from app.cloud.azure.managed_disks import AzureManagedDisks
from app.cloud.azure.snapshots import AzureSnapshots
from app.cloud.azure.images import AzureImages
from app.cloud.azure.availability_sets import AzureAvailabilitySets
from app.cloud.azure.blob_containers import AzureBlobContainers
from app.cloud.azure.file_shares import AzureFileShares
from app.cloud.azure.queues import AzureQueues
from app.cloud.azure.tables import AzureTables
from app.cloud.azure.policy import AzurePolicy
from app.cloud.azure.rbac import AzureRBAC
from app.cloud.azure.advisor import AzureAdvisor
from app.cloud.azure.log_analytics import AzureLogAnalytics
from app.cloud.azure.managed_identity import AzureManagedIdentity
from app.cloud.azure.sql_database import AzureSQL
from app.cloud.azure.cosmos_db import AzureCosmosDB
from app.cloud.azure.security_service import AzureSecurityService

# Optional database services
# from app.cloud.azure.postgresql import AzurePostgreSQL
# from app.cloud.azure.mysql import AzureMySQL

from azure.mgmt.network import NetworkManagementClient


class AzureService:

    def __init__(self):

        # ==========================================
        # Main Azure Client
        # ==========================================

        self.client = AzureClient()

        # ==========================================
        # Core Azure Services
        # ==========================================

        self.virtual_machines = AzureVirtualMachines(self.client)
        self.storage = AzureStorage(self.client)
        self.resource_groups = AzureResourceGroups(self.client)
        self.keyvault = AzureKeyVault(self.client)

        # Optional MySQL
        # self.mysql_service = AzureMySQL(self.client)

        self.sql_service = AzureSQL(self.client)
        self.cosmos_db_service = AzureCosmosDB(self.client)

        # ==========================================
        # Monitoring / Security / Governance
        # ==========================================

        self.monitor = AzureMonitor(self.client)
        self.advisor_service = AzureAdvisor(self.client)
        self.policy_service = AzurePolicy(self.client)
        self.defender = AzureDefender(self.client)

        # ==========================================
        # Identity
        # ==========================================

        self.identity = AzureIdentity(self.client)
        self.rbac_service = AzureRBAC(self.client)
        self.managed_identity_service = AzureManagedIdentity(self.client)

        # ==========================================
        # Network Services
        # ==========================================

        self.network = AzureNetwork(self.client)

        self.public_ips_service = AzurePublicIPs(self.client)
        self.route_tables_service = AzureRouteTables(self.client)
        self.load_balancers_service = AzureLoadBalancers(self.client)
        self.firewall_service = AzureFirewall(self.client)
        self.application_gateway_service = AzureApplicationGateway(self.client)
        self.bastion_service = AzureBastion(self.client)
        self.vpn_gateway_service = AzureVPNGateway(self.client)
        self.nat_gateway_service = AzureNATGateway(self.client)
        self.expressroute_service = AzureExpressRoute(self.client)
        self.private_endpoint_service = AzurePrivateEndpoints(self.client)

        # ==========================================
        # Storage Services
        # ==========================================

        self.table_service = AzureTables(self.client)
        self.queue_service = AzureQueues(self.client)
        self.file_share_service = AzureFileShares(self.client)
        self.blob_container_service = AzureBlobContainers(self.client)

        # ==========================================
        # Compute Services
        # ==========================================

        self.image_service = AzureImages(self.client)
        self.availability_set_service = AzureAvailabilitySets(self.client)
        self.snapshot_service = AzureSnapshots(self.client)
        self.managed_disk_service = AzureManagedDisks(self.client)
        self.vm_scale_set_service = AzureVMScaleSets(self.client)

        # ==========================================
        # Analytics
        # ==========================================

        self.log_analytics_service = AzureLogAnalytics(self.client)

        # ==========================================
        # Security Scanner
        # ==========================================

        self.security_analyzer = AzureAnalyzer()
        self.risk_engine = AzureRiskEngine()
        self.security_service = AzureSecurityService(self.client)

        # ==========================================
        # Optional PostgreSQL
        # ==========================================

        # self.postgresql_service = AzurePostgreSQL(self.client)

    # ==========================================
    # Connection Status
    # ==========================================

    def connected(self):
        return self.client.is_connected()

    def configuration_error(self):
        return self.client.configuration_error

    # ==========================================
    # Advisor
    # ==========================================

    def advisor(self):
        return self.advisor_service.list()

    # ==========================================
    # Networking
    # ==========================================

    def virtual_networks(self):
        return self.network.virtual_networks()

    def network_security_groups(self):
        return self.network.network_security_groups()

    def network_interfaces(self):
        return self.network.network_interfaces()

    # ==========================================
    # Governance / Identity
    # ==========================================

    def policies(self):
        return self.policy_service.list()

    def rbac(self):
        return self.rbac_service.list()

    def managed_identity(self):
        return self.managed_identity_service.list()

    # ==========================================
    # Storage
    # ==========================================

    def file_shares(self):
        return self.file_share_service.list()

    def log_analytics(self):
        return self.log_analytics_service.list()

    # ==========================================
    # Databases
    # ==========================================

    def sql_databases(self):
        return self.sql_service.list()

    def cosmos_db(self):
        return self.cosmos_db_service.list()

    # ==========================================
    # Public Networking
    # ==========================================

    def public_ips(self):
        return self.public_ips_service.list()

    def load_balancers(self):
        return self.load_balancers_service.list()

    def route_tables(self):
        return self.route_tables_service.list()

    def firewalls(self):
        return self.firewall_service.list()

    def nat_gateways(self):
        return self.nat_gateway_service.list()

    def application_gateways(self):
        return self.application_gateway_service.list()

    def vpn_gateways(self):
        return self.vpn_gateway_service.list()

    def private_endpoints(self):
        return self.private_endpoint_service.list()

    def bastion_hosts(self):
        return self.bastion_service.list()

    def express_routes(self):
        return self.expressroute_service.list()

    # ==========================================
    # Storage Resources
    # ==========================================

    def tables(self):
        return self.table_service.list()

    def queues(self):
        return self.queue_service.list()

    def blob_containers(self):
        return self.blob_container_service.list()

    # ==========================================
    # Compute Resources
    # ==========================================

    def vm_scale_sets(self):
        return self.vm_scale_set_service.list()

    def managed_disks(self):
        return self.managed_disk_service.list()

    def snapshots(self):
        return self.snapshot_service.list()

    def images(self):
        return self.image_service.list()

    def availability_sets(self):
        return self.availability_set_service.list()

    # ==========================================
    # Azure Security Scan
    # ==========================================

    def security_scan(self, user_id=None, project_id=None):
        return self.security_service.scan(
            user_id=user_id,
            project_id=project_id,
        )

    # ==========================================
    # Dashboard Summary
    # ==========================================

    def summary(self) -> dict[str, Any]:

        connection: dict[str, Any] = self.client.connection_status()

        if not connection["connected"]:
            return {
                "connected": False,
                "status": connection["status"],
                "error": connection["error"],
                "virtual_machines": "-",
                "storage_accounts": "-",
                "resource_groups": "-",
                "keyvaults": "-",
            }

        try:
            virtual_machines: dict[str, Any] = self.virtual_machines.list()
            resource_groups: dict[str, Any] = self.resource_groups.list()
            keyvaults: dict[str, Any] = self.keyvault.list()
            storage_accounts: list[Any] = list(
                self.client.storage_client().storage_accounts.list()
            )

            results = {
                "virtual_machines": virtual_machines,
                "resource_groups": resource_groups,
                "keyvaults": keyvaults,
            }
            if any(not result.get("success") for result in results.values()):
                failed = next(
                    result for result in results.values() if not result.get("success")
                )
                raise RuntimeError(failed.get("error", "Azure resource access failed."))

            return {
                "connected": True,
                "status": "connected",
                "error": "",
                "virtual_machines": virtual_machines["count"],
                "storage_accounts": len(storage_accounts),
                "resource_groups": resource_groups["count"],
                "keyvaults": keyvaults["count"],
            }

        except Exception as error:
            status, message = self.client._error_status(error)
            return {
                "connected": False,
                "status": status,
                "error": message,
                "virtual_machines": "-",
                "storage_accounts": "-",
                "resource_groups": "-",
                "keyvaults": "-",
            }

    # ==========================================
    # Security Dashboard
    # ==========================================

    def security_dashboard(self):
        """
        Generate Azure security dashboard data.
        """

        if not self.connected():
            return {
                "connected": False,
                "virtual_machines": 0,
                "storage_accounts": 0,
                "resource_groups": 0,
                "keyvaults": 0,
                "virtual_networks": 0,
                "network_security_groups": 0,
                "public_ips": 0,
                "load_balancers": 0,
                "secure_score": 0,
                "risk_level": "Unknown",
                "findings": [],
            }

        azure_data = {
            "virtual_machines": self.virtual_machines.list()["data"],
            "storage_accounts": self.storage.list()["data"],
            "network_security_groups": self.network_security_groups()["data"],
            "keyvaults": self.keyvault.list()["data"],
        }

        findings = self.security_analyzer.analyze(azure_data)

        risk = self.risk_engine.calculate(findings)

        return {
            "connected": True,

            "virtual_machines": len(
                self.virtual_machines.list()["data"]
            ),

            "storage_accounts": len(
                self.storage.list()["data"]
            ),

            "resource_groups": len(
                self.resource_groups.list()["data"]
            ),

            "keyvaults": len(
                self.keyvault.list()["data"]
            ),

            "virtual_networks": len(
                self.virtual_networks()["data"]
            ),

            "network_security_groups": len(
                self.network_security_groups()["data"]
            ),

            "public_ips": len(
                self.public_ips()["data"]
            ),

            "load_balancers": len(
                self.load_balancers()["data"]
            ),

            "secure_score": risk["total_score"],
            "risk_level": risk["risk_level"],
            "findings": findings,
        }