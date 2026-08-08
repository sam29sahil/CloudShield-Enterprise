"""
CloudShield Enterprise
Azure Storage Tables
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.data.tables import TableServiceClient

logger = logging.getLogger(__name__)


class AzureTables:

    def __init__(self, client):

        self.client = client

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

            storage_client = self.client.storage_client()

            for account in storage_client.storage_accounts.list():

                resource_group = self.resource_group(account.id)

                keys = storage_client.storage_accounts.list_keys(
                    resource_group,
                    account.name,
                )

                if not keys.keys:
                    continue

                connection_string = (
                    "DefaultEndpointsProtocol=https;"
                    f"AccountName={account.name};"
                    f"AccountKey={keys.keys[0].value};"
                    "EndpointSuffix=core.windows.net"
                )

                table_service = TableServiceClient.from_connection_string(
                    connection_string
                )

                for table in table_service.list_tables():

                    inventory.append(
                        {
                            "storage_account": account.name,
                            "name": table.name,
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