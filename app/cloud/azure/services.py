"""
CloudShield Enterprise
Azure Services
"""

from app.cloud.azure.client import AzureClient

from app.cloud.azure.virtual_machines import AzureVirtualMachines
from app.cloud.azure.storage import AzureStorage
from app.cloud.azure.resource_groups import AzureResourceGroups
from app.cloud.azure.keyvault import AzureKeyVault
from app.cloud.azure.monitor import AzureMonitor
from app.cloud.azure.defender import AzureDefender
from app.cloud.azure.identity import AzureIdentity
from app.cloud.azure.network import AzureNetwork
from app.cloud.azure.load_balancers import AzureLoadBalancers
from app.cloud.azure.security_analyzer import AzureSecurityAnalyzer
from app.cloud.azure.risk_engine import AzureRiskEngine


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
        self.load_balancers_service = AzureLoadBalancers(self.client)
        self.security_analyzer = AzureSecurityAnalyzer()
        self.risk_engine = AzureRiskEngine()
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

        return self.network.public_ips()
    
    def network_interfaces(self):

        return self.network.network_interfaces()
    
    def load_balancers(self):

        return self.load_balancers_service.list()

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

                "keyvaults": 0

            }

        return {

            "connected": True,

            "virtual_machines": len(
                self.virtual_machines.list()
            ),

            "storage_accounts": len(
                self.storage.list()
            ),

            "resource_groups": len(
                self.resource_groups.list()
            ),

            "keyvaults": len(
                self.keyvault.list()
            )

        }
    def security_dashboard(self):
        """
        Generate Azure security dashboard data.
        """

        if not self.connected():

            return {

                "connected": False,

                "score": 0,

                "risk_level": "Unknown",

                "findings": [],

                "summary": {}

            }

        azure_data = {

            "virtual_machines": self.virtual_machines.list(),

            "storage_accounts": self.storage.list(),

            "network_security_groups": self.network_security_groups(),

            "keyvaults": self.keyvault.list()

        }

        findings = self.security_analyzer.analyze(

            azure_data

        )

        dashboard = self.risk_engine.dashboard(

            findings

        )

        dashboard["connected"] = True

        dashboard["findings"] = findings

        return dashboard



        dashboard = self.security_dashboard()

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

            "secure_score": dashboard["score"],

            "risk_level": dashboard["risk_level"]

        }
        
            






    