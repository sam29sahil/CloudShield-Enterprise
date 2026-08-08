"""
CloudShield Enterprise
Azure Firewall
"""

from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.network import NetworkManagementClient

logger = logging.getLogger(__name__)


class AzureFirewall:

    """
    Azure Firewall Inventory
    """

    def __init__(self, client):

        self.client = client

        self.network = NetworkManagementClient(
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

            logger.info("Collecting Azure Firewalls...")

            for firewall in self.network.azure_firewalls.list_all():

                inventory.append(
                    {
                        "id": firewall.id,
                        "name": firewall.name,
                        "resource_group": self.resource_group(firewall.id),
                        "location": firewall.location,
                        "sku": (
                            firewall.sku.name
                            if firewall.sku
                            else "-"
                        ),
                        "tier": (
                            firewall.sku.tier
                            if firewall.sku
                            else "-"
                        ),
                        "threat_intelligence": (
                            firewall.threat_intel_mode
                            if firewall.threat_intel_mode
                            else "-"
                        ),
                        "provisioning_state": firewall.provisioning_state,
                        "ip_configurations": (
                            len(firewall.ip_configurations)
                            if firewall.ip_configurations
                            else 0
                        ),
                        "application_rule_collections": (
                            len(firewall.application_rule_collections)
                            if firewall.application_rule_collections
                            else 0
                        ),
                        "network_rule_collections": (
                            len(firewall.network_rule_collections)
                            if firewall.network_rule_collections
                            else 0
                        ),
                        "nat_rule_collections": (
                            len(firewall.nat_rule_collections)
                            if firewall.nat_rule_collections
                            else 0
                        ),
                        "tags": firewall.tags or {},
                    }
                )

            return {
                "success": True,
                "count": len(inventory),
                "data": inventory,
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