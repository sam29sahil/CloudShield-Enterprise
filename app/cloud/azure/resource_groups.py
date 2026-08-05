"""
CloudShield Enterprise
Azure Resource Groups
"""

from __future__ import annotations

import logging
from time import perf_counter

from app.cloud.azure.client import AzureClient

logger = logging.getLogger(__name__)


class AzureResourceGroups:
    """
    Azure Resource Group Inventory
    """

    def __init__(self, subscription_id: str):

        self.client = AzureClient(subscription_id)

    def list(self) -> dict:

        started = perf_counter()

        try:

            resource_client = self.client.resource_client()

            groups = []

            for group in resource_client.resource_groups.list():

                groups.append(
                    {
                        "name": group.name,
                        "location": group.location,
                        "tags": group.tags or {},
                        "managed_by": group.managed_by,
                        "id": group.id,
                        "type": group.type,
                    }
                )

            return {
                "success": True,
                "count": len(groups),
                "data": groups,
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
