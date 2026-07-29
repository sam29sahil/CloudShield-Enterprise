"""
CloudShield Enterprise
Risk Engine
"""


class RiskEngine:
    """
    Calculates overall risk score and security grade.
    """

    SEVERITY_SCORES = {
        "Critical": 10,
        "High": 7,
        "Medium": 4,
        "Low": 2,
        "Info": 1
    }

    @classmethod
    def calculate(cls, findings):

        total_score = 0

        summary = {
            "Critical": 0,
            "High": 0,
            "Medium": 0,
            "Low": 0,
            "Info": 0
        }

        for finding in findings:

            severity = finding.get("severity", "Info")

            if severity not in summary:
                severity = "Info"

            summary[severity] += 1
            total_score += cls.SEVERITY_SCORES[severity]

        grade = cls.grade(total_score)

        return {
            "risk_score": total_score,
            "grade": grade,
            "summary": summary,
            "total_findings": len(findings)
        }

    @staticmethod
    def grade(score):

        if score >= 80:
            return "F"

        if score >= 60:
            return "D"

        if score >= 40:
            return "C"

        if score >= 20:
            return "B"

        return "A"