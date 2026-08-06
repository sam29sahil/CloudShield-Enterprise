"""
CloudShield Enterprise
Azure Risk Engine
"""

from __future__ import annotations

from app.cloud.azure.findings import count_by_severity


class AzureRiskEngine:
    """
    Calculate overall Azure security risk.
    """

    WEIGHTS = {"Critical": 10, "High": 7, "Medium": 4, "Low": 2, "Info": 0}

    LEVELS = [
        (80, "Critical"),
        (60, "High"),
        (35, "Medium"),
        (15, "Low"),
        (0, "Minimal"),
    ]

    def calculate(self, findings):

        severity = count_by_severity(findings)

        total_score = 0

        for level, weight in self.WEIGHTS.items():

            total_score += severity[level] * weight

        return {
            "total_score": total_score,
            "risk_level": self.risk_level(total_score),
            "critical": severity["Critical"],
            "high": severity["High"],
            "medium": severity["Medium"],
            "low": severity["Low"],
            "info": severity["Info"],
            "weights": self.WEIGHTS.copy(),
        }

    def risk_level(self, score):

        for minimum, level in self.LEVELS:

            if score >= minimum:

                return level

        return "Minimal"
