"""
CloudShield Enterprise
Azure Defender
"""


class AzureDefender:

    def __init__(self, client):

        self.client = client

    # ----------------------------------
    # Security Overview
    # ----------------------------------

    def overview(self):

        if not self.client.is_connected():

            return {

                "connected": False,

                "recommendations": 0,

                "alerts": 0

            }

        try:

            return {

                "connected": True,

                "recommendations": 0,

                "alerts": 0

            }

        except Exception:

            return {

                "connected": False,

                "recommendations": 0,

                "alerts": 0

            }