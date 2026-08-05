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

<<<<<<< HEAD
            return {"connected": False, "recommendations": 0, "alerts": 0}

        try:

            return {"connected": True, "recommendations": 0, "alerts": 0}

        except Exception:

            return {"connected": False, "recommendations": 0, "alerts": 0}
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
