"""
CloudShield Enterprise
Azure Services
"""

from app.cloud.azure.client import AzureClient

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

class AzureService:

    def __init__(self):

        self.client = AzureClient()

        self.virtual_machines = AzureVirtualMachines(self.client)
        self.storage = AzureStorage(self.client)
        self.resource_groups = AzureResourceGroups(self.client)
        self.keyvault = AzureKeyVault(self.client)
        self.monitor = AzureMonitor(self.client)
        self.defender = AzureDefender(self.client)
        self.identity = AzureIdentity(self.client)
        self.network = AzureNetwork(self.client)
        self.public_ips_service = AzurePublicIPs(self.client)
        self.route_tables_service = AzureRouteTables(self.client)
        self.load_balancers_service = AzureLoadBalancers(self.client)
        self.firewall_service = AzureFirewall(self.client)
        self.application_gateway_service = AzureApplicationGateway(self.client)
        self.vpn_gateway_service = AzureVPNGateway(self.client)
        self.security_analyzer = AzureAnalyzer()
        self.risk_engine = AzureRiskEngine()
        self.nat_gateway_service = AzureNATGateway(self.client)
        self.expressroute_service = AzureExpressRoute(self.client)
        self.private_endpoint_service = AzurePrivateEndpoints(self.client)
    # -------------------------------------
    # Connection Status
    # -------------------------------------

    def connected(self):

        return self.client.is_connected()

    def virtual_networks(self):

        return self.network.virtual_networks()

    def network_security_groups(self):

        return self.network.network_security_groups()

    def public_ips(self):

        return self.public_ips_service.list()

    def network_interfaces(self):

        return self.network.network_interfaces()

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

    def express_routes(self):

        return self.expressroute_service.list()
    
    def private_endpoints(self):

        return self.private_endpoint_service.list()
    # -------------------------------------
    # Dashboard Summary
    # -------------------------------------

    def summary(self):

        if not self.connected():

            return {
                "connected": False,
                "virtual_machines": 0,
                "storage_accounts": 0,
                "resource_groups": 0,
                "keyvaults": 0,
            }

        return {
            "connected": True,
            "virtual_machines": len(self.virtual_machines.list()),
            "storage_accounts": len(self.storage.list()),
            "resource_groups": len(self.resource_groups.list()),
            "keyvaults": len(self.keyvault.list()),
        }

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

            "virtual_machines": len(self.virtual_machines.list()),
            "storage_accounts": len(self.storage.list()),
            "resource_groups": len(self.resource_groups.list()),
            "keyvaults": len(self.keyvault.list()),
    
            "virtual_networks": len(self.virtual_networks()),
            "network_security_groups": len(self.network_security_groups()),
            "public_ips": len(self.public_ips()),
            "load_balancers": len(self.load_balancers()),

            "secure_score": risk["total_score"],
            "risk_level": risk["risk_level"],

            "findings": findings,
        }