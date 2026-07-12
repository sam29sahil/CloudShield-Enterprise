"""
CloudShield Enterprise
Severity Engine
"""


class SeverityEngine:

    def calculate(self, score):

        if score >= 90:

            return "Info"

        elif score >= 75:

            return "Low"

        elif score >= 50:

            return "Medium"

        elif score >= 25:

            return "High"

        return "Critical"