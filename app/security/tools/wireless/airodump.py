"""
CloudShield Enterprise
Airodump-ng Tool
"""

from app.security.tools.common.base import BaseTool


class AirodumpTool(BaseTool):
    """
    Airodump-ng
    """

    name = "airodump-ng"

    default_arguments = []

    def monitor(self, interface):

        return self.scan(

            interface,

            []

        )

    def capture(self, interface, channel):

        return self.scan(

            interface,

            [

                "-c",

                str(channel)

            ]

        )

    def bssid(self, interface, bssid):

        return self.scan(

            interface,

            [

                "--bssid",

                bssid

            ]

        )

    def info(self):

        return {

            "name": self.name,

            "category": "Wireless",

            "description": "Wireless Packet Capture"

        }