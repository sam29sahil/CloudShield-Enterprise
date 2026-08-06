"""
CloudShield Enterprise
SSL Scanner
"""

import ssl
import socket


class SSLScanner:

    def __init__(self):
        self.name = "SSL Scanner"

    def scan(self, host):
        return get_ssl_info(host)


def get_ssl_info(host):

    try:

        context = ssl.create_default_context()

        with socket.create_connection((host, 443), timeout=5) as sock:

            with context.wrap_socket(sock, server_hostname=host) as secure:

                cert = secure.getpeercert()

                return {
                    "success": True,
                    "issuer": cert.get("issuer"),
                    "subject": cert.get("subject"),
                    "version": cert.get("version"),
                    "serial": cert.get("serialNumber"),
                    "expires": cert.get("notAfter"),
                }

    except Exception as e:

        return {"success": False, "error": str(e)}


# Backward compatibility
def scan_ssl(host):
    return get_ssl_info(host)
