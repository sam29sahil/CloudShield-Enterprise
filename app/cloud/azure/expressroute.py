"""
CloudShield Enterprise
Azure ExpressRoute
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.network import NetworkManagementClient

logger = logging.getLogger(__name__)


class AzureExpressRoute:

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

            logger.info("Collecting Azure ExpressRoute Circuits...")

            for circuit in self.network.express_route_circuits.list_all():

                inventory.append(
                    {
                        "id": circuit.id,
                        "name": circuit.name,
                        "resource_group": self.resource_group(circuit.id),
                        "location": circuit.location,
                        "sku": circuit.sku.name if circuit.sku else "-",
                        "tier": circuit.sku.tier if circuit.sku else "-",
                        "family": circuit.sku.family if circuit.sku else "-",
                        "bandwidth": (
                            circuit.service_provider_properties.bandwidth_in_mbps
                            if circuit.service_provider_properties
                            else "-"
                        ),
                        "provider": (
                            circuit.service_provider_properties.service_provider_name
                            if circuit.service_provider_properties
                            else "-"
                        ),
                        "peering_location": (
                            circuit.service_provider_properties.peering_location
                            if circuit.service_provider_properties
                            else "-"
                        ),
                        "provisioning_state": circuit.provisioning_state,
                        "tags": circuit.tags or {},
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
