"""
CloudShield Enterprise
Azure Route Tables
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.network import NetworkManagementClient

logger = logging.getLogger(__name__)


class AzureRouteTables:
    """
    Azure Route Table Inventory
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

            logger.info("Collecting Azure Route Tables...")

            for table in self.network.route_tables.list_all():

                routes = []

                if table.routes:

                    for route in table.routes:

                        routes.append(
                            {
                                "name": route.name,
                                "address_prefix": route.address_prefix,
                                "next_hop_type": str(route.next_hop_type),
                                "next_hop_ip": route.next_hop_ip_address,
                            }
                        )

                inventory.append(
                    {
                        "id": table.id,
                        "name": table.name,
                        "resource_group": self.resource_group(table.id),
                        "location": table.location,
                        "routes": routes,
                        "route_count": len(routes),
                        "disable_bgp": table.disable_bgp_route_propagation,
                        "subnets": (
                            len(table.subnets)
                            if table.subnets
                            else 0
                        ),
                        "tags": table.tags or {},
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