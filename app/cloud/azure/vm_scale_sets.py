"""
CloudShield Enterprise
Azure VM Scale Sets
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.compute import ComputeManagementClient

logger = logging.getLogger(__name__)


class AzureVMScaleSets:

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

            logger.info("Collecting Azure VM Scale Sets...")

            for vmss in self.compute.virtual_machine_scale_sets.list_all():

                inventory.append(
                    {
                        "id": vmss.id,
                        "name": vmss.name,
                        "resource_group": self.resource_group(vmss.id),
                        "location": vmss.location,
                        "sku": vmss.sku.name if vmss.sku else "-",
                        "capacity": vmss.sku.capacity if vmss.sku else 0,
                        "tier": vmss.sku.tier if vmss.sku else "-",
                        "upgrade_policy": (
                            vmss.upgrade_policy.mode
                            if vmss.upgrade_policy
                            else "-"
                        ),
                        "orchestration_mode": getattr(
                            vmss,
                            "orchestration_mode",
                            "-"
                        ),
                        "provisioning_state": vmss.provisioning_state,
                        "tags": vmss.tags or {},
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