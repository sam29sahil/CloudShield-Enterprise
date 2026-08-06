"""
CloudShield Enterprise
Azure Security Recommendations
"""

from __future__ import annotations

from collections import defaultdict


class RecommendationEngine:
    """
    Groups findings into remediation recommendations.
    """

    def generate(self, findings):

        grouped = defaultdict(
            lambda: {"severity": "", "recommendation": "", "resources": []}
        )

        for finding in findings:

            recommendation = finding.get(
                "recommendation", "No recommendation available."
            )

            group = grouped[recommendation]

            group["severity"] = finding.get("severity", "Info")

            group["recommendation"] = recommendation

            resource = finding.get("resource", "Unknown")

            if resource not in group["resources"]:

                group["resources"].append(resource)

        recommendations = []

        for item in grouped.values():

            recommendations.append(
                {
                    "severity": item["severity"],
                    "recommendation": item["recommendation"],
                    "affected_resources": len(item["resources"]),
                    "resources": sorted(item["resources"]),
                }
            )

        severity_order = {"Critical": 5, "High": 4, "Medium": 3, "Low": 2, "Info": 1}

        recommendations.sort(
            key=lambda item: severity_order.get(item["severity"], 0), reverse=True
        )

        return recommendations
