"""
CloudShield Enterprise
Risk Engine
"""


class RiskEngine:
    """
    Calculates overall risk score and security grade.
    """

<<<<<<< HEAD
    SEVERITY_SCORES = {"Critical": 10, "High": 7, "Medium": 4, "Low": 2, "Info": 1}
=======
    SEVERITY_SCORES = {
        "Critical": 10,
        "High": 7,
        "Medium": 4,
        "Low": 2,
        "Info": 1
    }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @classmethod
    def calculate(cls, findings):

        total_score = 0

<<<<<<< HEAD
        summary = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0, "Info": 0}
=======
        summary = {
            "Critical": 0,
            "High": 0,
            "Medium": 0,
            "Low": 0,
            "Info": 0
        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

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
<<<<<<< HEAD
            "total_findings": len(findings),
=======
            "total_findings": len(findings)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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

<<<<<<< HEAD
        return "A"
=======
        return "A"
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
