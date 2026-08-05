"""
CloudShield Enterprise
Azure Load Balancers
"""

from azure.mgmt.network import NetworkManagementClient


class AzureLoadBalancers:

    def __init__(self, client):

        self.client = client

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            network = NetworkManagementClient(
<<<<<<< HEAD
                credential=self.client.get_credential(),
                subscription_id=self.client.subscription(),
=======

                credential=self.client.get_credential(),

                subscription_id=self.client.subscription()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )

            load_balancers = []

            for lb in network.load_balancers.list_all():

                load_balancers.append(
<<<<<<< HEAD
                    {
                        "name": lb.name,
                        "location": lb.location,
                        "resource_group": lb.id.split("/")[4],
                        "frontend_ips": len(lb.frontend_ip_configurations),
                        "backend_pools": len(lb.backend_address_pools),
                        "probes": len(lb.probes),
                        "rules": len(lb.load_balancing_rules),
                        "sku": lb.sku.name if lb.sku else "-",
                        "id": lb.id,
                    }
=======

                    {

                        "name": lb.name,

                        "location": lb.location,

                        "resource_group": lb.id.split("/")[4],

                        "frontend_ips":
                            len(lb.frontend_ip_configurations),

                        "backend_pools":
                            len(lb.backend_address_pools),

                        "probes":
                            len(lb.probes),

                        "rules":
                            len(lb.load_balancing_rules),

                        "sku":
                            lb.sku.name if lb.sku else "-",

                        "id":
                            lb.id

                    }

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                )

            return load_balancers

        except Exception as e:

            print("Azure Load Balancer Error:", e)

<<<<<<< HEAD
            return []
=======
            return []
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
