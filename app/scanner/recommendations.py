"""
CloudShield Enterprise
Recommendation Engine
"""

from app.scanner.constants import SECURITY_HEADERS


def generate_recommendations(header_result):
    """
    Generate security recommendations
    based on missing security headers.
    """

    recommendations = []

    missing_headers = header_result.get(
        "missing",
        []
    )

    for header in missing_headers:

        info = SECURITY_HEADERS.get(header)

        if not info:
            continue

        recommendations.append({

            "title": header,

            "severity": info["severity"],

            "problem": info["description"],

            "recommendation":
                f"Configure the {header} HTTP header.",

            "impact": get_impact(header)

        })

    return recommendations


def get_impact(header):

    impacts = {

        "Strict-Transport-Security":

            "Protects users from HTTPS downgrade attacks.",

        "Content-Security-Policy":

            "Helps prevent Cross Site Scripting (XSS).",

        "X-Frame-Options":

            "Protects against Clickjacking attacks.",

        "X-Content-Type-Options":

            "Prevents MIME-Type sniffing.",

        "Referrer-Policy":

            "Prevents information leakage through referrers.",

        "Permissions-Policy":

            "Restricts unnecessary browser permissions."

    }

    return impacts.get(

        header,

        "No impact information available."

    )