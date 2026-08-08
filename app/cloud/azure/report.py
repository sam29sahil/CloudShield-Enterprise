"""
CloudShield Enterprise
Azure Basic Security Scan Report Generator
"""

from datetime import datetime


class ReportGenerator:
    """
    Report generator specifically for the Basic Azure Security Scan.

    The generator does not perform scanning.
    It only formats the results produced by:

        AzureSecurityService
            ↓
        Inventory
            ↓
        Analyzer
            ↓
        Risk Engine
            ↓
        Security Score
            ↓
        Recommendations
            ↓
        Basic Azure Report
    """

    def __init__(self):
        pass

    # ==================================================
    # COMPLETE REPORT
    # ==================================================

    def generate(
        self,
        findings,
        summary=None,
        inventory=None,
        risk=None,
        score=None,
        recommendations=None,
    ):
        """
        Generate the complete Basic Azure Security Report.
        """

        findings = (
            findings
            if isinstance(findings, list)
            else []
        )

        inventory = (
            inventory
            if isinstance(inventory, dict)
            else {}
        )

        risk = (
            risk
            if isinstance(risk, dict)
            else {}
        )

        score = (
            score
            if isinstance(score, dict)
            else {}
        )

        recommendations = (
            recommendations
            if isinstance(recommendations, list)
            else []
        )

        if summary is None:
            summary = self.executive_summary(
                findings
            )

        # ------------------------------------------
        # Inventory Summary
        # ------------------------------------------

        inventory_summary = self.inventory_summary(
            inventory
        )

        # ------------------------------------------
        # Score
        # ------------------------------------------

        security_score = score.get(
            "security_score",
            score.get("score", 0),
        )

        # ------------------------------------------
        # Risk
        # ------------------------------------------

        risk_level = risk.get(
            "risk_level",
            "Unknown",
        )

        return {
            # ======================================
            # Metadata
            # ======================================

            "generated_at": datetime.utcnow().isoformat(),

            "provider": "Microsoft Azure",

            "report_type": (
                "Basic Azure Security Assessment"
            ),

            "scanner": (
                "CloudShield Enterprise "
                "Azure Basic Security Scanner"
            ),

            # ======================================
            # Executive Summary
            # ======================================

            "summary": summary,

            "executive_summary": (
                self.executive_summary(findings)
            ),

            # ======================================
            # Security Score
            # ======================================

            "score": score,

            "security_score": security_score,

            # ======================================
            # Risk
            # ======================================

            "risk": risk,

            "risk_level": risk_level,

            # ======================================
            # Inventory
            # ======================================

            "inventory": inventory,

            "inventory_summary": inventory_summary,

            # ======================================
            # Findings
            # ======================================

            "findings": findings,

            "total_findings": len(findings),

            "severity": self.severity_breakdown(
                findings
            ),

            # ======================================
            # Recommendations
            # ======================================

            "recommendations": recommendations,

            "recommendation_count": len(
                recommendations
            ),

            # ======================================
            # Scan Status
            # ======================================

            "status": "Completed",
        }

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    def executive_summary(self, findings):

        if not isinstance(findings, list):
            findings = []

        critical = 0
        high = 0
        medium = 0
        low = 0
        info = 0

        for finding in findings:

            if not isinstance(finding, dict):
                continue

            severity = str(
                finding.get(
                    "severity",
                    "Info",
                )
            ).lower()

            if severity == "critical":
                critical += 1

            elif severity == "high":
                high += 1

            elif severity == "medium":
                medium += 1

            elif severity == "low":
                low += 1

            else:
                info += 1

        return {
            "critical": critical,
            "high": high,
            "medium": medium,
            "low": low,
            "info": info,
            "total": len(findings),
        }

    # ==================================================
    # SEVERITY BREAKDOWN
    # ==================================================

    def severity_breakdown(self, findings):

        summary = self.executive_summary(
            findings
        )

        return {
            "critical": summary["critical"],
            "high": summary["high"],
            "medium": summary["medium"],
            "low": summary["low"],
            "info": summary["info"],
        }

    # ==================================================
    # INVENTORY SUMMARY
    # ==================================================

    def inventory_summary(self, inventory):

        if not isinstance(inventory, dict):
            return {}

        resource_groups = self._data(
            inventory.get("resource_groups")
        )

        virtual_machines = self._data(
            inventory.get("virtual_machines")
        )

        keyvault = self._data(
            inventory.get("keyvault")
        )

        network = inventory.get(
            "network",
            {},
        )

        if not isinstance(network, dict):
            network = {}

        virtual_networks = self._data(
            network.get("virtual_networks")
        )

        subnets = self._data(
            network.get("subnets")
        )

        network_security_groups = self._data(
            network.get(
                "network_security_groups"
            )
        )

        network_interfaces = self._data(
            network.get(
                "network_interfaces"
            )
        )

        defender = inventory.get(
            "defender",
            {},
        )

        if not isinstance(defender, dict):
            defender = {}

        return {
            "resource_groups": len(
                resource_groups
            ),

            "virtual_machines": len(
                virtual_machines
            ),

            "virtual_networks": len(
                virtual_networks
            ),

            "subnets": len(
                subnets
            ),

            "network_security_groups": len(
                network_security_groups
            ),

            "network_interfaces": len(
                network_interfaces
            ),

            "keyvaults": len(
                keyvault
            ),

            "defender": {
                "secure_score": defender.get(
                    "secure_score",
                    0,
                ),

                "alerts": self._count(
                    defender.get(
                        "alerts",
                        [],
                    )
                ),

                "recommendations": self._count(
                    defender.get(
                        "recommendations",
                        [],
                    )
                ),
            },
        }

    # ==================================================
    # DATA NORMALIZER
    # ==================================================

    def _data(self, value):

        if isinstance(value, dict):

            data = value.get(
                "data",
                [],
            )

            return (
                data
                if isinstance(data, list)
                else []
            )

        if isinstance(value, list):
            return value

        return []

    # ==================================================
    # COUNT HELPER
    # ==================================================

    def _count(self, value):

        if isinstance(value, list):
            return len(value)

        if isinstance(value, dict):

            data = value.get(
                "data"
            )

            if isinstance(data, list):
                return len(data)

            return value.get(
                "count",
                0,
            )

        if isinstance(value, int):
            return value

        return 0

    # ==================================================
    # RISK SUMMARY
    # ==================================================

    def risk_summary(
        self,
        findings,
        risk=None,
    ):

        if not isinstance(risk, dict):
            risk = {}

        summary = self.executive_summary(
            findings
        )

        return {
            "risk_level": risk.get(
                "risk_level",
                "Unknown",
            ),

            "critical_findings": summary[
                "critical"
            ],

            "high_findings": summary[
                "high"
            ],

            "medium_findings": summary[
                "medium"
            ],

            "low_findings": summary[
                "low"
            ],
        }

    # ==================================================
    # DASHBOARD EXPORT
    # ==================================================

    def export_dashboard(
        self,
        findings,
        summary=None,
        risk=None,
        score=None,
        recommendations=None,
    ):
        """
        Return compact data for the Azure dashboard.
        """

        findings = (
            findings
            if isinstance(findings, list)
            else []
        )

        if summary is None:
            summary = self.executive_summary(
                findings
            )

        risk = (
            risk
            if isinstance(risk, dict)
            else {}
        )

        score = (
            score
            if isinstance(score, dict)
            else {}
        )

        recommendations = (
            recommendations
            if isinstance(recommendations, list)
            else []
        )

        return {
            "provider": "Microsoft Azure",

            "security_score": score.get(
                "security_score",
                score.get(
                    "score",
                    0,
                ),
            ),

            "risk_level": risk.get(
                "risk_level",
                "Unknown",
            ),

            "summary": summary,

            "severity": self.severity_breakdown(
                findings
            ),

            "findings": findings,

            "total_findings": len(
                findings
            ),

            "recommendations": recommendations,

            "recommendation_count": len(
                recommendations
            ),
        }

    # ==================================================
    # JSON EXPORT
    # ==================================================

    def export_json(
        self,
        findings,
        summary=None,
        inventory=None,
        risk=None,
        score=None,
        recommendations=None,
    ):
        """
        Return JSON-serializable report data.
        """

        return self.generate(
            findings=findings,
            summary=summary,
            inventory=inventory,
            risk=risk,
            score=score,
            recommendations=recommendations,
        )

    # ==================================================
    # FINDINGS EXPORT
    # ==================================================

    def export_findings(self, findings):

        if not isinstance(findings, list):
            return []

        return [
            {
                "rule_id": finding.get(
                    "rule_id",
                    "",
                ),

                "title": finding.get(
                    "title",
                    "Azure Security Finding",
                ),

                "severity": finding.get(
                    "severity",
                    "Info",
                ),

                "category": finding.get(
                    "category",
                    "Azure",
                ),

                "resource": finding.get(
                    "resource",
                    finding.get(
                        "resource_name",
                        "Unknown",
                    ),
                ),

                "description": finding.get(
                    "description",
                    "",
                ),

                "recommendation": finding.get(
                    "recommendation",
                    "",
                ),

                "evidence": finding.get(
                    "evidence",
                    finding.get(
                        "metadata",
                        {},
                    ),
                ),
            }
            for finding in findings
            if isinstance(finding, dict)
        ]
