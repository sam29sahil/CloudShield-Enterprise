"""
CloudShield Enterprise
Azure Virtual Machines
"""

from azure.mgmt.compute import ComputeManagementClient


class AzureVirtualMachines:

    def __init__(self, client):

        self.client = client

    # -------------------------------------
    # List Virtual Machines
    # -------------------------------------

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            compute = ComputeManagementClient(

                credential=self.client.get_credential(),

                subscription_id=self.client.subscription()

            )

            virtual_machines = []

            for vm in compute.virtual_machines.list_all():

                virtual_machines.append(

                    {

                        "name": vm.name,

                        "location": vm.location,

                        "type": vm.type,

                        "id": vm.id

                    }

                )

            return virtual_machines

        except Exception:

            return []