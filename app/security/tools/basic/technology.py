"""
CloudShield Enterprise
Technology Detection
"""

from app.security.constants import (
    SERVER_SIGNATURES,
    FRAMEWORK_SIGNATURES,
    HTML_SIGNATURES,
)


class TechnologyScanner:
    """
    Technology Scanner
    """

    def __init__(self):

        self.name = "Technology Scanner"

    def scan(self, headers, html):

        return detect_technology(headers, html)


def detect_technology(headers, html):
    """
    Detect web technologies.
    """

    technologies = []

    html = html.lower()

    server = headers.get("Server", "").lower()

    for key, value in SERVER_SIGNATURES.items():

        if key in server:

            technologies.append(value)

    powered = headers.get("X-Powered-By", "").lower()

    for key, value in FRAMEWORK_SIGNATURES.items():

        if key in powered:

            technologies.append(value)

    for key, value in HTML_SIGNATURES.items():

        if key in html:

            technologies.append(value)

    technologies = sorted(list(set(technologies)))

    return {"success": True, "count": len(technologies), "technologies": technologies}
