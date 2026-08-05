"""
CloudShield Enterprise
DNSEnum Tool
"""

from app.security.tools.common.base import BaseTool

from app.security.tools.dns.constants import DNSENUM_DEFAULT


class DNSEnumTool(BaseTool):
    """
    DNSEnum
    """

    name = "dnsenum"

    default_arguments = DNSENUM_DEFAULT

    timeout = 300

    def scan_all(self, target):

<<<<<<< HEAD
        return self.scan(target, [])

    def zone_transfer(self, target):

        return self.scan(target, ["--noreverse"])

    def reverse_lookup(self, target):

        return self.scan(target, ["--reverse"])

    def brute_force(self, target):

        return self.scan(target, ["--enum"])
=======
        return self.scan(

            target,

            []

        )

    def zone_transfer(self, target):

        return self.scan(

            target,

            [

                "--noreverse"

            ]

        )

    def reverse_lookup(self, target):

        return self.scan(

            target,

            [

                "--reverse"

            ]

        )

    def brute_force(self, target):

        return self.scan(

            target,

            [

                "--enum"

            ]

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "DNS",
            "description": "DNS Enumeration Tool",
        }
=======

            "name": self.name,

            "category": "DNS",

            "description": "DNS Enumeration Tool"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
