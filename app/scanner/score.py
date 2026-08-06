"""
CloudShield Enterprise
Security Score Engine
"""

from app.scanner.constants import SCORE_WEIGHTS


def calculate_security_score(
    website,
    headers,
    ssl_info,
    dns_info,
    whois_info,
    technology,
):
    """
    Calculate overall security score.
    """

    total_score = 0

    details = {}

    # ---------------------------------
    # Website
    # ---------------------------------

    website_score = 0

    if website.get("success"):

        website_score = 100

    total_score += (
        website_score *
        SCORE_WEIGHTS["website"]
    ) / 100

    details["website"] = website_score

    # ---------------------------------
    # Headers
    # ---------------------------------

    header_score = headers.get(
        "score",
        0
    )

    total_score += (
        header_score *
        SCORE_WEIGHTS["headers"]
    ) / 100

    details["headers"] = header_score

    # ---------------------------------
    # SSL
    # ---------------------------------

    ssl_score = 0

    if ssl_info:

        if ssl_info.get("valid"):

            ssl_score = 100

        else:

            ssl_score = 40

    total_score += (
        ssl_score *
        SCORE_WEIGHTS["ssl"]
    ) / 100

    details["ssl"] = ssl_score

    # ---------------------------------
    # DNS
    # ---------------------------------

    dns_score = 0

    if dns_info:

        records = 0

        for value in dns_info.values():

            if value:

                records += 1

        dns_score = min(
            records * 20,
            100
        )

    total_score += (
        dns_score *
        SCORE_WEIGHTS["dns"]
    ) / 100

    details["dns"] = dns_score

    # ---------------------------------
    # WHOIS
    # ---------------------------------

    whois_score = 0

    if whois_info:

        if whois_info.get("success"):

            whois_score = 100

    total_score += (
        whois_score *
        SCORE_WEIGHTS["whois"]
    ) / 100

    details["whois"] = whois_score

    # ---------------------------------
    # Technology
    # ---------------------------------

    tech_score = 50

    if technology:

        if technology.get("technologies"):

            tech_score = 100

    total_score += (
        tech_score *
        SCORE_WEIGHTS["technology"]
    ) / 100

    details["technology"] = tech_score

    # ---------------------------------
    # Recommendation
    # ---------------------------------

    recommendation_score = header_score

    total_score += (
        recommendation_score *
        SCORE_WEIGHTS["recommendations"]
    ) / 100

    details["recommendations"] = recommendation_score

    return {

        "overall_score": round(total_score),

        "details": details

    }