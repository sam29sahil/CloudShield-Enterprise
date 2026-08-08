"""
CloudShield Enterprise
Azure Snapshots
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.compute import ComputeManagementClient

logger = logging.getLogger(__name__)


class AzureSnapshots:

    def __init__(self, client):

        self.client = client

        self.compute = ComputeManagementClient(
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

            logger.info("Collecting Azure Snapshots...")

            for snapshot in self.compute.snapshots.list():

                inventory.append(
                    {
                        "id": snapshot.id,
                        "name": snapshot.name,
                        "resource_group": self.resource_group(snapshot.id),
                        "location": snapshot.location,
                        "size_gb": snapshot.disk_size_gb,
                        "sku": snapshot.sku.name if snapshot.sku else "-",
                        "incremental": snapshot.incremental,
                        "provisioning_state": snapshot.provisioning_state,
                        "tags": snapshot.tags or {},
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