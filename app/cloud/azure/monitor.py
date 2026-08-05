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

            return {"connected": False, "alerts": 0, "diagnostic_settings": 0}

        try:

            monitor = MonitorManagementClient(
                credential=self.client.get_credential(),
                subscription_id=self.client.subscription(),
            )

            return {"connected": True, "alerts": 0, "diagnostic_settings": 0}

        except Exception:

            return {"connected": False, "alerts": 0, "diagnostic_settings": 0}
