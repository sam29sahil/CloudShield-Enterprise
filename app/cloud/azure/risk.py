"""
CloudShield Enterprise
Azure Risk Engine
"""


class AzureRiskEngine:
    """
    Calculates CloudShield security score
    from Azure security findings.
    """

    WEIGHTS = {
        "Critical": 25,
        "High": 15,
        "Medium": 8,
        "Low": 3,
        "Info": 0,
    }

    def calculate_score(self, findings):
        """
        Returns a security score between 0 and 100.
        """

        score = 100

        for finding in findings:
            severity = finding.get("severity", "Info")
            score -= self.WEIGHTS.get(severity, 0)

        return max(score, 0)

    def severity_summary(self, findings):

        summary = {
            "Critical": 0,
            "High": 0,
            "Medium": 0,
            "Low": 0,
            "Info": 0,
        }

        for finding in findings:
            severity = finding.get("severity", "Info")

            if severity in summary:
                summary[severity] += 1

        return summary

    def risk_level(self, score):

        if score >= 90:
            return "Excellent"

        if score >= 75:
            return "Good"

        if score >= 50:
            return "Moderate"

        if score >= 25:
            return "High Risk"

        return "Critical"

    def dashboard(self, findings):
        """
        Returns dashboard metrics.
        """

        score = self.calculate_score(findings)

        summary = self.severity_summary(findings)

        return {
            "score": score,
            "risk_level": self.risk_level(score),
            "total_findings": len(findings),
            "critical": summary["Critical"],
            "high": summary["High"],
            "medium": summary["Medium"],
            "low": summary["Low"],
            "info": summary["Info"],
        }
