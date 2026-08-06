"""
CloudShield Enterprise
Azure Client Manager
"""

from __future__ import annotations

import logging

from azure.identity import DefaultAzureCredential

from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient

logger = logging.getLogger(__name__)


class AzureClient:

    def __init__(self, subscription_id: str):

        if not subscription_id:
            raise ValueError("Azure subscription ID is required.")

        self._subscription = subscription_id

        self._credential = DefaultAzureCredential(
            exclude_interactive_browser_credential=False
        )

    # --------------------------------------------------
    # Helpers
    # --------------------------------------------------

    def subscription(self) -> str:

        return self._subscription

    def get_credential(self):

        return self._credential

    def is_connected(self) -> bool:

        return self.test_connection()

    # --------------------------------------------------
    # SDK Clients
    # --------------------------------------------------

    def resource_client(self):

        return ResourceManagementClient(self._credential, self._subscription)

    def compute_client(self):

        return ComputeManagementClient(self._credential, self._subscription)

    def network_client(self):

        return NetworkManagementClient(self._credential, self._subscription)

    def storage_client(self):

        return StorageManagementClient(self._credential, self._subscription)

    # --------------------------------------------------
    # Connection Test
    # --------------------------------------------------

    def test_connection(self) -> bool:

        try:

            client = self.resource_client()

            next(client.resource_groups.list(), None)

            return True

        except Exception as error:

            logger.exception(error)

            return False
