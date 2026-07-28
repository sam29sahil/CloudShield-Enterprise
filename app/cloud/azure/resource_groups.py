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

                resource_count = 0

                try:

                    resources = resource_client.resources.list_by_resource_group(
                        group.name
                    )

                    resource_count = sum(1 for _ in resources)

                except Exception:
                    pass

                tags = group.tags or {}

                groups.append(

                    {

                        "name": group.name,

                        "location": group.location,

                        "id": group.id,

                        "managed_by": group.managed_by,

                        "provisioning_state": group.properties.provisioning_state
                        if group.properties else "Unknown",

                        "tags": tags,

                        "resource_count": resource_count,

                        "risk": self.calculate_risk(
                            resource_count,
                            tags
                        )

                    }

                )

            return groups

        except Exception as e:

            print("Azure Resource Groups Error:", e)

            return []

    # ----------------------------------
    # Risk Calculation
    # ----------------------------------

    def calculate_risk(self, resource_count, tags):

        score = 0

        if resource_count == 0:
            score += 1

        if len(tags) == 0:
            score += 1

        if score == 0:
            return "Low"

        if score == 1:
            return "Medium"

        return "High"