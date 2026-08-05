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

                storage_accounts.append(
                    {
                        "name": account.name,
                        "location": account.location,
                        "kind": account.kind,
                        "sku": account.sku.name if account.sku else "-",
                        "id": account.id,
                    }
                )

            return storage_accounts

        except Exception:

            return []
