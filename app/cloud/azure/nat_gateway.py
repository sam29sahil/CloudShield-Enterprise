"""
CloudShield Enterprise
Azure NAT Gateway
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.network import NetworkManagementClient

logger = logging.getLogger(__name__)


class AzureNATGateway:
    """
    Azure NAT Gateway Inventory
    """

    def __init__(self, client):

        self.client = client

        self.network = NetworkManagementClient(
            credential=self.client.get_credential(),
            subscription_id=self.client.subscription(),
        )

    @staticmethod
    def resource_group(resource_id):

        try:
            return resource_id.split("/")[4]
        except Exception:
            return "-"

    def list(self):

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

            logger.info("Collecting Azure NAT Gateways...")

            for gateway in self.network.nat_gateways.list_all():

                inventory.append(
                    {
                        "id": gateway.id,
                        "name": gateway.name,
                        "resource_group": self.resource_group(gateway.id),
                        "location": gateway.location,
                        "sku": gateway.sku.name if gateway.sku else "-",
                        "idle_timeout": gateway.idle_timeout_in_minutes,
                        "public_ips": (
                            len(gateway.public_ip_addresses)
                            if gateway.public_ip_addresses
                            else 0
                        ),
                        "public_ip_prefixes": (
                            len(gateway.public_ip_prefixes)
                            if gateway.public_ip_prefixes
                            else 0
                        ),
                        "subnets": (
                            len(gateway.subnets)
                            if gateway.subnets
                            else 0
                        ),
                        "provisioning_state": gateway.provisioning_state,
                        "tags": gateway.tags or {},
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