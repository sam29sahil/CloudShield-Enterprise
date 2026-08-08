"""
CloudShield Enterprise
DNS Scanner
"""

import socket


class DNSScanner:

    def __init__(self):

        self.name = "DNS Scanner"

    def scan(self, domain):

        return dns_scan(domain)


def dns_scan(domain):

    try:

        ip = socket.gethostbyname(domain)

        return {

            "success": True,

            "domain": domain,

            "ip": ip

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }