"""
CloudShield Enterprise
Azure Managed Disks
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.compute import ComputeManagementClient

logger = logging.getLogger(__name__)


class AzureManagedDisks:

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

            logger.info("Collecting Azure Managed Disks...")

            for disk in self.compute.disks.list():

                inventory.append(
                    {
                        "id": disk.id,
                        "name": disk.name,
                        "resource_group": self.resource_group(disk.id),
                        "location": disk.location,
                        "size_gb": disk.disk_size_gb,
                        "sku": disk.sku.name if disk.sku else "-",
                        "os_type": disk.os_type or "-",
                        "state": disk.disk_state,
                        "provisioning_state": disk.provisioning_state,
                        "tags": disk.tags or {},
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