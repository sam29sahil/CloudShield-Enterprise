"""
CloudShield Enterprise
Azure Blob Containers
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.storage.blob import BlobServiceClient

logger = logging.getLogger(__name__)


class AzureBlobContainers:

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

            accounts = storage_client.storage_accounts.list()

            for account in accounts:

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

                blob_service = BlobServiceClient.from_connection_string(
                    connection_string
                )

                for container in blob_service.list_containers():

                    inventory.append(
                        {
                            "storage_account": account.name,
                            "name": container.name,
                            "public_access": container.public_access or "Private",
                            "has_immutability_policy": getattr(
                                container,
                                "has_immutability_policy",
                                False,
                            ),
                            "has_legal_hold": getattr(
                                container,
                                "has_legal_hold",
                                False,
                            ),
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