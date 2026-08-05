"""
CloudShield Enterprise
Fierce Tool
"""

from app.security.tools.common.base import BaseTool


class FierceTool(BaseTool):
    """
    Fierce DNS Scanner
    """

    name = "fierce"

    default_arguments = []
    timeout = 300

    def scan_all(self, target):

<<<<<<< HEAD
        return self.scan(target, ["--domain"])

    def dns_servers(self, target):

        return self.scan(target, ["--dns-servers"])

    def range_scan(self, target):

        return self.scan(target, ["--range"])
=======
        return self.scan(

            target,

            [

                "--domain"

            ]

        )

    def dns_servers(self, target):

        return self.scan(

            target,

            [

                "--dns-servers"

            ]

        )

    def range_scan(self, target):

        return self.scan(

            target,

            [

                "--range"

            ]

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "DNS",
            "description": "DNS Reconnaissance Tool",
        }
=======

            "name": self.name,

            "category": "DNS",

            "description": "DNS Reconnaissance Tool"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
