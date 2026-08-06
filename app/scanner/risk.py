"""
CloudShield Enterprise
Risk Assessment Engine
"""

from app.scanner.constants import RISK_LEVELS


def calculate_risk(score):
    """
    Convert score into risk level.
    """

    for minimum_score, level in RISK_LEVELS:

        if score >= minimum_score:

            if level == "Excellent":

                color = "success"

                summary = (
                    "Excellent security posture. "
                    "Only minor improvements are recommended."
                )

            elif level == "Low":

                color = "primary"

                summary = (
                    "Low security risk. "
                    "Most security best practices are implemented."
                )

            elif level == "Medium":

                color = "warning"

                summary = (
                    "Medium security risk. "
                    "Several improvements should be implemented."
                )

            elif level == "High":

                color = "danger"

                summary = (
                    "High security risk. "
                    "Immediate security improvements are recommended."
                )

            else:

                color = "dark"

                summary = (
                    "Critical security risk. " "The target requires urgent attention."
                )

            return {"score": score, "level": level, "color": color, "summary": summary}

    return {
        "score": 0,
        "level": "Unknown",
        "color": "secondary",
        "summary": "Unable to determine risk.",
    }
