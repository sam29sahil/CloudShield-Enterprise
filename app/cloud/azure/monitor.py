"""
CloudShield Enterprise
Azure Monitor
"""

from azure.mgmt.monitor import MonitorManagementClient


class AzureMonitor:

    def __init__(self, client):

        self.client = client

    # ----------------------------------
    # Monitor Overview
    # ----------------------------------

    def overview(self):

        if not self.client.is_connected():

<<<<<<< HEAD
            return {"connected": False, "alerts": 0, "diagnostic_settings": 0}
=======
            return {

                "connected": False,

                "alerts": 0,

                "diagnostic_settings": 0

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        try:

            monitor = MonitorManagementClient(
<<<<<<< HEAD
                credential=self.client.get_credential(),
                subscription_id=self.client.subscription(),
            )

            return {"connected": True, "alerts": 0, "diagnostic_settings": 0}

        except Exception:

            return {"connected": False, "alerts": 0, "diagnostic_settings": 0}
=======

                credential=self.client.get_credential(),

                subscription_id=self.client.subscription()

            )

            return {

                "connected": True,

                "alerts": 0,

                "diagnostic_settings": 0

            }

        except Exception:

            return {

                "connected": False,

                "alerts": 0,

                "diagnostic_settings": 0

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
