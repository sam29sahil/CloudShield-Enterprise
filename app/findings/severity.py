"""
CloudShield Enterprise
Severity Engine
"""


class FindingSeverity:
    """
    Enterprise Severity Engine
    """

    LEVELS = ["Critical", "High", "Medium", "Low", "Info"]

    WEIGHTS = {"Critical": 10, "High": 7, "Medium": 5, "Low": 2, "Info": 0}

    COLORS = {
        "Critical": "danger",
        "High": "warning",
        "Medium": "primary",
        "Low": "secondary",
        "Info": "info",
    }

    ICONS = {
        "Critical": "bi-exclamation-octagon-fill",
        "High": "bi-exclamation-triangle-fill",
        "Medium": "bi-shield-fill-exclamation",
        "Low": "bi-shield",
        "Info": "bi-info-circle-fill",
    }

    @classmethod
    def color(cls, severity):

        return cls.COLORS.get(severity, "secondary")

    @classmethod
    def icon(cls, severity):

        return cls.ICONS.get(severity, "bi-info-circle")

    @classmethod
    def weight(cls, severity):

        return cls.WEIGHTS.get(severity, 0)

    @classmethod
    def valid(cls, severity):

        return severity in cls.LEVELS

    @classmethod
    def sort(cls, findings):

        return sorted(
            findings, key=lambda finding: cls.weight(finding.severity), reverse=True
        )

    @classmethod
    def risk_score(cls, findings):

        score = 0

        for finding in findings:

            score += cls.weight(finding.severity)

        return score

    @classmethod
    def from_cvss(cls, cvss):

        if cvss >= 9:

            return "Critical"

        elif cvss >= 7:

            return "High"

        elif cvss >= 4:

            return "Medium"

        elif cvss > 0:

            return "Low"

        return "Info"

    @classmethod
    def badge(cls, severity):

        return f"bg-{cls.color(severity)}"

    @classmethod
    def is_critical(cls, severity):

        return severity == "Critical"

    @classmethod
    def is_high(cls, severity):

        return severity == "High"

    @classmethod
    def is_medium(cls, severity):

        return severity == "Medium"

    @classmethod
    def is_low(cls, severity):

        return severity == "Low"

    @classmethod
    def is_info(cls, severity):

        return severity == "Info"


# ===========================================
# Backward Compatibility
# ===========================================

SeverityEngine = FindingSeverity
