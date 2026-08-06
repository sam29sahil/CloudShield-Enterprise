"""
CloudShield Enterprise
Azure Security Service
"""

from __future__ import annotations

import logging

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

        network = {
            "virtual_networks": self.network.virtual_networks(),
            "subnets": self.network.subnets(),
            "network_security_groups": self.network.network_security_groups(),
            "network_interfaces": self.network.network_interfaces(),
        }

        inventory = {
            "resource_groups": self.resource_groups.list(),
            "virtual_machines": self.virtual_machines.list(),
            "network": network,
            "keyvault": self.keyvault.list(),
            "defender": self.defender.inventory(),
        }

        return inventory

    # --------------------------------------------------
    # Security Assessment
    # --------------------------------------------------

    def scan(self):

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

        return {
            "inventory": inventory,
            "findings": findings,
            "summary": summary,
            "risk": risk,
            "score": score,
            "recommendations": recommendations,
            "report": report,
        }
