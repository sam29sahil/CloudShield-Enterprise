import socket
import ssl
from datetime import datetime


def get_ssl_info(hostname):
    try:
        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:

                cert = ssock.getpeercert()

                issuer = dict(x[0] for x in cert["issuer"])

                issued_to = dict(x[0] for x in cert["subject"])

                expires = datetime.strptime(
                    cert["notAfter"],
                    "%b %d %H:%M:%S %Y %Z"
                )

                days_left = (expires - datetime.utcnow()).days

                return {
                    "issuer": issuer.get("organizationName", "Unknown"),
                    "issued_to": issued_to.get("commonName", "Unknown"),
                    "expires": expires.strftime("%d-%m-%Y"),
                    "days_left": days_left,
                    "valid": days_left > 0
                }

    except Exception as e:
        return {
            "error": str(e)
        }