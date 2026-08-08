"""
CloudShield Enterprise
Azure SQL Database
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.sql import SqlManagementClient

logger = logging.getLogger(__name__)


class AzureSQL:

    def __init__(self, client):

        self.client = client

        self.sql = SqlManagementClient(
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

            logger.info("Collecting Azure SQL Databases...")

            for server in self.sql.servers.list():

                resource_group = self.resource_group(server.id)

                for database in self.sql.databases.list_by_server(
                    resource_group,
                    server.name,
                ):

                    inventory.append(
                        {
                            "server": server.name,
                            "name": database.name,
                            "resource_group": resource_group,
                            "location": server.location,
                            "status": database.status,
                            "edition": database.sku.name if database.sku else "-",
                            "max_size_gb": round(
                                database.max_size_bytes / (1024 ** 3),
                                2
                            ) if database.max_size_bytes else 0,
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