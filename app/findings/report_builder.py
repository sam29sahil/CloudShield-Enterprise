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
<<<<<<< HEAD
            "title": title,
            "generated_at": datetime.utcnow(),
            "product": "CloudShield Enterprise",
            "version": "1.0",
=======

            "title": title,

            "generated_at": datetime.utcnow(),

            "product": "CloudShield Enterprise",

            "version": "1.0"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # SUMMARY
    # =====================================================

    @staticmethod
    def summary(findings):

        return {
<<<<<<< HEAD
            "total": len(findings),
            "severity": FindingAggregator.by_severity(findings),
            "status": FindingAggregator.by_status(findings),
            "categories": FindingAggregator.by_category(findings),
            "risk_score": FindingAggregator.risk_score(findings),
=======

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

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # FINDINGS
    # =====================================================

    @staticmethod
    def findings(findings):

<<<<<<< HEAD
        return FindingExporter.serialize_many(findings)

        # =====================================================

=======
        return FindingExporter.serialize_many(

            findings

        )
    
        # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # EXECUTIVE REPORT
    # =====================================================

    @staticmethod
    def executive(findings):

        return {
<<<<<<< HEAD
            "header": ReportBuilder.header("Executive Security Report"),
            "summary": ReportBuilder.summary(findings),
            "dashboard": FindingAggregator.dashboard(findings),
            "statistics": FindingStatistics.executive_summary(),
            "findings": FindingExporter.serialize_many(findings),
=======

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

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # TECHNICAL REPORT
    # =====================================================

    @staticmethod
    def technical(findings):

        return {
<<<<<<< HEAD
            "header": ReportBuilder.header("Technical Security Report"),
            "summary": ReportBuilder.summary(findings),
            "timeline": FindingAggregator.timeline(findings),
            "monthly": FindingAggregator.monthly(findings),
            "findings": FindingExporter.serialize_many(findings),
=======

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

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # PROJECT REPORT
    # =====================================================

    @staticmethod
    def project(project, findings):

        return {
<<<<<<< HEAD
            "header": ReportBuilder.header(f"Project Report - {project.name}"),
            "project": {"id": project.id, "name": project.name},
            "summary": ReportBuilder.summary(findings),
            "findings": FindingExporter.serialize_many(findings),
=======

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

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # ASSET REPORT
    # =====================================================

    @staticmethod
    def asset(asset, findings):

        return {
<<<<<<< HEAD
            "header": ReportBuilder.header(f"Asset Report - {asset.name}"),
            "asset": {"id": asset.id, "name": asset.name, "target": asset.target},
            "summary": ReportBuilder.summary(findings),
            "findings": FindingExporter.serialize_many(findings),
        }

        # =====================================================

=======

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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # SCAN REPORT
    # =====================================================

    @staticmethod
    def scan(scan, findings):

        return {
<<<<<<< HEAD
            "header": ReportBuilder.header(f"Scan Report - {scan.tool}"),
            "scan": {
                "id": scan.id,
                "tool": scan.tool,
                "target": scan.target,
                "category": scan.category,
                "started_at": scan.started_at,
                "completed_at": scan.completed_at,
                "duration": scan.duration,
            },
            "summary": ReportBuilder.summary(findings),
            "findings": FindingExporter.serialize_many(findings),
=======

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

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # COMPLIANCE REPORT
    # =====================================================

    @staticmethod
    def compliance(findings):

        return {
<<<<<<< HEAD
            "header": ReportBuilder.header("Compliance Report"),
            "summary": ReportBuilder.summary(findings),
            "statistics": FindingStatistics.summary(),
            "categories": FindingAggregator.by_category(findings),
            "findings": FindingExporter.serialize_many(findings),
=======

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

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # RISK REPORT
    # =====================================================

    @staticmethod
    def risk(findings):

        return {
<<<<<<< HEAD
            "header": ReportBuilder.header("Risk Assessment Report"),
            "risk_score": FindingAggregator.risk_score(findings),
            "severity": FindingAggregator.by_severity(findings),
            "cvss": FindingAggregator.cvss(findings),
            "findings": FindingExporter.serialize_many(findings),
=======

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

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # MANAGEMENT REPORT
    # =====================================================

    @staticmethod
    def management(findings):

        return {
<<<<<<< HEAD
            "header": ReportBuilder.header("Management Report"),
            "dashboard": FindingAggregator.dashboard(findings),
            "statistics": FindingStatistics.executive_summary(),
            "top_assets": FindingAggregator.top_assets(findings),
            "top_projects": FindingAggregator.top_projects(findings),
            "findings": FindingExporter.serialize_many(findings),
        }
        # =====================================================

=======

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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # METADATA
    # =====================================================

    @staticmethod
    def metadata():

        return {
<<<<<<< HEAD
            "product": "CloudShield Enterprise",
            "module": "Findings",
            "version": "1.0",
            "generated_at": datetime.utcnow(),
=======

            "product": "CloudShield Enterprise",

            "module": "Findings",

            "version": "1.0",

            "generated_at": datetime.utcnow()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # JSON REPORT
    # =====================================================

    @staticmethod
    def json(findings):

        return {
<<<<<<< HEAD
            "metadata": ReportBuilder.metadata(),
            "report": ReportBuilder.executive(findings),
=======

            "metadata": ReportBuilder.metadata(),

            "report": ReportBuilder.executive(

                findings

            )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # COMPLETE PACKAGE
    # =====================================================

    @staticmethod
    def package(findings):

        return {
<<<<<<< HEAD
            "metadata": ReportBuilder.metadata(),
            "executive": ReportBuilder.executive(findings),
            "technical": ReportBuilder.technical(findings),
            "risk": ReportBuilder.risk(findings),
            "management": ReportBuilder.management(findings),
            "compliance": ReportBuilder.compliance(findings),
=======

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

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # BUILD
    # =====================================================

    @staticmethod
    def build(report_type, findings, **kwargs):

        if report_type == "executive":

<<<<<<< HEAD
            return ReportBuilder.executive(findings)

        elif report_type == "technical":

            return ReportBuilder.technical(findings)

        elif report_type == "risk":

            return ReportBuilder.risk(findings)

        elif report_type == "management":

            return ReportBuilder.management(findings)

        elif report_type == "compliance":

            return ReportBuilder.compliance(findings)

        elif report_type == "project":

            return ReportBuilder.project(kwargs["project"], findings)

        elif report_type == "asset":

            return ReportBuilder.asset(kwargs["asset"], findings)

        elif report_type == "scan":

            return ReportBuilder.scan(kwargs["scan"], findings)

        return ReportBuilder.executive(findings)
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
