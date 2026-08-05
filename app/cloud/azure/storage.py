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
<<<<<<< HEAD
                credential=self.client.get_credential(),
                subscription_id=self.client.subscription(),
=======

                credential=self.client.get_credential(),

                subscription_id=self.client.subscription()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )

            storage_accounts = []

            for account in storage_client.storage_accounts.list():

                storage_accounts.append(
<<<<<<< HEAD
                    {
                        "name": account.name,
                        "location": account.location,
                        "kind": account.kind,
                        "sku": account.sku.name if account.sku else "-",
                        "id": account.id,
                    }
=======

                    {

                        "name": account.name,

                        "location": account.location,

                        "kind": account.kind,

                        "sku": account.sku.name if account.sku else "-",

                        "id": account.id

                    }

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                )

            return storage_accounts

        except Exception:

<<<<<<< HEAD
            return []
=======
            return []
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
