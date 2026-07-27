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

    # -------------------------------------
    # Connection Status
    # -------------------------------------

    def connected(self):

        return self.client.is_connected()

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