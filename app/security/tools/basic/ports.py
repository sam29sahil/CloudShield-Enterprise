"""
CloudShield Enterprise
Port Scanner
"""

import socket

<<<<<<< HEAD
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP Alternate",
=======

COMMON_PORTS = {

    21: "FTP",

    22: "SSH",

    25: "SMTP",

    53: "DNS",

    80: "HTTP",

    110: "POP3",

    143: "IMAP",

    443: "HTTPS",

    3306: "MySQL",

    3389: "RDP",

    5432: "PostgreSQL",

    8080: "HTTP Alternate"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
}


class PortScanner:
    """
    Port Scanner
    """

    def __init__(self):

        self.name = "Port Scanner"

    def scan(self, target):

        return port_scan(target)


def port_scan(host):

    results = []

    socket.setdefaulttimeout(0.5)

    for port, service in COMMON_PORTS.items():

<<<<<<< HEAD
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:

            status = sock.connect_ex((host, port))

            if status == 0:

                results.append({"port": port, "service": service, "status": "Open"})
=======
        sock = socket.socket(

            socket.AF_INET,

            socket.SOCK_STREAM

        )

        try:

            status = sock.connect_ex(

                (host, port)

            )

            if status == 0:

                results.append({

                    "port": port,

                    "service": service,

                    "status": "Open"

                })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        except Exception:

            pass

        finally:

            sock.close()

<<<<<<< HEAD
    return {"success": True, "count": len(results), "ports": results}
=======
    return {

        "success": True,

        "count": len(results),

        "ports": results

    }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
