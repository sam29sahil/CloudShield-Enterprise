"""
CloudShield Enterprise
Severity Engine
"""


class FindingSeverity:
    """
    Enterprise Severity Engine
    """

<<<<<<< HEAD
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
=======
    LEVELS = [

        "Critical",

        "High",

        "Medium",

        "Low",

        "Info"

    ]

    WEIGHTS = {

        "Critical": 10,

        "High": 7,

        "Medium": 5,

        "Low": 2,

        "Info": 0

    }

    COLORS = {

        "Critical": "danger",

        "High": "warning",

        "Medium": "primary",

        "Low": "secondary",

        "Info": "info"

    }

    ICONS = {

        "Critical": "bi-exclamation-octagon-fill",

        "High": "bi-exclamation-triangle-fill",

        "Medium": "bi-shield-fill-exclamation",

        "Low": "bi-shield",

        "Info": "bi-info-circle-fill"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    }

    @classmethod
    def color(cls, severity):

<<<<<<< HEAD
        return cls.COLORS.get(severity, "secondary")
=======
        return cls.COLORS.get(

            severity,

            "secondary"

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @classmethod
    def icon(cls, severity):

<<<<<<< HEAD
        return cls.ICONS.get(severity, "bi-info-circle")
=======
        return cls.ICONS.get(

            severity,

            "bi-info-circle"

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @classmethod
    def weight(cls, severity):

<<<<<<< HEAD
        return cls.WEIGHTS.get(severity, 0)
=======
        return cls.WEIGHTS.get(

            severity,

            0

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @classmethod
    def valid(cls, severity):

        return severity in cls.LEVELS

    @classmethod
    def sort(cls, findings):

        return sorted(
<<<<<<< HEAD
            findings, key=lambda finding: cls.weight(finding.severity), reverse=True
=======

            findings,

            key=lambda finding: cls.weight(

                finding.severity

            ),

            reverse=True

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

    @classmethod
    def risk_score(cls, findings):

        score = 0

        for finding in findings:

<<<<<<< HEAD
            score += cls.weight(finding.severity)
=======
            score += cls.weight(

                finding.severity

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

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
<<<<<<< HEAD


=======
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# ===========================================
# Backward Compatibility
# ===========================================

<<<<<<< HEAD
SeverityEngine = FindingSeverity
=======
SeverityEngine = FindingSeverity
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
