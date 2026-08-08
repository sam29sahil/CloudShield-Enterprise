"""
CloudShield Enterprise
Azure Images
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.compute import ComputeManagementClient

logger = logging.getLogger(__name__)


class AzureImages:

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

            logger.info("Collecting Azure Images...")

            for image in self.compute.images.list():

                inventory.append(
                    {
                        "id": image.id,
                        "name": image.name,
                        "resource_group": self.resource_group(image.id),
                        "location": image.location,
                        "os_type": image.storage_profile.os_disk.os_type if image.storage_profile and image.storage_profile.os_disk else "-",
                        "hyper_v_generation": getattr(image, "hyper_v_generation", "-"),
                        "provisioning_state": image.provisioning_state,
                        "tags": image.tags or {},
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