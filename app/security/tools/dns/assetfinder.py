"""
CloudShield Enterprise
AssetFinder Tool
"""

from app.security.tools.common.base import BaseTool

from app.security.tools.dns.constants import ASSETFINDER_DEFAULT


class AssetFinderTool(BaseTool):
    """
    Assetfinder
    """

    name = "assetfinder"

    default_arguments = ASSETFINDER_DEFAULT
    timeout = 300

    def scan_all(self, target):

        return self.scan(

            target,

            [

                "--subs-only"

            ]

        )

    def info(self):

        return {

            "name": self.name,

            "category": "DNS",

            "description": "Assetfinder Subdomain Enumeration"

        }