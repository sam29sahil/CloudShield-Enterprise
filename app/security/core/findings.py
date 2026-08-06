"""
CloudShield Enterprise
Findings Engine
"""

from datetime import datetime


class FindingsEngine:
    """
    Converts scan results into standardized findings.
    """

    @staticmethod
    def create(
        tool,
        category,
        target,
        severity="Info",
        title="",
        description="",
        recommendation="",
        references=None,
        raw=None,
    ):

        if references is None:
            references = []

        if raw is None:
            raw = {}

        return {
            "tool": tool,
            "category": category,
            "target": target,
            "severity": severity,
            "title": title,
            "description": description,
            "recommendation": recommendation,
            "references": references,
            "raw": raw,
            "timestamp": datetime.utcnow().isoformat(),
        }
