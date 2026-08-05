"""
CloudShield Enterprise
HTTP Security Header Scanner
"""

import requests

<<<<<<< HEAD
from app.security.constants import HTTP_TIMEOUT, USER_AGENT
=======
from app.security.constants import (
    HTTP_TIMEOUT,
    USER_AGENT
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


class HeaderScanner:
    """
    HTTP Header Scanner
    """

    def __init__(self):

        self.name = "Header Scanner"

    def scan(self, target):

        return scan_headers(target)


def scan_headers(url):

    try:

        response = requests.get(
<<<<<<< HEAD
            url, timeout=HTTP_TIMEOUT, headers={"User-Agent": USER_AGENT}
=======

            url,

            timeout=HTTP_TIMEOUT,

            headers={

                "User-Agent": USER_AGENT

            }

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        headers = response.headers

        security_headers = {
<<<<<<< HEAD
            "Content-Security-Policy": headers.get("Content-Security-Policy"),
            "Strict-Transport-Security": headers.get("Strict-Transport-Security"),
            "X-Frame-Options": headers.get("X-Frame-Options"),
            "X-Content-Type-Options": headers.get("X-Content-Type-Options"),
            "Referrer-Policy": headers.get("Referrer-Policy"),
            "Permissions-Policy": headers.get("Permissions-Policy"),
        }

        missing = [key for key, value in security_headers.items() if value is None]

        return {
            "success": True,
            "headers": security_headers,
            "missing": missing,
            "score": max(100 - len(missing) * 15, 0),
=======

            "Content-Security-Policy": headers.get("Content-Security-Policy"),

            "Strict-Transport-Security": headers.get("Strict-Transport-Security"),

            "X-Frame-Options": headers.get("X-Frame-Options"),

            "X-Content-Type-Options": headers.get("X-Content-Type-Options"),

            "Referrer-Policy": headers.get("Referrer-Policy"),

            "Permissions-Policy": headers.get("Permissions-Policy")

        }

        missing = [

            key

            for key, value in security_headers.items()

            if value is None

        ]

        return {

            "success": True,

            "headers": security_headers,

            "missing": missing,

            "score": max(

                100 - len(missing) * 15,

                0

            )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    except Exception as e:

<<<<<<< HEAD
        return {"success": False, "error": str(e)}

    # ----------------------------------
    # Compatibility
    #     ----------------------------------
=======
        return {

            "success": False,

            "error": str(e)

        }

    # ----------------------------------
    # Compatibility
#     ----------------------------------
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def header_scan(response_headers):

        found = []

        missing = []

        security_headers = [
<<<<<<< HEAD
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Referrer-Policy",
            "Permissions-Policy",
=======

            "Content-Security-Policy",

            "Strict-Transport-Security",
    
            "X-Frame-Options",

            "X-Content-Type-Options",

            "Referrer-Policy",

            "Permissions-Policy"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        ]

        for header in security_headers:

            if header in response_headers:

                found.append(header)

            else:

                missing.append(header)

        return {
<<<<<<< HEAD
            "success": True,
            "headers": dict(response_headers),
            "found": found,
            "missing": missing,
            "score": max(100 - len(missing) * 15, 0),
        }
=======

            "success": True,

            "headers": dict(response_headers),

            "found": found,

            "missing": missing,

            "score": max(100 - len(missing) * 15, 0)

        }   
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
