"""
CloudShield Enterprise
Azure Resource Groups
"""

<<<<<<< HEAD
from __future__ import annotations

import logging
from time import perf_counter

from app.cloud.azure.client import AzureClient

logger = logging.getLogger(__name__)


class AzureResourceGroups:
    """
    Azure Resource Group Inventory
    """

    def __init__(self, subscription_id: str):

        self.client = AzureClient(subscription_id)

    def list(self) -> dict:

        started = perf_counter()

        try:

            resource_client = self.client.resource_client()
=======
from azure.mgmt.resource.resources import ResourceManagementClient


class AzureResourceGroups:

    def __init__(self, client):

        self.client = client

    # ----------------------------------
    # List Resource Groups
    # ----------------------------------

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            resource_client = ResourceManagementClient(

                credential=self.client.get_credential(),

                subscription_id=self.client.subscription()

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            groups = []

            for group in resource_client.resource_groups.list():

<<<<<<< HEAD
                groups.append(
                    {
                        "name": group.name,
                        "location": group.location,
                        "tags": group.tags or {},
                        "managed_by": group.managed_by,
                        "id": group.id,
                        "type": group.type,
                    }
                )

            return {
                "success": True,
                "count": len(groups),
                "data": groups,
                "execution_time": round(perf_counter() - started, 3),
                "error": "",
            }

        except Exception as error:

            logger.exception(error)

            return {
                "success": False,
                "count": 0,
                "data": [],
                "execution_time": round(perf_counter() - started, 3),
                "error": str(error),
            }
=======
                resource_count = 0

                try:

                    resources = resource_client.resources.list_by_resource_group(
                        group.name
                    )

                    resource_count = sum(1 for _ in resources)

                except Exception:
                    pass

                tags = group.tags or {}

                groups.append(

                    {

                        "name": group.name,

                        "location": group.location,

                        "id": group.id,

                        "managed_by": group.managed_by,

                        "provisioning_state": group.properties.provisioning_state
                        if group.properties else "Unknown",

                        "tags": tags,

                        "resource_count": resource_count,

                        "risk": self.calculate_risk(
                            resource_count,
                            tags
                        )

                    }

                )

            return groups

        except Exception as e:

            print("Azure Resource Groups Error:", e)

            return []

    # ----------------------------------
    # Risk Calculation
    # ----------------------------------

    def calculate_risk(self, resource_count, tags):

        score = 0

        if resource_count == 0:
            score += 1

        if len(tags) == 0:
            score += 1

        if score == 0:
            return "Low"

        if score == 1:
            return "Medium"

        return "High"
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
