"""
CloudShield Enterprise
Azure Bastion
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.network import NetworkManagementClient

logger = logging.getLogger(__name__)


class AzureBastion:

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

            logger.info("Collecting Azure Bastion Hosts...")

            for bastion in self.network.bastion_hosts.list():

                inventory.append(
                    {
                        "id": bastion.id,
                        "name": bastion.name,
                        "resource_group": self.resource_group(bastion.id),
                        "location": bastion.location,
                        "sku": bastion.sku.name if bastion.sku else "-",
                        "scale_units": getattr(bastion, "scale_units", 1),
                        "ip_configurations": len(bastion.ip_configurations or []),
                        "dns_name": getattr(bastion, "dns_name", "-"),
                        "provisioning_state": bastion.provisioning_state,
                        "tags": bastion.tags or {},
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