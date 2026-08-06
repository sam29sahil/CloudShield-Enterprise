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

    def info(self):

        return {

            "name": self.name,

            "category": "Wireless",

            "description": "WEP/WPA Password Recovery"

        }