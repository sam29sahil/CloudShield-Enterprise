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

    def info(self):

        return {

            "name": self.name,

            "category": "DNS",

            "description": "OWASP Amass Subdomain Enumeration"

        }