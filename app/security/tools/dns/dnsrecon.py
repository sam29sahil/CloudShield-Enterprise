"""
CloudShield Enterprise
DNSRecon Tool
"""

from app.security.tools.common.base import BaseTool

from app.security.tools.dns.constants import DNSRECON_DEFAULT


class DNSReconTool(BaseTool):
    """
    DNSRecon
    """

    name = "dnsrecon"

    default_arguments = DNSRECON_DEFAULT
    timeout = 300

    def standard(self, target):

<<<<<<< HEAD
        return self.scan(target, ["-t", "std"])

    def zone_transfer(self, target):

        return self.scan(target, ["-t", "axfr"])

    def brute_force(self, target):

        return self.scan(target, ["-t", "brt"])

    def reverse_lookup(self, target):

        return self.scan(target, ["-t", "rvl"])
=======
        return self.scan(

            target,

            [

                "-t",

                "std"

            ]

        )

    def zone_transfer(self, target):

        return self.scan(

            target,

            [

                "-t",

                "axfr"

            ]

        )

    def brute_force(self, target):

        return self.scan(

            target,

            [

                "-t",

                "brt"

            ]

        )

    def reverse_lookup(self, target):

        return self.scan(

            target,

            [

                "-t",

                "rvl"

            ]

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "DNS",
            "description": "DNS Enumeration and Zone Transfer Testing",
        }
=======

            "name": self.name,

            "category": "DNS",

            "description": "DNS Enumeration and Zone Transfer Testing"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
