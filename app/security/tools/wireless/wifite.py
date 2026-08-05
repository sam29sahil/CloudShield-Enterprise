"""
CloudShield Enterprise
Wifite Tool
"""

from app.security.tools.common.base import BaseTool


class WifiteTool(BaseTool):
    """
    Wifite
    """

    name = "wifite"

    default_arguments = []

    def automatic(self):

<<<<<<< HEAD
        return self.scan("", [])

    def wep(self):

        return self.scan("", ["--wep"])

    def wpa(self):

        return self.scan("", ["--wpa"])

    def pmkid(self):

        return self.scan("", ["--pmkid"])
=======
        return self.scan(

            "",

            []

        )

    def wep(self):

        return self.scan(

            "",

            [

                "--wep"

            ]

        )

    def wpa(self):

        return self.scan(

            "",

            [

                "--wpa"

            ]

        )

    def pmkid(self):

        return self.scan(

            "",

            [

                "--pmkid"

            ]

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "Wireless",
            "description": "Automated Wireless Security Testing",
        }
=======

            "name": self.name,

            "category": "Wireless",

            "description": "Automated Wireless Security Testing"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
