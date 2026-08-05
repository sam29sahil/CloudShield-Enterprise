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

<<<<<<< HEAD
        return self.scan(target, ["--subs-only"])
=======
        return self.scan(

            target,

            [

                "--subs-only"

            ]

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "DNS",
            "description": "Assetfinder Subdomain Enumeration",
        }
=======

            "name": self.name,

            "category": "DNS",

            "description": "Assetfinder Subdomain Enumeration"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
