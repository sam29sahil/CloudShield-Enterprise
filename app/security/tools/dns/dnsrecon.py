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

        return self.scan(target, ["-t", "std"])

    def zone_transfer(self, target):

        return self.scan(target, ["-t", "axfr"])

    def brute_force(self, target):

        return self.scan(target, ["-t", "brt"])

    def reverse_lookup(self, target):

        return self.scan(target, ["-t", "rvl"])

    def info(self):

        return {
            "name": self.name,
            "category": "DNS",
            "description": "DNS Enumeration and Zone Transfer Testing",
        }
