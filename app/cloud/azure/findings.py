"""
CloudShield Enterprise
Azure Security Finding
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any


@dataclass
class Finding:
    """
    Standard CloudShield security finding.
    """

    rule_id: str
    severity: str
    category: str
    resource: str

    title: str
    description: str
    recommendation: str

    reference: str = "Microsoft Azure Security Benchmark"

    status: str = "Open"

    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self):

        return {
            "id": self.rule_id,
            "severity": self.severity,
            "category": self.category,
            "resource": self.resource,
            "title": self.title,
            "description": self.description,
            "recommendation": self.recommendation,
            "reference": self.reference,
            "status": self.status,
            "created_at": self.created_at,
            "metadata": self.metadata,
        }

SEVERITY_ORDER = {"Critical": 5, "High": 4, "Medium": 3, "Low": 2, "Info": 1}

def sort_findings(findings):

    return sorted(
        findings,
        key=lambda finding: SEVERITY_ORDER.get(finding.get("severity", "Info"), 0),
        reverse=True,
    )

def count_by_severity(findings):

    counts = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0, "Info": 0}

    for finding in findings:

        severity = finding.get("severity", "Info")

        counts[severity] = counts.get(severity, 0) + 1

    return counts

def group_by_category(findings):

    groups = defaultdict(list)

    for finding in findings:

        groups[finding.get("category", "Other")].append(finding)

    return dict(groups)

def group_by_resource(findings):

    groups = defaultdict(list)

    for finding in findings:

        groups[finding.get("resource", "Unknown")].append(finding)

    return dict(groups)

def group_by_severity(findings):

    groups = defaultdict(list)

    for finding in findings:

        groups[finding.get("severity", "Info")].append(finding)

    return dict(groups)

# --------------------------------------------------

# Finding Statistics
# --------------------------------------------------

def finding_statistics(findings):

    severity = count_by_severity(findings)

    return {
        "total": len(findings),
        "critical": severity["Critical"],
        "high": severity["High"],
        "medium": severity["Medium"],
        "low": severity["Low"],
        "info": severity["Info"],
    }

# --------------------------------------------------
# Filter by Severity
# --------------------------------------------------

def filter_by_severity(findings, severity):

    return [finding for finding in findings if finding.get("severity") == severity]

# --------------------------------------------------
# Filter by Category
# --------------------------------------------------

def filter_by_category(findings, category):

    return [finding for finding in findings if finding.get("category") == category]

# --------------------------------------------------
# Filter by Status
# --------------------------------------------------

def filter_by_status(findings, status):

    return [
        finding for finding in findings if finding.get("status", "Open") == status
    ]

# --------------------------------------------------
# Finding Summary
# --------------------------------------------------

def finding_summary(findings):

    stats = finding_statistics(findings)

    return {
        "total_findings": stats["total"],
        "critical": stats["critical"],
        "high": stats["high"],
        "medium": stats["medium"],
        "low": stats["low"],
        "info": stats["info"],
        "categories": {
            category: len(items)
            for category, items in group_by_category(findings).items()
        },
    }

# --------------------------------------------------
# Export Ready
# --------------------------------------------------

def export_ready(findings):

    return [
        finding if isinstance(finding, dict) else finding.to_dict()
        for finding in findings
    ]
