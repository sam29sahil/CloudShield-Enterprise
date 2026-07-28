"""
CloudShield Enterprise
Azure Networking
"""

from azure.mgmt.network import NetworkManagementClient


class AzureNetwork:

    """
    Azure Networking Service
    """

    def __init__(self, client):

        self.client = client

    # --------------------------------------------------
    # Network Client
    # --------------------------------------------------

    def network_client(self):

        return NetworkManagementClient(

            credential=self.client.get_credential(),

            subscription_id=self.client.subscription()

        )

    # --------------------------------------------------
    # Virtual Networks
    # --------------------------------------------------

    def virtual_networks(self):

        if not self.client.is_connected():

            return []

        try:

            network = self.network_client()

            vnets = []

            for vnet in network.virtual_networks.list_all():

                vnets.append({

                    "name": vnet.name,

                    "location": vnet.location,

                    "address_space":
                        vnet.address_space.address_prefixes,

                    "subnets":
                        len(vnet.subnets),

                    "id":
                        vnet.id

                })

            return vnets

        except Exception:

            return []

    # --------------------------------------------------
    # Subnets
    # --------------------------------------------------

    def subnets(self):

        if not self.client.is_connected():

            return []

        try:

            network = self.network_client()

            subnets = []

            for vnet in network.virtual_networks.list_all():

                resource_group = vnet.id.split("/")[4]

                for subnet in network.subnets.list(

                        resource_group,

                        vnet.name

                ):

                    subnets.append({

                        "name": subnet.name,

                        "vnet": vnet.name,

                        "address_prefix":
                            subnet.address_prefix,

                        "id":
                            subnet.id

                    })

            return subnets

        except Exception:

            return []

    # --------------------------------------------------
    # Network Security Groups
    # --------------------------------------------------

    def network_security_groups(self):

        if not self.client.is_connected():

            return []

        try:

            network = self.network_client()

            groups = []

            for nsg in network.network_security_groups.list_all():

                groups.append({

                    "name": nsg.name,

                    "location": nsg.location,

                    "rules":
                        len(nsg.security_rules),

                    "id":
                        nsg.id

                })

            return groups

        except Exception:

            return []
    # --------------------------------------------------
# Network Interfaces
# --------------------------------------------------

    def network_interfaces(self):

        if not self.client.is_connected():

            return []

        try:

            client = self.network_client()

            interfaces = []

            for nic in client.network_interfaces.list_all():

                private_ip = None

                subnet = None

                public_ip = None

                if nic.ip_configurations:

                    config = nic.ip_configurations[0]

                    private_ip = config.private_ip_address

                    if config.subnet:
                        subnet = config.subnet.id.split("/")[-1]

                    if config.public_ip_address:
                        public_ip = config.public_ip_address.id

                interfaces.append({

                    "name": nic.name,

                    "location": nic.location,

                    "resource_group": nic.id.split("/")[4],

                    "private_ip": private_ip,

                    "public_ip": public_ip,

                    "subnet": subnet,

                    "mac_address": nic.mac_address,

                    "id": nic.id

                })

            return interfaces

        except Exception as e:

            print("Azure NIC Error:", e)

            return []    