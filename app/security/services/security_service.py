"""
CloudShield Enterprise
Enterprise Security Service
"""

from datetime import datetime

from app.extensions import db

from app.models import SecurityScan
from app.models.finding import Finding
from app.models.report import Report

from app.notifications.models import Notification

from app.security.core.engine import UniversalScannerEngine


class SecurityService:
    """
    Enterprise Security Service

    Acts as bridge between

        Scanner
            ↓
        Engine
            ↓
        Database
    """

    def __init__(self):

        self.engine = UniversalScannerEngine()

    # =====================================================
    # Execute Scan
    # =====================================================

    def execute(self, user_id, asset_id, mode, category, tool, target, arguments=None):

        if arguments is None:

            arguments = []

        #
        # Execute Engine
        #

        result = self.engine.scan(
            target=target, category=category, mode=mode, tool=tool, arguments=arguments
        )

        #
        # Engine failed
        #

        if not result.get("success"):

            return {"success": False, "result": result}

        #
        # Create Scan
        #

        scan = SecurityScan(
            user_id=user_id,
            asset_id=asset_id,
            category=category,
            tool=tool or category,
            target=target,
            arguments=" ".join(arguments),
            status="Completed",
            score=result["risk"].get("score", 0),
            risk=result["risk"].get("level", "Unknown"),
            raw_output=str(result["results"]),
            started_at=datetime.utcnow(),
            completed_at=datetime.utcnow(),
            duration=0,
        )

        db.session.add(scan)

        db.session.flush()

        # =====================================================
        # Save Findings
        # =====================================================

        created_findings = []

        for item in result.get("findings", []):

            finding = Finding(
                project_id=0,
                asset_id=asset_id,
                scan_id=scan.id,
                title=item.get("title", "Finding"),
                description=item.get("description", ""),
                severity=item.get("severity", "Low"),
                category=item.get("category", category),
                evidence=str(item.get("raw", "")),
                recommendation=item.get("recommendation", ""),
                remediation=item.get("remediation", ""),
                impact=item.get("impact", ""),
            )

            db.session.add(finding)

            created_findings.append(finding)

        # =====================================================
        # Create Report
        # =====================================================

        report = Report(
            scan_id=scan.id, report_type="Enterprise", file_name=f"scan_{scan.id}.pdf"
        )

        db.session.add(report)

        # =====================================================
        # Commit
        # =====================================================

        db.session.commit()

        # =====================================================
        # Return
        # =====================================================

        return {
            "success": True,
            "scan": scan,
            "result": result,
            "findings": created_findings,
            "report": report,
        }
