"""
CloudShield Enterprise
Azure Configuration
"""

import os


class AzureConfig:
    """
    Azure Configuration
    """

    TENANT_ID = os.getenv("AZURE_TENANT_ID")
    CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
    CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
    SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")

    @classmethod
    def configured(cls):
        """
        Returns True if Azure credentials exist.
        """

        return all(
            [
                cls.TENANT_ID,
                cls.CLIENT_ID,
                cls.CLIENT_SECRET,
                cls.SUBSCRIPTION_ID,
            ]
        )
