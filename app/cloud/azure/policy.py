"""
CloudShield Enterprise
Azure Policy Service
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.resource.policy import PolicyClient

logger = logging.getLogger(__name__)


class AzurePolicy:

    def __init__(self, client):

        self.client = client

        self.policy = PolicyClient(
            credential=self.client.get_credential(),
            subscription_id=self.client.subscription(),
        )

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

            logger.info("Collecting Azure Policy Definitions...")

            for definition in self.policy.policy_definitions.list():

                metadata = definition.metadata or {}

                inventory.append(
                    {
                        "id": definition.id,
                        "name": definition.name,
                        "display_name": definition.display_name,
                        "policy_type": definition.policy_type,
                        "mode": definition.mode or "-",
                        "category": metadata.get("category", "-"),
                    }
                )

            return {
                "success": True,
                "count": len(inventory),
                "data": inventory,
                "execution_time": round(
                    perf_counter() - started,
                    3,
                ),
                "error": "",
            }

        except Exception as error:

            logger.exception(error)

            return {
                "success": False,
                "count": 0,
                "data": [],
                "execution_time": round(
                    perf_counter() - started,
                    3,
                ),
                "error": str(error),
            }