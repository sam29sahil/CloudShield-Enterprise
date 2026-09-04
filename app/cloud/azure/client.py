"""
CloudShield Enterprise
Azure Client Manager
"""
from __future__ import annotations

import os
import logging
import subprocess
from typing import Any, Optional

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
from azure.identity import DefaultAzureCredential

from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient

logger = logging.getLogger(__name__)


AZURE_CONFIGURATION_ERROR = (
    "Azure credentials are not configured. Configure "
    "AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET and "
    "AZURE_SUBSCRIPTION_ID."
)


class AzureConfigurationError(ValueError):
    """Raised when an Azure operation is requested without configuration."""


class AzureClient:

    def __init__(self, subscription_id: Optional[str] = None):

        if subscription_id is None:
            subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")

        if not subscription_id:
            subscription_id = self._cli_subscription_id()

        self._subscription = subscription_id or ""
        self._credential = None

    @staticmethod
    def _cli_subscription_id() -> Optional[str]:
        try:
            result = subprocess.run(
                ["cmd", "/c", "az", "account", "show", "--query", "id", "-o", "tsv"],
                check=True,
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.stdout.strip() or None
        except (OSError, subprocess.SubprocessError):
            return None

    @property
    def configuration_error(self):
        if self._subscription:
            return None

        return AZURE_CONFIGURATION_ERROR

    def _require_configuration(self):
        if self.configuration_error:
            raise AzureConfigurationError(self.configuration_error)

    def _get_credential(self):
        if self._credential is None:
            self._credential = DefaultAzureCredential(
                exclude_interactive_browser_credential=True,
            )

        return self._credential

    # --------------------------------------------------
    # Helpers
    # --------------------------------------------------

    def subscription(self) -> str:

        return self._subscription

    def get_credential(self):

        return self._get_credential()

    def is_connected(self) -> bool:

        return self.connection_status()["connected"]

    @staticmethod
    def _error_status(error: Exception) -> tuple[str, str]:
        error_text = str(error).lower()

        if isinstance(error, ClientAuthenticationError):
            return "authentication", "Azure authentication failed."

        if (
            isinstance(error, HttpResponseError) and error.status_code == 403
        ) or "403" in error_text or "forbidden" in error_text:
            return "authorization", "Azure authorization failed."

        if "credential" in error_text or "authentication" in error_text:
            return "authentication", "Azure authentication failed."

        return "connection", "Azure connection failed."

    def connection_status(self) -> dict[str, Any]:
        if self.configuration_error:
            return {
                "connected": False,
                "status": "configuration",
                "error": "Azure credentials are not configured.",
            }

        try:
            client = self.resource_client()
            next(iter(client.resource_groups.list()), None)
            return {"connected": True, "status": "connected", "error": ""}
        except Exception as error:
            status, message = self._error_status(error)
            logger.warning("Azure connection check failed (%s).", status)
            return {"connected": False, "status": status, "error": message}

    # --------------------------------------------------
    # SDK Clients
    # --------------------------------------------------

    def resource_client(self):

        self._require_configuration()
        return ResourceManagementClient(self._get_credential(), self._subscription)

    def compute_client(self):

        self._require_configuration()
        return ComputeManagementClient(self._get_credential(), self._subscription)

    def network_client(self):

        self._require_configuration()
        return NetworkManagementClient(self._get_credential(), self._subscription)

    def storage_client(self):

        self._require_configuration()
        return StorageManagementClient(self._get_credential(), self._subscription)

    # --------------------------------------------------
    # Connection Test
    # --------------------------------------------------

    def test_connection(self) -> bool:
        return self.connection_status()["connected"]
