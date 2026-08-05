"""
CloudShield Enterprise
Finding Service
"""

from datetime import datetime

from sqlalchemy import or_

from app.extensions import db
from app.models.finding import Finding


class FindingService:
    """
    Enterprise Finding Service

    Central business layer for Findings.
    """

    # =====================================================
    # CREATE
    # =====================================================

    def create(self, **kwargs):

        finding = Finding(**kwargs)

        db.session.add(finding)

        db.session.commit()

        return finding

    # =====================================================
    # GET
    # =====================================================

    def get(self, finding_id):

        return Finding.query.get_or_404(finding_id)

    # =====================================================
    # UPDATE
    # =====================================================

    def update(self, finding_id, **kwargs):

        finding = self.get(finding_id)

        for key, value in kwargs.items():

            if hasattr(finding, key):

                setattr(finding, key, value)

        finding.updated_at = datetime.utcnow()

        db.session.commit()

        return finding

    # =====================================================
    # DELETE
    # =====================================================

    def delete(self, finding_id):

        finding = self.get(finding_id)

        db.session.delete(finding)

        db.session.commit()

        return True

    # =====================================================
    # LIST
    # =====================================================

    def list(self):

        return Finding.query.order_by(Finding.created_at.desc()).all()

    # =====================================================
    # RECENT
    # =====================================================

    def recent(self, limit=10):

        return Finding.query.order_by(Finding.created_at.desc()).limit(limit).all()

    # =====================================================
    # SEARCH
    # =====================================================

    def search(self, keyword):

        return Finding.query.filter(
            or_(
                Finding.title.ilike(f"%{keyword}%"),
                Finding.description.ilike(f"%{keyword}%"),
                Finding.category.ilike(f"%{keyword}%"),
            )
        ).all()

    # =====================================================
    # BY PROJECT
    # =====================================================

    def by_project(self, project_id):

        return (
            Finding.query.filter_by(project_id=project_id)
            .order_by(Finding.created_at.desc())
            .all()
        )

    # =====================================================
    # BY ASSET
    # =====================================================

    def by_asset(self, asset_id):

        return (
            Finding.query.filter_by(asset_id=asset_id)
            .order_by(Finding.created_at.desc())
            .all()
        )

    # =====================================================
    # BY SCAN
    # =====================================================

    def by_scan(self, scan_id):

        return (
            Finding.query.filter_by(scan_id=scan_id)
            .order_by(Finding.created_at.desc())
            .all()
        )

    # =====================================================
    # BY SEVERITY
    # =====================================================

    def by_severity(self, severity):

        return (
            Finding.query.filter_by(severity=severity)
            .order_by(Finding.created_at.desc())
            .all()
        )

    # =====================================================
    # BY STATUS
    # =====================================================

    def by_status(self, status):

        return (
            Finding.query.filter_by(status=status)
            .order_by(Finding.created_at.desc())
            .all()
        )

    # =====================================================
    # BY CATEGORY
    # =====================================================

    def by_category(self, category):

        return (
            Finding.query.filter_by(category=category)
            .order_by(Finding.created_at.desc())
            .all()
        )

    # =====================================================
    # OPEN FINDINGS
    # =====================================================

    def open(self):

        return (
            Finding.query.filter_by(status="Open")
            .order_by(Finding.created_at.desc())
            .all()
        )

    # =====================================================
    # RESOLVED FINDINGS
    # =====================================================

    def resolved(self):

        return (
            Finding.query.filter_by(status="Resolved")
            .order_by(Finding.resolved_at.desc())
            .all()
        )

    # =====================================================
    # FALSE POSITIVES
    # =====================================================

    def false_positives(self):

        return (
            Finding.query.filter_by(false_positive=True)
            .order_by(Finding.created_at.desc())
            .all()
        )

    # =====================================================
    # CRITICAL FINDINGS
    # =====================================================

    def critical(self):

        return (
            Finding.query.filter_by(severity="Critical")
            .order_by(Finding.created_at.desc())
            .all()
        )

    # =====================================================
    # HIGH FINDINGS
    # =====================================================

    def high(self):

        return (
            Finding.query.filter_by(severity="High")
            .order_by(Finding.created_at.desc())
            .all()
        )

        # =====================================================

    # RESOLVE FINDING
    # =====================================================

    def resolve(self, finding_id):

        finding = self.get(finding_id)

        finding.status = "Resolved"

        finding.resolved_at = datetime.utcnow()

        finding.updated_at = datetime.utcnow()

        db.session.commit()

        return finding

    # =====================================================
    # REOPEN FINDING
    # =====================================================

    def reopen(self, finding_id):

        finding = self.get(finding_id)

        finding.status = "Open"

        finding.resolved_at = None

        finding.updated_at = datetime.utcnow()

        db.session.commit()

        return finding

    # =====================================================
    # MARK FALSE POSITIVE
    # =====================================================

    def mark_false_positive(self, finding_id):

        finding = self.get(finding_id)

        finding.false_positive = True

        finding.updated_at = datetime.utcnow()

        db.session.commit()

        return finding

    # =====================================================
    # RESTORE FALSE POSITIVE
    # =====================================================

    def restore(self, finding_id):

        finding = self.get(finding_id)

        finding.false_positive = False

        finding.updated_at = datetime.utcnow()

        db.session.commit()

        return finding

    # =====================================================
    # CHANGE SEVERITY
    # =====================================================

    def change_severity(self, finding_id, severity):

        finding = self.get(finding_id)

        finding.severity = severity

        finding.updated_at = datetime.utcnow()

        db.session.commit()

        return finding

    # =====================================================
    # BULK DELETE
    # =====================================================

    def bulk_delete(self, ids):

        findings = Finding.query.filter(Finding.id.in_(ids)).all()

        for finding in findings:

            db.session.delete(finding)

        db.session.commit()

        return len(findings)

    # =====================================================
    # BULK RESOLVE
    # =====================================================

    def bulk_resolve(self, ids):

        findings = Finding.query.filter(Finding.id.in_(ids)).all()

        now = datetime.utcnow()

        for finding in findings:

            finding.status = "Resolved"

            finding.resolved_at = now

            finding.updated_at = now

        db.session.commit()

        return len(findings)

    # =====================================================
    # BULK REOPEN
    # =====================================================

    def bulk_reopen(self, ids):

        findings = Finding.query.filter(Finding.id.in_(ids)).all()

        now = datetime.utcnow()

        for finding in findings:

            finding.status = "Open"

            finding.resolved_at = None

            finding.updated_at = now

        db.session.commit()

        return len(findings)

    # =====================================================
    # BULK FALSE POSITIVE
    # =====================================================

    def bulk_false_positive(self, ids):

        findings = Finding.query.filter(Finding.id.in_(ids)).all()

        now = datetime.utcnow()

        for finding in findings:

            finding.false_positive = True

            finding.updated_at = now

        db.session.commit()

        return len(findings)

    # =====================================================
    # BULK CHANGE SEVERITY
    # =====================================================

    def bulk_change_severity(self, ids, severity):

        findings = Finding.query.filter(Finding.id.in_(ids)).all()

        now = datetime.utcnow()

        for finding in findings:

            finding.severity = severity

            finding.updated_at = now

        db.session.commit()

        return len(findings)

        # =====================================================

    # TOTAL FINDINGS
    # =====================================================

    def total(self):

        return Finding.query.count()

    # =====================================================
    # DASHBOARD SUMMARY
    # =====================================================

    def summary(self):

        return {
            "total": Finding.query.count(),
            "critical": Finding.query.filter_by(severity="Critical").count(),
            "high": Finding.query.filter_by(severity="High").count(),
            "medium": Finding.query.filter_by(severity="Medium").count(),
            "low": Finding.query.filter_by(severity="Low").count(),
            "info": Finding.query.filter_by(severity="Info").count(),
            "open": Finding.query.filter_by(status="Open").count(),
            "resolved": Finding.query.filter_by(status="Resolved").count(),
            "false_positive": Finding.query.filter_by(false_positive=True).count(),
        }

    # =====================================================
    # DASHBOARD
    # =====================================================

    def dashboard(self):

        return {
            "summary": self.summary(),
            "recent": self.recent(10),
            "critical": self.critical(),
            "high": self.high(),
            "open": self.open(),
            "resolved": self.resolved(),
        }

    # =====================================================
    # RISK SCORE
    # =====================================================

    def risk_score(self):

        score = 0

        weights = {"Critical": 10, "High": 7, "Medium": 5, "Low": 2, "Info": 0}

        findings = Finding.query.filter_by(status="Open").all()

        for finding in findings:

            score += weights.get(finding.severity, 0)

        return score

    # =====================================================
    # TOP ASSETS
    # =====================================================

    def top_assets(self, limit=10):

        from sqlalchemy import func

        return (
            db.session.query(Finding.asset_id, func.count(Finding.id))
            .group_by(Finding.asset_id)
            .order_by(func.count(Finding.id).desc())
            .limit(limit)
            .all()
        )

    # =====================================================
    # TOP PROJECTS
    # =====================================================

    def top_projects(self, limit=10):

        from sqlalchemy import func

        return (
            db.session.query(Finding.project_id, func.count(Finding.id))
            .group_by(Finding.project_id)
            .order_by(func.count(Finding.id).desc())
            .limit(limit)
            .all()
        )

    # =====================================================
    # LATEST FINDINGS
    # =====================================================

    def latest(self, limit=20):

        return Finding.query.order_by(Finding.created_at.desc()).limit(limit).all()

    # =====================================================
    # EXISTS
    # =====================================================

    def exists(self, finding_id):

        return Finding.query.filter_by(id=finding_id).first() is not None
