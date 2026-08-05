"""
CloudShield Enterprise
Aircrack-ng Tool
"""

from app.security.tools.common.base import BaseTool


class AircrackTool(BaseTool):
    """
    Aircrack-ng
    """

    name = "aircrack-ng"

    default_arguments = []

    def crack(self, capture_file):

<<<<<<< HEAD
        return self.scan(capture_file, [])

    def wordlist(self, capture_file, wordlist):

        return self.scan(capture_file, ["-w", wordlist])
=======
        return self.scan(

            capture_file,

            []

        )

    def wordlist(self, capture_file, wordlist):

        return self.scan(

            capture_file,

            [

                "-w",

                wordlist

            ]

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "Wireless",
            "description": "WEP/WPA Password Recovery",
        }
=======

            "name": self.name,

            "category": "Wireless",

            "description": "WEP/WPA Password Recovery"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
