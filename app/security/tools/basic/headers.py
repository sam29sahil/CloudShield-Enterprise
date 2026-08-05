"""
CloudShield Enterprise
HTTP Security Header Scanner
"""

import requests

from app.security.constants import HTTP_TIMEOUT, USER_AGENT


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
            url, timeout=HTTP_TIMEOUT, headers={"User-Agent": USER_AGENT}
        )

        headers = response.headers

        security_headers = {
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
        }

    except Exception as e:

        return {"success": False, "error": str(e)}

    # ----------------------------------
    # Compatibility
    #     ----------------------------------

    def header_scan(response_headers):

        found = []

        missing = []

        security_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Referrer-Policy",
            "Permissions-Policy",
        ]

        for header in security_headers:

            if header in response_headers:

                found.append(header)

            else:

                missing.append(header)

        return {
            "success": True,
            "headers": dict(response_headers),
            "found": found,
            "missing": missing,
            "score": max(100 - len(missing) * 15, 0),
        }
