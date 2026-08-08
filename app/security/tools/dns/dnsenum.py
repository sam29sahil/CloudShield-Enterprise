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

    def info(self):

        return {

            "name": self.name,

            "category": "DNS",

            "description": "DNS Enumeration Tool"

        }