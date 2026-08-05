"""
CloudShield Enterprise
Findings Engine
"""

from datetime import datetime
<<<<<<< HEAD
=======
from typing import Any
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


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
<<<<<<< HEAD
            "timestamp": datetime.utcnow().isoformat(),
        }
=======
            "timestamp": datetime.utcnow().isoformat()
        }

    @classmethod
    def technology(cls, tool: str, category: str, target: str, technologies: Any):
        """Build informational findings from technology-identification output."""
        if not isinstance(technologies, dict):
            return []
        return [
            cls.create(
                tool=tool,
                category=category,
                target=target,
                title=f"Technology detected: {name}",
                description=f"{name} was identified by {tool}.",
                raw=details if isinstance(details, dict) else {"value": details},
            )
            for name, details in technologies.items()
        ]


# The short name is the framework API; FindingsEngine remains service-compatible.
Findings = FindingsEngine
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
