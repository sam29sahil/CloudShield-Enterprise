"""
CloudShield Enterprise
<<<<<<< HEAD
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
=======
Azure Client
"""

from azure.identity import ClientSecretCredential

from app.cloud.azure.config import AzureConfig


class AzureClient:
    """
    Azure Authentication Client
    """

    def __init__(self):

        self.connected = False
        self.credential = None

        if not AzureConfig.configured():
            return

        try:

            self.credential = ClientSecretCredential(

                tenant_id=AzureConfig.TENANT_ID,

                client_id=AzureConfig.CLIENT_ID,

                client_secret=AzureConfig.CLIENT_SECRET

            )

            self.connected = True

        except Exception:

            self.connected = False

            self.credential = None

    # -------------------------------------------------
    # Connection
    # -------------------------------------------------

    def is_connected(self):

        return self.connected

    # -------------------------------------------------
    # Credential
    # -------------------------------------------------

    def get_credential(self):

        return self.credential

    # -------------------------------------------------
    # Subscription
    # -------------------------------------------------

    def subscription(self):

        return AzureConfig.SUBSCRIPTION_ID

    # -------------------------------------------------
    # Metadata
    # -------------------------------------------------

    def subscription_id(self):

        return AzureConfig.SUBSCRIPTION_ID

    def tenant_id(self):

        return AzureConfig.TENANT_ID

    def client_id(self):

        return AzureConfig.CLIENT_ID

    def subscription_name(self):
        """
        Placeholder until Azure SDK
        fetches the real subscription name.
        """

        return "Azure Subscription"

    def region(self):
        """
        Default region.
        Can later be fetched dynamically.
        """

        return "Central India"

    # -------------------------------------------------
    # Dashboard Info
    # -------------------------------------------------

    def info(self):

        return {

            "connected": self.connected,

            "subscription_id": self.subscription_id(),

            "subscription_name": self.subscription_name(),

            "tenant_id": self.tenant_id(),

            "client_id": self.client_id(),

            "region": self.region()

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
