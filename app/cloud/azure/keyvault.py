"""
CloudShield Enterprise
Azure Key Vault
"""

try:

    from azure.mgmt.keyvault import KeyVaultManagementClient

except Exception:

    KeyVaultManagementClient = None


class AzureKeyVault:

    def __init__(self, client):

        self.client = client

    # ----------------------------------
    # List Key Vaults
    # ----------------------------------

    def list(self):

        if not self.client.is_connected():

            return []

        if KeyVaultManagementClient is None:

            return []

        try:

            vault_client = KeyVaultManagementClient(

                credential=self.client.get_credential(),

                subscription_id=self.client.subscription()

            )

            vaults = []

            for vault in vault_client.vaults.list():

                vaults.append(

                    {

                        "name": vault.name,

                        "location": vault.location,

                        "id": vault.id

                    }

                )

            return vaults

        except Exception:

            return []