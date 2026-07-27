"""
CloudShield Enterprise
Azure Resource Groups
"""

from azure.mgmt.resource.resources import ResourceManagementClient


class AzureResourceGroups:

    def __init__(self, client):

        self.client = client

    # ----------------------------------
    # List Resource Groups
    # ----------------------------------

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            resource_client = ResourceManagementClient(

                credential=self.client.get_credential(),

                subscription_id=self.client.subscription()

            )

            groups = []

            for group in resource_client.resource_groups.list():

                groups.append(

                    {

                        "name": group.name,

                        "location": group.location,

                        "id": group.id

                    }

                )

            return groups

        except Exception:

            return []