"""
CloudShield Enterprise
Azure Security Score
"""

from __future__ import annotations


class SecurityScore:
    """
    Convert risk results into a security score and grade.
    """

    MAX_RISK_SCORE = 100

    def calculate(self, risk):

        total_risk = risk.get("total_score", 0)

        score = max(0, self.MAX_RISK_SCORE - total_risk)

        grade = self.grade(score)

        return {
            "security_score": score,
            "grade": grade,
            "risk_level": risk.get("risk_level"),
            "total_risk": total_risk,
        }

    @staticmethod
    def grade(score):

        if score >= 90:

            return "A"

        if score >= 80:

            return "B"

        if score >= 70:

            return "C"

        if score >= 60:

            return "D"

        return "F"

    @staticmethod
    def label(score):

        if score >= 90:

            return "Excellent"

        if score >= 80:

            return "Good"

        if score >= 70:

            return "Fair"

        if score >= 60:

            return "Poor"

        return "Critical"
