"""
CloudShield Enterprise
Azure VPN Gateway
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.network import NetworkManagementClient

logger = logging.getLogger(__name__)


class AzureVPNGateway:

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

            logger.info("Collecting Azure VPN Gateways...")

            for gateway in self.network.virtual_network_gateways.list_all():

                inventory.append(
                    {
                        "id": gateway.id,
                        "name": gateway.name,
                        "resource_group": self.resource_group(gateway.id),
                        "location": gateway.location,
                        "gateway_type": str(gateway.gateway_type),
                        "vpn_type": str(gateway.vpn_type),
                        "sku": gateway.sku.name if gateway.sku else "-",
                        "generation": getattr(gateway, "vpn_gateway_generation", "-"),
                        "enable_bgp": gateway.enable_bgp,
                        "active_active": gateway.active_active,
                        "connections": len(gateway.ip_configurations or []),
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