"""
CloudShield Enterprise
Azure Client
"""

from azure.identity import ClientSecretCredential

from app.cloud.azure.config import AzureConfig


class AzureClient:
    """
    Azure Authentication Client
    """

    def __init__(self):

        self.connected = False
        self.credential = None

        if not AzureConfig.configured():
            return

        try:

            self.credential = ClientSecretCredential(
                tenant_id=AzureConfig.TENANT_ID,
                client_id=AzureConfig.CLIENT_ID,
                client_secret=AzureConfig.CLIENT_SECRET
            )

            self.connected = True

        except Exception:

            self.connected = False

            self.credential = None

    # ---------------------------------------
    # Connection Status
    # ---------------------------------------

    def is_connected(self):

        return self.connected

    # ---------------------------------------
    # Credential
    # ---------------------------------------

    def get_credential(self):

        return self.credential

    # ---------------------------------------
    # Subscription
    # ---------------------------------------

    def subscription(self):

        return AzureConfig.SUBSCRIPTION_ID