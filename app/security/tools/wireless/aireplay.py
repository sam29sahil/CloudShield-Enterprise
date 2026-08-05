"""
CloudShield Enterprise
Aireplay-ng Tool
"""

from app.security.tools.common.base import BaseTool


class AireplayTool(BaseTool):
    """
    Aireplay-ng
    """

    name = "aireplay-ng"

    default_arguments = []

    def deauth(self, interface, bssid):

        return self.scan(interface, ["--deauth", "10", "-a", bssid])

    def fakeauth(self, interface, bssid):

        return self.scan(interface, ["--fakeauth", "5", "-a", bssid])

    def info(self):

        return {
            "name": self.name,
            "category": "Wireless",
            "description": "Wireless Packet Injection",
        }
