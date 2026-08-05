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

<<<<<<< HEAD
        return self.scan(interface, [])

    def capture(self, interface, channel):

        return self.scan(interface, ["-c", str(channel)])

    def bssid(self, interface, bssid):

        return self.scan(interface, ["--bssid", bssid])
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "Wireless",
            "description": "Wireless Packet Capture",
        }
=======

            "name": self.name,

            "category": "Wireless",

            "description": "Wireless Packet Capture"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
