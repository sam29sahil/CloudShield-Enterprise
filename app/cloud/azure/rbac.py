"""
CloudShield Enterprise
Azure RBAC
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.authorization import AuthorizationManagementClient

logger = logging.getLogger(__name__)


class AzureRBAC:

    def __init__(self, client):

        self.client = client

        self.authorization = AuthorizationManagementClient(
            credential=self.client.get_credential(),
            subscription_id=self.client.subscription(),
        )

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

            logger.info("Collecting Azure Role Definitions...")

            scope = f"/subscriptions/{self.client.subscription()}"

            for role in self.authorization.role_definitions.list(scope):

                inventory.append(
                    {
                        "id": role.id,
                        "name": role.role_name,
                        "description": role.description or "-",
                        "type": role.role_type,
                        "assignable_scopes": len(role.assignable_scopes),
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