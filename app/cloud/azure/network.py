"""
CloudShield Enterprise
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
    """

    def __init__(self, client):

        self.client = client

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
    # Virtual Networks
    # --------------------------------------------------

    def virtual_networks(self):

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
                        # Address Space
                        "address_space": (
                            vnet.address_space.address_prefixes
                            if vnet.address_space
                            else []
                        ),
                        # DNS Servers
                        "dns_servers": (
                            vnet.dhcp_options.dns_servers
                            if (vnet.dhcp_options and vnet.dhcp_options.dns_servers)
                            else []
                        ),
                        # Subnets
                        "subnets": len(vnet.subnets),
                        # Peering Count
                        "peerings": (
                            len(vnet.virtual_network_peerings)
                            if getattr(vnet, "virtual_network_peerings", None)
                            else 0
                        ),
                        # DDoS Protection
                        "ddos_protection": bool(
                            getattr(vnet, "enable_ddos_protection", False)
                        ),
                        # Encryption
                        "encryption": (
                            str(vnet.encryption.enabled)
                            if getattr(vnet, "encryption", None)
                            else "Unknown"
                        ),
                        # Provisioning State
                        "provisioning_state": (
                            vnet.provisioning_state
                            if hasattr(vnet, "provisioning_state")
                            else "-"
                        ),
                        # Tags
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

    def virtual_network_summary(self):

        result = self.virtual_networks()

        if not result["success"]:

            return result

        inventory = result["data"]

        return {
            "total_virtual_networks": len(inventory),
            "total_subnets": sum(v["subnets"] for v in inventory),
            "total_peerings": sum(v["peerings"] for v in inventory),
            "ddos_enabled": sum(1 for v in inventory if v["ddos_protection"]),
            "success": True,
        }

    # --------------------------------------------------
    # Network Security Groups
    # --------------------------------------------------

    def network_security_groups(self):

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
