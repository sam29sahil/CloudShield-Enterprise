"""
CloudShield Enterprise
Technology Detection
"""

from app.security.constants import (
<<<<<<< HEAD
    SERVER_SIGNATURES,
    FRAMEWORK_SIGNATURES,
    HTML_SIGNATURES,
=======

    SERVER_SIGNATURES,

    FRAMEWORK_SIGNATURES,

    HTML_SIGNATURES

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
)


class TechnologyScanner:
    """
    Technology Scanner
    """

    def __init__(self):

        self.name = "Technology Scanner"

    def scan(self, headers, html):

<<<<<<< HEAD
        return detect_technology(headers, html)
=======
        return detect_technology(

            headers,

            html

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


def detect_technology(headers, html):
    """
    Detect web technologies.
    """

    technologies = []

    html = html.lower()

<<<<<<< HEAD
    server = headers.get("Server", "").lower()
=======
    server = headers.get(

        "Server",

        ""

    ).lower()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    for key, value in SERVER_SIGNATURES.items():

        if key in server:

            technologies.append(value)

<<<<<<< HEAD
    powered = headers.get("X-Powered-By", "").lower()
=======
    powered = headers.get(

        "X-Powered-By",

        ""

    ).lower()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    for key, value in FRAMEWORK_SIGNATURES.items():

        if key in powered:

            technologies.append(value)

    for key, value in HTML_SIGNATURES.items():

        if key in html:

            technologies.append(value)

<<<<<<< HEAD
    technologies = sorted(list(set(technologies)))

    return {"success": True, "count": len(technologies), "technologies": technologies}
=======
    technologies = sorted(

        list(

            set(technologies)

        )

    )

    return {

        "success": True,

        "count": len(technologies),

        "technologies": technologies

    }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
