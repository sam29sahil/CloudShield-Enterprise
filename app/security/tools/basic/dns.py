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

<<<<<<< HEAD
        return {"success": True, "domain": domain, "ip": ip}

    except Exception as e:

        return {"success": False, "error": str(e)}
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
