"""
CloudShield Enterprise
<<<<<<< HEAD
Azure Identity Service
"""

from __future__ import annotations

import logging

from azure.mgmt.resource import SubscriptionClient

from app.cloud.azure.client import AzureClient

logger = logging.getLogger(__name__)


class AzureIdentity:
    """
    Azure Identity & Subscription Information
    """

    def __init__(self, subscription_id: str):

        self.client = AzureClient(subscription_id)

        self.subscription_id = subscription_id

    def subscription(self) -> dict:
        """
        Return Azure subscription information.
        """

        try:

            credential = self.client.credential

            subscription_client = SubscriptionClient(credential)

            for subscription in subscription_client.subscriptions.list():

                if subscription.subscription_id == self.subscription_id:

                    return {
                        "connected": True,
                        "subscription_name": subscription.display_name,
                        "subscription_id": subscription.subscription_id,
                        "tenant_id": subscription.tenant_id,
                        "state": subscription.state,
                    }

            return {"connected": False, "error": "Subscription not found."}

        except Exception as error:

            logger.exception(error)

            return {"connected": False, "error": str(error)}
=======
Azure Identity
"""


class AzureIdentity:

    def __init__(self, client):

        self.client = client

    # ----------------------------------
    # Identity Information
    # ----------------------------------

    def information(self):

        if not self.client.is_connected():

            return {

                "connected": False,

                "tenant": "-",

                "subscription": "-"

            }

        try:

            return {

                "connected": True,

                "tenant": self.client.subscription(),

                "subscription": self.client.subscription()

            }

        except Exception:

            return {

                "connected": False,

                "tenant": "-",

                "subscription": "-"

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
