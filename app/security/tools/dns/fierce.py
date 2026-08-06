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

        return self.scan(target, ["--domain"])

    def dns_servers(self, target):

        return self.scan(target, ["--dns-servers"])

    def range_scan(self, target):

        return self.scan(target, ["--range"])

    def info(self):

        return {
            "name": self.name,
            "category": "DNS",
            "description": "DNS Reconnaissance Tool",
        }
