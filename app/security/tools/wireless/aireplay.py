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

<<<<<<< HEAD
        return self.scan(interface, ["--deauth", "10", "-a", bssid])

    def fakeauth(self, interface, bssid):

        return self.scan(interface, ["--fakeauth", "5", "-a", bssid])
=======
        return self.scan(

            interface,

            [

                "--deauth",

                "10",

                "-a",

                bssid

            ]

        )

    def fakeauth(self, interface, bssid):

        return self.scan(

            interface,

            [

                "--fakeauth",

                "5",

                "-a",

                bssid

            ]

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "Wireless",
            "description": "Wireless Packet Injection",
        }
=======

            "name": self.name,

            "category": "Wireless",

            "description": "Wireless Packet Injection"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
