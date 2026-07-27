"""
CloudShield Enterprise
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