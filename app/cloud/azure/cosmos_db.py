"""
CloudShield Enterprise
Azure Cosmos DB
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.cosmosdb import CosmosDBManagementClient

logger = logging.getLogger(__name__)


class AzureCosmosDB:

    def __init__(self, client):

        self.client = client

        self.cosmos = CosmosDBManagementClient(
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

            logger.info("Collecting Azure Cosmos DB Accounts...")

            for account in self.cosmos.database_accounts.list():

                inventory.append(
                    {
                        "name": account.name,
                        "resource_group": self.resource_group(account.id),
                        "location": account.location,
                        "kind": account.kind,
                        "offer_type": account.database_account_offer_type,
                        "provisioning_state": account.provisioning_state,
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