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

    # -------------------------------------------------
    # Connection
    # -------------------------------------------------

    def is_connected(self):

        return self.connected

    # -------------------------------------------------
    # Credential
    # -------------------------------------------------

    def get_credential(self):

        return self.credential

    # -------------------------------------------------
    # Subscription
    # -------------------------------------------------

    def subscription(self):

        return AzureConfig.SUBSCRIPTION_ID

    # -------------------------------------------------
    # Metadata
    # -------------------------------------------------

    def subscription_id(self):

        return AzureConfig.SUBSCRIPTION_ID

    def tenant_id(self):

        return AzureConfig.TENANT_ID

    def client_id(self):

        return AzureConfig.CLIENT_ID

    def subscription_name(self):
        """
        Placeholder until Azure SDK
        fetches the real subscription name.
        """

        return "Azure Subscription"

    def region(self):
        """
        Default region.
        Can later be fetched dynamically.
        """

        return "Central India"

    # -------------------------------------------------
    # Dashboard Info
    # -------------------------------------------------

    def info(self):

        return {

            "connected": self.connected,

            "subscription_id": self.subscription_id(),

            "subscription_name": self.subscription_name(),

            "tenant_id": self.tenant_id(),

            "client_id": self.client_id(),

            "region": self.region()

        }