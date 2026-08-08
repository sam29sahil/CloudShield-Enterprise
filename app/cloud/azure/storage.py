"""
CloudShield Enterprise
Azure Storage Accounts
"""

from azure.mgmt.storage import StorageManagementClient


class AzureStorage:

    def __init__(self, client):

        self.client = client

    # ----------------------------------
    # List Storage Accounts
    # ----------------------------------

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            storage_client = StorageManagementClient(
                credential=self.client.get_credential(),
                subscription_id=self.client.subscription(),
            )

            storage_accounts = []

            for account in storage_client.storage_accounts.list():

                https_only = getattr(account, "enable_https_traffic_only", False)

                public_access = getattr(account, "allow_blob_public_access", None)

                minimum_tls = getattr(account, "minimum_tls_version", "-")

                encryption = False

                try:
                    encryption = bool(account.encryption.services.blob.enabled)
                except Exception:
                    pass

                storage_accounts.append(
                    {
                        "name": account.name,
                        "location": account.location,
                        "resource_group": account.id.split("/")[4],
                        "kind": str(account.kind),
                        "sku": account.sku.name if account.sku else "-",
                        "https_only": https_only,
                        "public_access": public_access,
                        "tls": minimum_tls,
                        "encryption": encryption,
                        "tags": account.tags or {},
                        "id": account.id,
                    }
                )

            return storage_accounts

        except Exception as e:

            print(e)

            return []
