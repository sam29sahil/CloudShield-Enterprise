"""
CloudShield Enterprise
WHOIS Scanner
"""

import whois


class WhoisScanner:
    """
    WHOIS Scanner
    """

    def __init__(self):

        self.name = "WHOIS Scanner"

    def scan(self, target):

        return whois_scan(target)


def whois_scan(domain):
    """
    Retrieve WHOIS information.
    """

    try:

        data = whois.whois(domain)

        return {
<<<<<<< HEAD
            "success": True,
            "registrar": data.registrar,
            "creation_date": str(data.creation_date),
            "expiration_date": str(data.expiration_date),
            "updated_date": str(data.updated_date),
            "name_servers": data.name_servers,
            "status": data.status,
            "emails": data.emails,
=======

            "success": True,

            "registrar": data.registrar,

            "creation_date": str(
                data.creation_date
            ),

            "expiration_date": str(
                data.expiration_date
            ),

            "updated_date": str(
                data.updated_date
            ),

            "name_servers": data.name_servers,

            "status": data.status,

            "emails": data.emails

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
