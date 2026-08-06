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
