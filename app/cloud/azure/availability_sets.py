"""
CloudShield Enterprise
Azure Availability Sets
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.compute import ComputeManagementClient

logger = logging.getLogger(__name__)


class AzureAvailabilitySets:

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

            logger.info("Collecting Azure Availability Sets...")

            for av in self.compute.availability_sets.list_by_subscription():

                inventory.append(
                    {
                        "id": av.id,
                        "name": av.name,
                        "resource_group": self.resource_group(av.id),
                        "location": av.location,
                        "fault_domains": av.platform_fault_domain_count,
                        "update_domains": av.platform_update_domain_count,
                        "managed": av.sku is not None,
                        "provisioning_state": av.provisioning_state,
                        "tags": av.tags or {},
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