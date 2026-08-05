"""
CloudShield Enterprise
<<<<<<< HEAD
Azure Networking Service
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.network import NetworkManagementClient

logger = logging.getLogger(__name__)


class AzureNetwork:
    """
    Azure Network Inventory Service
=======
Azure Networking
"""

from azure.mgmt.network import NetworkManagementClient


class AzureNetwork:

    """
    Azure Networking Service
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    """

    def __init__(self, client):

        self.client = client

<<<<<<< HEAD
        self.network = NetworkManagementClient(
            credential=self.client.get_credential(),
            subscription_id=self.client.subscription(),
        )

    # --------------------------------------------------
    # Helpers
    # --------------------------------------------------

    @staticmethod
    def resource_group(resource_id):

        try:

            return resource_id.split("/")[4]

        except Exception:

            return "-"

    # --------------------------------------------------
=======
    # --------------------------------------------------
    # Network Client
    # --------------------------------------------------

    def network_client(self):

        return NetworkManagementClient(

            credential=self.client.get_credential(),

            subscription_id=self.client.subscription()

        )

    # --------------------------------------------------
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # Virtual Networks
    # --------------------------------------------------

    def virtual_networks(self):

<<<<<<< HEAD
        started = perf_counter()

        if not self.client.is_connected():

            return {
                "success": False,
                "count": 0,
                "data": [],
                "execution_time": 0,
                "error": "Azure connection failed.",
            }

        inventory = []

        try:

            logger.info("Collecting Azure Virtual Networks...")

            for vnet in self.network.virtual_networks.list_all():

                inventory.append(
                    {
                        "id": vnet.id,
                        "name": vnet.name,
                        "resource_group": self.resource_group(vnet.id),
                        "location": vnet.location,
                        "address_space": (
                            vnet.address_space.address_prefixes
                            if vnet.address_space
                            else []
                        ),
                        "dns_servers": (
                            vnet.dhcp_options.dns_servers
                            if (vnet.dhcp_options and vnet.dhcp_options.dns_servers)
                            else []
                        ),
                        "subnets": len(vnet.subnets),
                        "tags": vnet.tags or {},
                    }
                )

            return {
                "success": True,
                "count": len(inventory),
                "data": inventory,
                "execution_time": round(perf_counter() - started, 3),
                "error": "",
            }

        except Exception as error:

            logger.exception(error)

            return {
                "success": False,
                "count": 0,
                "data": [],
                "execution_time": round(perf_counter() - started, 3),
                "error": str(error),
            }
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # --------------------------------------------------
    # Network Security Groups
    # --------------------------------------------------

    def network_security_groups(self):

<<<<<<< HEAD
        started = perf_counter()

        if not self.client.is_connected():

            return {
                "success": False,
                "count": 0,
                "data": [],
                "execution_time": 0,
                "error": "Azure connection failed.",
            }

        inventory = []

        try:

            logger.info("Collecting Azure Network Security Groups...")

            for nsg in self.network.network_security_groups.list_all():

                security_rules = []

                if nsg.security_rules:

                    for rule in nsg.security_rules:

                        security_rules.append(
                            {
                                "name": rule.name,
                                "priority": rule.priority,
                                "direction": rule.direction,
                                "access": rule.access,
                                "protocol": rule.protocol,
                                "source": rule.source_address_prefix,
                                "destination": rule.destination_address_prefix,
                                "destination_port": rule.destination_port_range,
                                "source_port": rule.source_port_range,
                                "description": rule.description,
                            }
                        )

                inventory.append(
                    {
                        "id": nsg.id,
                        "name": nsg.name,
                        "resource_group": self.resource_group(nsg.id),
                        "location": nsg.location,
                        "rules": security_rules,
                        "rule_count": len(security_rules),
                        "tags": nsg.tags or {},
                    }
                )

            return {
                "success": True,
                "count": len(inventory),
                "data": inventory,
                "execution_time": round(perf_counter() - started, 3),
                "error": "",
            }

        except Exception as error:

            logger.exception(error)

            return {
                "success": False,
                "count": 0,
                "data": [],
                "execution_time": round(perf_counter() - started, 3),
                "error": str(error),
            }
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
