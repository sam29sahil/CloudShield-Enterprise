"""
CloudShield Enterprise
Finding Export Engine
"""

import csv
import io
import json

from app.models.finding import Finding


class FindingExporter:
    """
    Enterprise Finding Export Engine
    """

    # =====================================================
    # SERIALIZE
    # =====================================================

    @staticmethod
    def serialize(finding):

        return {
<<<<<<< HEAD
            "id": finding.id,
            "title": finding.title,
            "description": finding.description,
            "severity": finding.severity,
            "cvss": finding.cvss,
            "category": finding.category,
            "status": finding.status,
            "false_positive": finding.false_positive,
            "project_id": finding.project_id,
            "asset_id": finding.asset_id,
            "scan_id": finding.scan_id,
            "recommendation": finding.recommendation,
            "evidence": finding.evidence,
            "created_at": (
                finding.created_at.isoformat() if finding.created_at else None
            ),
            "updated_at": (
                finding.updated_at.isoformat() if finding.updated_at else None
            ),
            "resolved_at": (
                finding.resolved_at.isoformat() if finding.resolved_at else None
            ),
=======

            "id": finding.id,

            "title": finding.title,

            "description": finding.description,

            "severity": finding.severity,

            "cvss": finding.cvss,

            "category": finding.category,

            "status": finding.status,

            "false_positive": finding.false_positive,

            "project_id": finding.project_id,

            "asset_id": finding.asset_id,

            "scan_id": finding.scan_id,

            "recommendation": finding.recommendation,

            "evidence": finding.evidence,

            "created_at": (
                finding.created_at.isoformat()
                if finding.created_at else None
            ),

            "updated_at": (
                finding.updated_at.isoformat()
                if finding.updated_at else None
            ),

            "resolved_at": (
                finding.resolved_at.isoformat()
                if finding.resolved_at else None
            )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # SERIALIZE MANY
    # =====================================================

    @classmethod
    def serialize_many(cls, findings):

<<<<<<< HEAD
        return [cls.serialize(finding) for finding in findings]

        # =====================================================

=======
        return [

            cls.serialize(finding)

            for finding in findings

        ]

        # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # JSON EXPORT
    # =====================================================

    @classmethod
    def export_json(cls, findings):

<<<<<<< HEAD
        return json.dumps(cls.serialize_many(findings), indent=4, default=str)
=======
        return json.dumps(

            cls.serialize_many(findings),

            indent=4,

            default=str

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # SINGLE JSON
    # =====================================================

    @classmethod
    def export_single_json(cls, finding):

<<<<<<< HEAD
        return json.dumps(cls.serialize(finding), indent=4, default=str)
=======
        return json.dumps(

            cls.serialize(finding),

            indent=4,

            default=str

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # CSV EXPORT
    # =====================================================

    @classmethod
    def export_csv(cls, findings):

        output = io.StringIO()

        writer = csv.writer(output)

<<<<<<< HEAD
        writer.writerow(
            [
                "ID",
                "Title",
                "Severity",
                "CVSS",
                "Category",
                "Status",
                "Project",
                "Asset",
                "Scan",
                "False Positive",
                "Recommendation",
                "Created",
            ]
        )

        for finding in findings:

            writer.writerow(
                [
                    finding.id,
                    finding.title,
                    finding.severity,
                    finding.cvss,
                    finding.category,
                    finding.status,
                    finding.project_id,
                    finding.asset_id,
                    finding.scan_id,
                    finding.false_positive,
                    finding.recommendation,
                    finding.created_at,
                ]
            )
=======
        writer.writerow([

            "ID",

            "Title",

            "Severity",

            "CVSS",

            "Category",

            "Status",

            "Project",

            "Asset",

            "Scan",

            "False Positive",

            "Recommendation",

            "Created"

        ])

        for finding in findings:

            writer.writerow([

                finding.id,

                finding.title,

                finding.severity,

                finding.cvss,

                finding.category,

                finding.status,

                finding.project_id,

                finding.asset_id,

                finding.scan_id,

                finding.false_positive,

                finding.recommendation,

                finding.created_at

            ])
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return output.getvalue()

    # =====================================================
    # SINGLE CSV
    # =====================================================

    @classmethod
    def export_single_csv(cls, finding):

<<<<<<< HEAD
        return cls.export_csv([finding])

        # =====================================================

=======
        return cls.export_csv(

            [finding]

        )
    
        # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # EXECUTIVE REPORT
    # =====================================================

    @classmethod
    def executive_report(cls, findings):

<<<<<<< HEAD
        critical = sum(1 for f in findings if f.severity == "Critical")

        high = sum(1 for f in findings if f.severity == "High")

        medium = sum(1 for f in findings if f.severity == "Medium")

        low = sum(1 for f in findings if f.severity == "Low")

        info = sum(1 for f in findings if f.severity == "Info")

        return {
            "summary": {
                "total": len(findings),
                "critical": critical,
                "high": high,
                "medium": medium,
                "low": low,
                "info": info,
            },
            "findings": cls.serialize_many(findings),
=======
        critical = sum(
            1 for f in findings
            if f.severity == "Critical"
        )

        high = sum(
            1 for f in findings
            if f.severity == "High"
        )

        medium = sum(
            1 for f in findings
            if f.severity == "Medium"
        )

        low = sum(
            1 for f in findings
            if f.severity == "Low"
        )

        info = sum(
            1 for f in findings
            if f.severity == "Info"
        )

        return {

            "summary": {

                "total": len(findings),

                "critical": critical,

                "high": high,

                "medium": medium,

                "low": low,

                "info": info

            },

            "findings": cls.serialize_many(findings)

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # TECHNICAL REPORT
    # =====================================================

    @classmethod
    def technical_report(cls, findings):

<<<<<<< HEAD
        return {"total": len(findings), "findings": cls.serialize_many(findings)}
=======
        return {

            "total": len(findings),

            "findings": cls.serialize_many(findings)

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # =====================================================
    # PROJECT REPORT
    # =====================================================

    @classmethod
    def project_report(cls, project_id, findings):

        return {
<<<<<<< HEAD
            "project_id": project_id,
            "total": len(findings),
            "findings": cls.serialize_many(findings),
=======

            "project_id": project_id,

            "total": len(findings),

            "findings": cls.serialize_many(findings)

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # ASSET REPORT
    # =====================================================

    @classmethod
    def asset_report(cls, asset_id, findings):

        return {
<<<<<<< HEAD
            "asset_id": asset_id,
            "total": len(findings),
            "findings": cls.serialize_many(findings),
=======

            "asset_id": asset_id,

            "total": len(findings),

            "findings": cls.serialize_many(findings)

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # SCAN REPORT
    # =====================================================

    @classmethod
    def scan_report(cls, scan_id, findings):

        return {
<<<<<<< HEAD
            "scan_id": scan_id,
            "total": len(findings),
            "findings": cls.serialize_many(findings),
        }
        # =====================================================

=======

            "scan_id": scan_id,

            "total": len(findings),

            "findings": cls.serialize_many(findings)

        }
        # =====================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # FILTER BY PROJECT
    # =====================================================

    @classmethod
    def by_project(cls, findings, project_id):

<<<<<<< HEAD
        filtered = [finding for finding in findings if finding.project_id == project_id]
=======
        filtered = [

            finding

            for finding in findings

            if finding.project_id == project_id

        ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return cls.serialize_many(filtered)

    # =====================================================
    # FILTER BY ASSET
    # =====================================================

    @classmethod
    def by_asset(cls, findings, asset_id):

<<<<<<< HEAD
        filtered = [finding for finding in findings if finding.asset_id == asset_id]
=======
        filtered = [

            finding

            for finding in findings

            if finding.asset_id == asset_id

        ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return cls.serialize_many(filtered)

    # =====================================================
    # FILTER BY SCAN
    # =====================================================

    @classmethod
    def by_scan(cls, findings, scan_id):

<<<<<<< HEAD
        filtered = [finding for finding in findings if finding.scan_id == scan_id]
=======
        filtered = [

            finding

            for finding in findings

            if finding.scan_id == scan_id

        ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return cls.serialize_many(filtered)

    # =====================================================
    # FILTER BY SEVERITY
    # =====================================================

    @classmethod
    def by_severity(cls, findings, severity):

<<<<<<< HEAD
        filtered = [finding for finding in findings if finding.severity == severity]
=======
        filtered = [

            finding

            for finding in findings

            if finding.severity == severity

        ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return cls.serialize_many(filtered)

    # =====================================================
    # FILTER BY STATUS
    # =====================================================

    @classmethod
    def by_status(cls, findings, status):

<<<<<<< HEAD
        filtered = [finding for finding in findings if finding.status == status]
=======
        filtered = [

            finding

            for finding in findings

            if finding.status == status

        ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return cls.serialize_many(filtered)

    # =====================================================
    # EXPORT SUMMARY
    # =====================================================

    @classmethod
    def summary(cls, findings):

        return {
<<<<<<< HEAD
            "total": len(findings),
            "critical": sum(1 for f in findings if f.severity == "Critical"),
            "high": sum(1 for f in findings if f.severity == "High"),
            "medium": sum(1 for f in findings if f.severity == "Medium"),
            "low": sum(1 for f in findings if f.severity == "Low"),
            "info": sum(1 for f in findings if f.severity == "Info"),
            "resolved": sum(1 for f in findings if f.status == "Resolved"),
            "open": sum(1 for f in findings if f.status == "Open"),
=======

            "total": len(findings),

            "critical": sum(
                1 for f in findings
                if f.severity == "Critical"
            ),

            "high": sum(
                1 for f in findings
                if f.severity == "High"
            ),

            "medium": sum(
                1 for f in findings
                if f.severity == "Medium"
            ),

            "low": sum(
                1 for f in findings
                if f.severity == "Low"
            ),

            "info": sum(
                1 for f in findings
                if f.severity == "Info"
            ),

            "resolved": sum(
                1 for f in findings
                if f.status == "Resolved"
            ),

            "open": sum(
                1 for f in findings
                if f.status == "Open"
            )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # =====================================================
    # EXPORT PACKAGE
    # =====================================================

    @classmethod
    def package(cls, findings):

        return {
<<<<<<< HEAD
            "summary": cls.summary(findings),
            "json": cls.export_json(findings),
            "csv": cls.export_csv(findings),
            "technical": cls.technical_report(findings),
            "executive": cls.executive_report(findings),
        }
=======

            "summary": cls.summary(findings),

            "json": cls.export_json(findings),

            "csv": cls.export_csv(findings),

            "technical": cls.technical_report(findings),

            "executive": cls.executive_report(findings)

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
