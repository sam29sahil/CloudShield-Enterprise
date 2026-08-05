"""
CloudShield Enterprise
Subfinder Tool
"""

from app.security.tools.common.base import BaseTool

from app.security.tools.dns.constants import SUBFINDER_DEFAULT


class SubfinderTool(BaseTool):
    """
    ProjectDiscovery Subfinder
    """

    name = "subfinder"

    default_arguments = SUBFINDER_DEFAULT
    timeout = 300

    def passive(self, target):

<<<<<<< HEAD
        return self.scan(target, ["-silent"])

    def recursive(self, target):

        return self.scan(target, ["-recursive"])

    def all_sources(self, target):

        return self.scan(target, ["-all"])
=======
        return self.scan(

            target,

            [

                "-silent"

            ]

        )

    def recursive(self, target):

        return self.scan(

            target,

            [

                "-recursive"

            ]

        )

    def all_sources(self, target):

        return self.scan(

            target,

            [

                "-all"

            ]

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "DNS",
            "description": "Passive Subdomain Enumeration",
        }
=======

            "name": self.name,

            "category": "DNS",

            "description": "Passive Subdomain Enumeration"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
