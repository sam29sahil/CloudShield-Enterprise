"""
CloudShield Enterprise
Azure Advisor
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.advisor import AdvisorManagementClient

logger = logging.getLogger(__name__)


class AzureAdvisor:

    def __init__(self, client):

        self.client = client

        self.advisor = AdvisorManagementClient(
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

            logger.info("Collecting Azure Advisor Recommendations...")

            for recommendation in self.advisor.recommendations.list():

                inventory.append(
                    {
                        "name": recommendation.short_description.problem,
                        "solution": recommendation.short_description.solution,
                        "category": recommendation.category,
                        "impact": recommendation.impact,
                        "resource": recommendation.resource_metadata.resource_id,
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