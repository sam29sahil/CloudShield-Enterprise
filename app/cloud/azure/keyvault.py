"""
CloudShield Enterprise
Azure Key Vault Inventory
"""

from __future__ import annotations

import logging
from time import perf_counter

try:

    from azure.mgmt.keyvault import KeyVaultManagementClient

except Exception:

    KeyVaultManagementClient = None


logger = logging.getLogger(__name__)


class AzureKeyVault:
    """
    Azure Key Vault Inventory Service
    """

    def __init__(self, client):

        self.client = client

        self.vault_client = None

        if KeyVaultManagementClient:

            self.vault_client = KeyVaultManagementClient(
                credential=self.client.get_credential(),
                subscription_id=self.client.subscription(),
            )

    # --------------------------------------------------
    # Helpers
    # --------------------------------------------------

    @staticmethod
    def resource_group(resource_id):

        try:

            return resource_id.split("/")[4]

        except Exception:

            return "-"

    # --------------------------------------------------
    # Inventory
    # --------------------------------------------------

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

        if self.vault_client is None:

            return {
                "success": False,
                "count": 0,
                "data": [],
                "execution_time": 0,
                "error": "Azure Key Vault SDK not installed.",
            }

        inventory = []

        try:

            logger.info("Collecting Azure Key Vault inventory...")

            for vault in self.vault_client.vaults.list():
                # --------------------------------------------------
                # Access Policies
                # --------------------------------------------------

                access_policies = []

                try:

                    if vault.properties.access_policies:

                        for policy in vault.properties.access_policies:

                            access_policies.append(
                                {
                                    "tenant_id": str(policy.tenant_id),
                                    "object_id": str(policy.object_id),
                                    "keys": len(policy.permissions.keys or []),
                                    "secrets": len(policy.permissions.secrets or []),
                                    "certificates": len(
                                        policy.permissions.certificates or []
                                    ),
                                    "storage": len(policy.permissions.storage or []),
                                }
                            )

                except Exception:

                    pass

                # --------------------------------------------------
                # Private Endpoints
                # --------------------------------------------------

                private_endpoints = 0

                try:

                    if hasattr(vault.properties, "private_endpoint_connections"):

                        private_endpoints = len(
                            vault.properties.private_endpoint_connections or []
                        )

                except Exception:

                    pass

                # --------------------------------------------------
                # Network ACLs
                # --------------------------------------------------

                network_acls = {
                    "default_action": None,
                    "bypass": None,
                    "ip_rules": [],
                    "virtual_network_rules": [],
                }

                try:

                    if vault.properties.network_acls:

                        acl = vault.properties.network_acls

                        network_acls = {
                            "default_action": acl.default_action,
                            "bypass": acl.bypass,
                            "ip_rules": [rule.value for rule in acl.ip_rules or []],
                            "virtual_network_rules": [
                                rule.id for rule in acl.virtual_network_rules or []
                            ],
                        }

                except Exception:

                    pass

                # --------------------------------------------------
                # Inventory
                # --------------------------------------------------

                inventory.append(
                    {
                        "id": vault.id,
                        "name": vault.name,
                        "resource_group": self.resource_group(vault.id),
                        "location": vault.location,
                        "tenant_id": str(vault.properties.tenant_id),
                        "sku": (
                            vault.properties.sku.name if vault.properties.sku else "-"
                        ),
                        "soft_delete": getattr(
                            vault.properties, "enable_soft_delete", False
                        ),
                        "purge_protection": getattr(
                            vault.properties, "enable_purge_protection", False
                        ),
                        "enabled_for_deployment": vault.properties.enabled_for_deployment,
                        "enabled_for_disk_encryption": vault.properties.enabled_for_disk_encryption,
                        "enabled_for_template_deployment": vault.properties.enabled_for_template_deployment,
                        "public_network_access": getattr(
                            vault.properties, "public_network_access", "Unknown"
                        ),
                        "rbac_authorization": getattr(
                            vault.properties, "enable_rbac_authorization", False
                        ),
                        "private_endpoints": private_endpoints,
                        "access_policies": access_policies,
                        "network_acls": network_acls,
                        "tags": vault.tags or {},
                    }
                )
            logger.info("Collected %s Azure Key Vault(s).", len(inventory))

            return {
                "success": True,
                "count": len(inventory),
                "data": inventory,
                "execution_time": round(perf_counter() - started, 3),
                "error": "",
            }

        except Exception as error:

            logger.exception("Azure Key Vault inventory failed: %s", error)

            return {
                "success": False,
                "count": 0,
                "data": [],
                "execution_time": round(perf_counter() - started, 3),
                "error": str(error),
            }
