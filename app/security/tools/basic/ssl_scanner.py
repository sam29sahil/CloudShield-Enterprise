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

<<<<<<< HEAD
            with context.wrap_socket(sock, server_hostname=host) as secure:
=======
            with context.wrap_socket(
                sock,
                server_hostname=host
            ) as secure:
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

                cert = secure.getpeercert()

                return {
<<<<<<< HEAD
                    "success": True,
                    "issuer": cert.get("issuer"),
                    "subject": cert.get("subject"),
                    "version": cert.get("version"),
                    "serial": cert.get("serialNumber"),
                    "expires": cert.get("notAfter"),
=======

                    "success": True,

                    "issuer": cert.get("issuer"),

                    "subject": cert.get("subject"),

                    "version": cert.get("version"),

                    "serial": cert.get("serialNumber"),

                    "expires": cert.get("notAfter")

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                }

    except Exception as e:

<<<<<<< HEAD
        return {"success": False, "error": str(e)}
=======
        return {

            "success": False,

            "error": str(e)

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# Backward compatibility
def scan_ssl(host):
<<<<<<< HEAD
    return get_ssl_info(host)
=======
    return get_ssl_info(host)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
