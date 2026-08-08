"""
CloudShield Enterprise
Azure Public IP Inventory
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.network import NetworkManagementClient

logger = logging.getLogger(__name__)


class AzurePublicIPs:

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

            logger.info("Collecting Azure Public IPs...")

            for ip in self.network.public_ip_addresses.list_all():

                inventory.append(
                    {
                        "id": ip.id,
                        "name": ip.name,
                        "resource_group": self.resource_group(ip.id),
                        "location": ip.location,
                        "ip_address": ip.ip_address,
                        "version": str(ip.public_ip_address_version),
                        "allocation": str(ip.public_ip_allocation_method),
                        "sku": ip.sku.name if ip.sku else "-",
                        "dns": (
                            ip.dns_settings.fqdn
                            if ip.dns_settings
                            else "-"
                        ),
                        "idle_timeout": ip.idle_timeout_in_minutes,
                        "attached": ip.ip_configuration is not None,
                        "tags": ip.tags or {},
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