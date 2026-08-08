"""
CloudShield Enterprise
Azure Report Generator
"""

from datetime import datetime


class ReportGenerator:
    """
    Generates Azure security reports.
    """

    def __init__(self):
        pass

    def generate(self, findings, summary=None):
        """
        Generate complete report.
        """

        if summary is None:
            summary = {}

        return {
            "generated_at": datetime.utcnow().isoformat(),
            "provider": "Microsoft Azure",
            "summary": summary,
            "findings": findings,
            "total_findings": len(findings),
        }

    def executive_summary(self, findings):

        critical = sum(
            1 for f in findings if f.get("severity") == "Critical"
        )

        high = sum(
            1 for f in findings if f.get("severity") == "High"
        )

        medium = sum(
            1 for f in findings if f.get("severity") == "Medium"
        )

        low = sum(
            1 for f in findings if f.get("severity") == "Low"
        )

        info = sum(
            1 for f in findings if f.get("severity") == "Info"
        )

        return {
            "critical": critical,
            "high": high,
            "medium": medium,
            "low": low,
            "info": info,
            "total": len(findings),
        }

    def export_json(self, findings):

        return self.generate(
            findings,
            self.executive_summary(findings)
        )

    def export_dashboard(self, findings):

        summary = self.executive_summary(findings)

        return {
            "score": max(0, 100 - (summary["critical"] * 20 + summary["high"] * 10)),
            "risk": (
                "Critical"
                if summary["critical"]
                else "High"
                if summary["high"]
                else "Medium"
                if summary["medium"]
                else "Low"
            ),
            "summary": summary,
            "findings": findings,
        }