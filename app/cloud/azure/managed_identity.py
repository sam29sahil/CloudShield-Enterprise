"""
CloudShield Enterprise
Azure Managed Identity
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.msi import ManagedServiceIdentityClient

logger = logging.getLogger(__name__)


class AzureManagedIdentity:

    def __init__(self, client):

        self.client = client

        self.identity = ManagedServiceIdentityClient(
            credential=self.client.get_credential(),
            subscription_id=self.client.subscription(),
        )

    @staticmethod
    def resource_group(resource_id):

        try:
            return resource_id.split("/")[4]
        except (AttributeError, IndexError):
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

            logger.info(
                "Collecting Azure User Assigned Managed Identities..."
            )

            identities = (
                self.identity.user_assigned_identities
                .list_by_subscription()
            )

            for identity in identities:

                inventory.append(
                    {
                        "name": identity.name,
                        "resource_group": self.resource_group(
                            identity.id
                        ),
                        "location": identity.location,
                        "client_id": identity.client_id,
                        "principal_id": identity.principal_id,
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

            logger.exception(
                "Azure Managed Identity error: %s",
                error,
            )

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