"""
CloudShield Enterprise
Amass Tool
"""

from app.security.tools.common.base import BaseTool

from app.security.tools.dns.constants import AMASS_DEFAULT


class AmassTool(BaseTool):
    """
    OWASP Amass
    """

    name = "amass"

    default_arguments = AMASS_DEFAULT
    timeout = 300

    def passive(self, target):

<<<<<<< HEAD
        return self.scan(target, ["enum", "-passive"])

    def active(self, target):

        return self.scan(target, ["enum", "-active"])

    def intel(self, target):

        return self.scan(target, ["intel"])

    def enum(self, target):

        return self.scan(target, ["enum"])
=======
        return self.scan(

            target,

            [

                "enum",

                "-passive"

            ]

        )

    def active(self, target):

        return self.scan(

            target,

            [

                "enum",

                "-active"

            ]

        )

    def intel(self, target):

        return self.scan(

            target,

            [

                "intel"

            ]

        )

    def enum(self, target):

        return self.scan(

            target,

            [

                "enum"

            ]

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "DNS",
            "description": "OWASP Amass Subdomain Enumeration",
        }
=======

            "name": self.name,

            "category": "DNS",

            "description": "OWASP Amass Subdomain Enumeration"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
