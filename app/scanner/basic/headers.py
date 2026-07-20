"""
CloudShield Enterprise
Security Header Analyzer
"""

from app.scanner.constants import (
    SECURITY_HEADERS,
    OWASP_REFERENCE
)


def header_scan(response_headers):
    """
    Analyze HTTP security headers.
    """

    found = []
    missing = []
    analysis = []

    total_headers = len(SECURITY_HEADERS)

    for header, info in SECURITY_HEADERS.items():

        # Accept Report-Only CSP
        if (
            header == "Content-Security-Policy"
            and "Content-Security-Policy-Report-Only" in response_headers
        ):

            found.append(header)

            analysis.append({

                "header": header,

                "status": "Report Only",

                "severity": info["severity"],

                "description": info["description"],

                "recommendation":
                    "Enable full Content-Security-Policy.",

                "reference": OWASP_REFERENCE

            })

            continue

        if header in response_headers:

            found.append(header)

            analysis.append({

                "header": header,

                "status": "Present",

                "severity": "Info",

                "description": info["description"],

                "recommendation": "No action required.",

                "reference": OWASP_REFERENCE

            })

        else:

            missing.append(header)

            analysis.append({

                "header": header,

                "status": "Missing",

                "severity": info["severity"],

                "description": info["description"],

                "recommendation":
                    f"Configure {header}.",

                "reference": OWASP_REFERENCE

            })

    score = round(

        (len(found) / total_headers) * 100

    )

    return {

        "found": found,

        "missing": missing,

        "analysis": analysis,

        "score": score

    }