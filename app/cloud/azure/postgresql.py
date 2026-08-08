"""
CloudShield Enterprise
Azure Database for PostgreSQL
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.rdbms.postgresql_flexibleservers import PostgreSQLManagementClient

logger = logging.getLogger(__name__)


class AzurePostgreSQL:

    def __init__(self, client):

        self.client = client

        self.postgresql = PostgreSQLManagementClient(
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

            logger.info("Collecting Azure PostgreSQL Flexible Servers...")

            for server in self.postgresql.servers.list():

                inventory.append(
                    {
                        "name": server.name,
                        "resource_group": self.resource_group(server.id),
                        "location": server.location,
                        "version": server.version,
                        "sku": server.sku.name if server.sku else "-",
                        "state": server.state,
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