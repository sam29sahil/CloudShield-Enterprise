"""
CloudShield Enterprise
Azure Private Endpoints
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.network import NetworkManagementClient

logger = logging.getLogger(__name__)


class AzurePrivateEndpoints:

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

            logger.info("Collecting Azure Private Endpoints...")

            for endpoint in self.network.private_endpoints.list_all():

                inventory.append(
                    {
                        "id": endpoint.id,
                        "name": endpoint.name,
                        "resource_group": self.resource_group(endpoint.id),
                        "location": endpoint.location,
                        "subnet": endpoint.subnet.id.split("/")[-1] if endpoint.subnet else "-",
                        "network_interfaces": len(endpoint.network_interfaces or []),
                        "private_connections": len(endpoint.private_link_service_connections or []),
                        "manual_connections": len(endpoint.manual_private_link_service_connections or []),
                        "provisioning_state": endpoint.provisioning_state,
                        "tags": endpoint.tags or {},
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