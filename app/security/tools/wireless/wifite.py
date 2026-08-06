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

        return self.scan("", [])

    def wep(self):

        return self.scan("", ["--wep"])

    def wpa(self):

        return self.scan("", ["--wpa"])

    def pmkid(self):

        return self.scan("", ["--pmkid"])

    def info(self):

        return {
            "name": self.name,
            "category": "Wireless",
            "description": "Automated Wireless Security Testing",
        }
