"""
CloudShield Enterprise
Azure Log Analytics
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.loganalytics import LogAnalyticsManagementClient

logger = logging.getLogger(__name__)


class AzureLogAnalytics:

    def __init__(self, client):

        self.client = client

        self.logs = LogAnalyticsManagementClient(
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

            logger.info("Collecting Log Analytics Workspaces...")

            for workspace in self.logs.workspaces.list():

                inventory.append(
                    {
                        "name": workspace.name,
                        "resource_group": self.resource_group(workspace.id),
                        "location": workspace.location,
                        "sku": workspace.sku.name if workspace.sku else "-",
                        "retention": workspace.retention_in_days,
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