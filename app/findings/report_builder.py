"""
CloudShield Enterprise
Enterprise Report Builder
"""

from datetime import datetime

from app.findings.aggregator import FindingAggregator
from app.findings.statistics import FindingStatistics
from app.findings.exporter import FindingExporter


class ReportBuilder:
    """
    Enterprise Report Builder
    """

    # =====================================================
    # HEADER
    # =====================================================

    @staticmethod
    def header(title):

        return {

            "title": title,

            "generated_at": datetime.utcnow(),

            "product": "CloudShield Enterprise",

            "version": "1.0"

        }

    # =====================================================
    # SUMMARY
    # =====================================================

    @staticmethod
    def summary(findings):

        return {

            "total": len(findings),

            "severity": FindingAggregator.by_severity(

                findings

            ),

            "status": FindingAggregator.by_status(

                findings

            ),

            "categories": FindingAggregator.by_category(

                findings

            ),

            "risk_score": FindingAggregator.risk_score(

                findings

            )

        }

    # =====================================================
    # FINDINGS
    # =====================================================

    @staticmethod
    def findings(findings):

        return FindingExporter.serialize_many(

            findings

        )
    
        # =====================================================
    # EXECUTIVE REPORT
    # =====================================================

    @staticmethod
    def executive(findings):

        return {

            "header": ReportBuilder.header(

                "Executive Security Report"

            ),

            "summary": ReportBuilder.summary(

                findings

            ),

            "dashboard": FindingAggregator.dashboard(

                findings

            ),

            "statistics": FindingStatistics.executive_summary(),

            "findings": FindingExporter.serialize_many(

                findings

            )

        }

    # =====================================================
    # TECHNICAL REPORT
    # =====================================================

    @staticmethod
    def technical(findings):

        return {

            "header": ReportBuilder.header(

                "Technical Security Report"

            ),

            "summary": ReportBuilder.summary(

                findings

            ),

            "timeline": FindingAggregator.timeline(

                findings

            ),

            "monthly": FindingAggregator.monthly(

                findings

            ),

            "findings": FindingExporter.serialize_many(

                findings

            )

        }

    # =====================================================
    # PROJECT REPORT
    # =====================================================

    @staticmethod
    def project(project, findings):

        return {

            "header": ReportBuilder.header(

                f"Project Report - {project.name}"

            ),

            "project": {

                "id": project.id,

                "name": project.name

            },

            "summary": ReportBuilder.summary(

                findings

            ),

            "findings": FindingExporter.serialize_many(

                findings

            )

        }

    # =====================================================
    # ASSET REPORT
    # =====================================================

    @staticmethod
    def asset(asset, findings):

        return {

            "header": ReportBuilder.header(

                f"Asset Report - {asset.name}"

            ),

            "asset": {

                "id": asset.id,

                "name": asset.name,

                "target": asset.target

            },

            "summary": ReportBuilder.summary(

                findings

            ),

            "findings": FindingExporter.serialize_many(

                findings

            )

        }
    
        # =====================================================
    # SCAN REPORT
    # =====================================================

    @staticmethod
    def scan(scan, findings):

        return {

            "header": ReportBuilder.header(

                f"Scan Report - {scan.tool}"

            ),

            "scan": {

                "id": scan.id,

                "tool": scan.tool,

                "target": scan.target,

                "category": scan.category,

                "started_at": scan.started_at,

                "completed_at": scan.completed_at,

                "duration": scan.duration

            },

            "summary": ReportBuilder.summary(

                findings

            ),

            "findings": FindingExporter.serialize_many(

                findings

            )

        }

    # =====================================================
    # COMPLIANCE REPORT
    # =====================================================

    @staticmethod
    def compliance(findings):

        return {

            "header": ReportBuilder.header(

                "Compliance Report"

            ),

            "summary": ReportBuilder.summary(

                findings

            ),

            "statistics": FindingStatistics.summary(),

            "categories": FindingAggregator.by_category(

                findings

            ),

            "findings": FindingExporter.serialize_many(

                findings

            )

        }

    # =====================================================
    # RISK REPORT
    # =====================================================

    @staticmethod
    def risk(findings):

        return {

            "header": ReportBuilder.header(

                "Risk Assessment Report"

            ),

            "risk_score": FindingAggregator.risk_score(

                findings

            ),

            "severity": FindingAggregator.by_severity(

                findings

            ),

            "cvss": FindingAggregator.cvss(

                findings

            ),

            "findings": FindingExporter.serialize_many(

                findings

            )

        }

    # =====================================================
    # MANAGEMENT REPORT
    # =====================================================

    @staticmethod
    def management(findings):

        return {

            "header": ReportBuilder.header(

                "Management Report"

            ),

            "dashboard": FindingAggregator.dashboard(

                findings

            ),

            "statistics": FindingStatistics.executive_summary(),

            "top_assets": FindingAggregator.top_assets(

                findings

            ),

            "top_projects": FindingAggregator.top_projects(

                findings

            ),

            "findings": FindingExporter.serialize_many(

                findings

            )

        }
        # =====================================================
    # METADATA
    # =====================================================

    @staticmethod
    def metadata():

        return {

            "product": "CloudShield Enterprise",

            "module": "Findings",

            "version": "1.0",

            "generated_at": datetime.utcnow()

        }

    # =====================================================
    # JSON REPORT
    # =====================================================

    @staticmethod
    def json(findings):

        return {

            "metadata": ReportBuilder.metadata(),

            "report": ReportBuilder.executive(

                findings

            )

        }

    # =====================================================
    # COMPLETE PACKAGE
    # =====================================================

    @staticmethod
    def package(findings):

        return {

            "metadata": ReportBuilder.metadata(),

            "executive": ReportBuilder.executive(

                findings

            ),

            "technical": ReportBuilder.technical(

                findings

            ),

            "risk": ReportBuilder.risk(

                findings

            ),

            "management": ReportBuilder.management(

                findings

            ),

            "compliance": ReportBuilder.compliance(

                findings

            )

        }

    # =====================================================
    # BUILD
    # =====================================================

    @staticmethod
    def build(report_type, findings, **kwargs):

        if report_type == "executive":

            return ReportBuilder.executive(

                findings

            )

        elif report_type == "technical":

            return ReportBuilder.technical(

                findings

            )

        elif report_type == "risk":

            return ReportBuilder.risk(

                findings

            )

        elif report_type == "management":

            return ReportBuilder.management(

                findings

            )

        elif report_type == "compliance":

            return ReportBuilder.compliance(

                findings

            )

        elif report_type == "project":

            return ReportBuilder.project(

                kwargs["project"],

                findings

            )

        elif report_type == "asset":

            return ReportBuilder.asset(

                kwargs["asset"],

                findings

            )

        elif report_type == "scan":

            return ReportBuilder.scan(

                kwargs["scan"],

                findings

            )

        return ReportBuilder.executive(

            findings

        )