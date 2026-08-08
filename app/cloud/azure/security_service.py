"""
CloudShield Enterprise
Azure Security Service
"""

from __future__ import annotations

import logging
import json
from datetime import datetime

from app.extensions import db
from app.models.asset import Asset
from app.models.project import Project
from app.models.security_scan import SecurityScan
from app.findings.engine import FindingEngine

from app.cloud.azure.analyzer import AzureAnalyzer
from app.cloud.azure.defender import AzureDefender
from app.cloud.azure.findings import (
    export_ready,
    finding_summary,
)
from app.cloud.azure.keyvault import AzureKeyVault
from app.cloud.azure.network import AzureNetwork
from app.cloud.azure.recommendations import RecommendationEngine
from app.cloud.azure.report import ReportGenerator
from app.cloud.azure.resource_groups import AzureResourceGroups
from app.cloud.azure.risk import AzureRiskEngine
from app.cloud.azure.score import SecurityScore
from app.cloud.azure.virtual_machines import AzureVirtualMachines

logger = logging.getLogger(__name__)


class AzureSecurityService:
    """
    Complete Azure Security Assessment Service.

    Inventory
        ↓
    Analyzer
        ↓
    Risk
        ↓
    Score
        ↓
    Recommendations
        ↓
    Report
    """

    def __init__(self, client):

        self.client = client

        self.resource_groups = AzureResourceGroups(client)
        self.virtual_machines = AzureVirtualMachines(client)
        self.network = AzureNetwork(client)
        self.keyvault = AzureKeyVault(client)
        self.defender = AzureDefender(client)

        self.analyzer = AzureAnalyzer()
        self.risk_engine = AzureRiskEngine()
        self.score_engine = SecurityScore()
        self.recommendation_engine = RecommendationEngine()
        self.report_generator = ReportGenerator()

    # --------------------------------------------------
    # Inventory
    # --------------------------------------------------

    def inventory(self):

        logger.info("Collecting Azure inventory...")

        network_result = {
            "virtual_networks": self.network.virtual_networks(),
            "network_security_groups": self.network.network_security_groups(),
            "network_interfaces": self.network.network_interfaces(),
        }

        inventory = {
            "resource_groups": self.resource_groups.list(),
            "virtual_machines": self.virtual_machines.list(),
            "network": network_result,
            "keyvault": self.keyvault.list(),
            "defender": self.defender.overview(),
        }

        # The analyzer consumes inventory lists, while the Azure service
        # modules return standardized {success, data, ...} dictionaries.
        def data_or_empty(result):
            if isinstance(result, dict):
                value = result.get("data", [])
                return value if isinstance(value, list) else []
            return result if isinstance(result, list) else []

        normalized = {
            "resource_groups": data_or_empty(inventory["resource_groups"]),
            "virtual_machines": data_or_empty(inventory["virtual_machines"]),
            "network": {
                "virtual_networks": data_or_empty(network_result["virtual_networks"]),
                "subnets": data_or_empty(
                    self.network.subnets()
                ),
                "network_security_groups": data_or_empty(
                    network_result["network_security_groups"]
                ),
                "network_interfaces": data_or_empty(
                    network_result["network_interfaces"]
                ),
            },
            "keyvault": data_or_empty(inventory["keyvault"]),
            "defender": inventory["defender"],
        }

        return normalized

    # --------------------------------------------------
    # Security Assessment
    # --------------------------------------------------

    def scan(self, user_id=None, project_id=None):

        started = datetime.utcnow()

        inventory = self.inventory()

        findings = self.analyzer.analyze(inventory)

        findings = export_ready(findings)

        risk = self.risk_engine.calculate(findings)

        score = self.score_engine.calculate(risk)

        recommendations = self.recommendation_engine.generate(findings)

        summary = finding_summary(findings)

        report = self.report_generator.generate(
            inventory=inventory,
            findings=findings,
            summary=summary,
            risk=risk,
            score=score,
            recommendations=recommendations,
        )

        persisted = {
            "scan_id": None,
            "asset_id": None,
            "findings_created": 0,
            "message": "Scan results were returned without database persistence.",
        }

        # Link the existing Azure scanner to the existing CloudShield
        # SecurityScan + FindingEngine pipeline when user/project context exists.
        if user_id is not None:
            try:
                project = None

                if project_id:
                    project = Project.query.get(project_id)

                if project is None:
                    project = Project.query.order_by(Project.id.asc()).first()

                if project is not None:

                    target = f"azure:{self.client.subscription()}"

                    asset = Asset.query.filter_by(
                        project_id=project.id,
                        target=target,
                    ).first()

                    if asset is None:
                        asset = Asset(
                            project_id=project.id,
                            name="Azure Subscription",
                            target=target,
                            asset_type="Azure",
                        )
                        db.session.add(asset)
                        db.session.flush()

                    completed = datetime.utcnow()
                    duration = (completed - started).total_seconds()

                    scan = SecurityScan(
                        user_id=user_id,
                        asset_id=asset.id,
                        category="Cloud",
                        tool="azure_basic_security_scan",
                        target=self.client.subscription(),
                        arguments="",
                        status="Completed",
                        score=score.get("security_score", 0),
                        risk=risk.get("risk_level", "Unknown"),
                        raw_output=json.dumps(
                            inventory, indent=2, default=str
                        ),
                        parsed_output=json.dumps(
                            {
                                "findings": findings,
                                "summary": summary,
                                "risk": risk,
                                "score": score,
                                "recommendations": recommendations,
                            },
                            indent=2,
                            default=str,
                        ),
                        started_at=started,
                        completed_at=completed,
                        duration=duration,
                    )

                    db.session.add(scan)
                    db.session.flush()

                    created = 0

                    for finding in findings:

                        created_finding = FindingEngine.create(
                            scan=scan,
                            title=finding.get("title", "Azure Security Finding"),
                            severity=finding.get("severity", "Low"),
                            description=finding.get("description", ""),
                            recommendation=finding.get("recommendation", ""),
                            category=finding.get("category", "Azure"),
                            cvss=float(finding.get("cvss", 0.0) or 0.0),
                            evidence=json.dumps(
                                finding.get("metadata", {}),
                                default=str,
                            ),
                        )

                        if created_finding is not None:
                            created += 1

                    asset.score = score.get("security_score", 0)
                    asset.risk = risk.get("risk_level", "Unknown")

                    db.session.commit()

                    persisted = {
                        "scan_id": scan.id,
                        "asset_id": asset.id,
                        "findings_created": created,
                        "message": "Azure scan linked to the existing findings engine.",
                    }

                else:
                    logger.warning(
                        "Azure scan completed, but no project exists; "
                        "database persistence skipped."
                    )

            except Exception:
                db.session.rollback()
                logger.exception(
                    "Azure scan completed but finding persistence failed."
                )
                persisted["message"] = (
                    "Azure scan completed, but persistence failed. "
                    "Check the application log."
                )

        return {
            "inventory": inventory,
            "findings": findings,
            "summary": summary,
            "risk": risk,
            "score": score,
            "recommendations": recommendations,
            "report": report,
            "persistence": persisted,
        }
