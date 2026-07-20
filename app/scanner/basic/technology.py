"""
CloudShield Enterprise
Technology Detection
"""

from app.scanner.constants import (
    SERVER_SIGNATURES,
    FRAMEWORK_SIGNATURES,
    HTML_SIGNATURES
)


def detect_technology(headers, html):
    """
    Detect web technologies.
    """

    technologies = []

    html = html.lower()

    # --------------------------
    # Server Detection
    # --------------------------

    server = headers.get(
        "Server",
        ""
    ).lower()

    for key, value in SERVER_SIGNATURES.items():

        if key in server:

            technologies.append(value)

    # --------------------------
    # Framework Detection
    # --------------------------

    powered = headers.get(
        "X-Powered-By",
        ""
    ).lower()

    for key, value in FRAMEWORK_SIGNATURES.items():

        if key in powered:

            technologies.append(value)

    # --------------------------
    # HTML Detection
    # --------------------------

    for key, value in HTML_SIGNATURES.items():

        if key in html:

            technologies.append(value)

    return {

        "success": True,

        "count": len(
            set(technologies)
        ),

        "technologies": sorted(
            list(set(technologies))
        )

    }