"""
CloudShield Enterprise
Findings Service
"""

import csv
import io
import json
from sqlalchemy import or_
from app.models.finding import Finding
from sqlalchemy import or_
from app.extensions import db


class FindingsService:

    @staticmethod
    def all():

        return Finding.query.order_by(
            Finding.severity.desc(), Finding.created_at.desc()
        ).all()

    @staticmethod
    def critical():

        return Finding.query.filter_by(severity="Critical").all()

    @staticmethod
    def high():

        return Finding.query.filter_by(severity="High").all()

    @staticmethod
    def medium():

        return Finding.query.filter_by(severity="Medium").all()

    @staticmethod
    def low():

        return Finding.query.filter_by(severity="Low").all()

    @staticmethod
    def open():

        return Finding.query.filter_by(status="Open").all()

    @staticmethod
    def resolved():

        return Finding.query.filter_by(status="Resolved").all()

    @staticmethod
    def get(finding_id):

        from app.models.finding import Finding

        return Finding.query.get_or_404(finding_id)

    @staticmethod
    def update(finding_id, status, recommendation):

        from app.models.finding import Finding
        from app.extensions import db

        finding = Finding.query.get_or_404(finding_id)

        finding.status = status

        finding.recommendation = recommendation

        db.session.commit()

        return finding

    @staticmethod
    def latest(limit=10):
        """
        Return the most recent findings.
        """
        return Finding.query.order_by(Finding.created_at.desc()).limit(limit).all()

    @staticmethod
    def search(keyword):
        """
        Search findings by title, description or category.
        """
        if not keyword:
            return FindingsService.all()

        return (
            Finding.query.filter(
                or_(
                    Finding.title.ilike(f"%{keyword}%"),
                    Finding.description.ilike(f"%{keyword}%"),
                    Finding.category.ilike(f"%{keyword}%"),
                )
            )
            .order_by(Finding.created_at.desc())
            .all()
        )

    @staticmethod
    def filter_findings(search=None, severity=None, status=None, category=None):
        """
        Enterprise search and filtering.
        """

        query = Finding.query

        if search:
            query = query.filter(
                or_(
                    Finding.title.ilike(f"%{search}%"),
                    Finding.description.ilike(f"%{search}%"),
                    Finding.category.ilike(f"%{search}%"),
                )
            )

        if severity:
            query = query.filter(Finding.severity == severity)

        if status:
            query = query.filter(Finding.status == status)

        if category:
            query = query.filter(Finding.category.ilike(f"%{category}%"))

        return query.order_by(Finding.created_at.desc()).all()

    @staticmethod
    def related(finding_id, limit=10):
        """
        Return findings related to the given finding
        based on project, asset or category.
        """
        finding = Finding.query.get_or_404(finding_id)

        return (
            Finding.query.filter(
                Finding.id != finding.id,
                or_(
                    Finding.project_id == finding.project_id,
                    Finding.asset_id == finding.asset_id,
                    Finding.category == finding.category,
                ),
            )
            .limit(limit)
            .all()
        )

    @staticmethod
    def resolve(finding_id):
        """
        Mark a finding as resolved.
        """
        from datetime import datetime

        finding = Finding.query.get_or_404(finding_id)

        finding.status = "Resolved"
        finding.resolved_at = datetime.utcnow()

        db.session.commit()

        return finding

    @staticmethod
    def reopen(finding_id):
        """
        Reopen a resolved finding.
        """
        finding = Finding.query.get_or_404(finding_id)

        finding.status = "Open"
        finding.resolved_at = None

        db.session.commit()

        return finding

    @staticmethod
    def mark_false_positive(finding_id):
        """
        Mark a finding as false positive.
        """
        finding = Finding.query.get_or_404(finding_id)

        finding.false_positive = True

        db.session.commit()

        return finding

    @staticmethod
    def unmark_false_positive(finding_id):
        """
        Remove false positive flag.
        """
        finding = Finding.query.get_or_404(finding_id)

        finding.false_positive = False

        db.session.commit()

        return finding

    @staticmethod
    def delete(finding_id):
        """
        Delete a finding.
        """
        finding = Finding.query.get_or_404(finding_id)

        db.session.delete(finding)

        db.session.commit()

        return True

    @staticmethod
    def counts():
        """
        Return severity counts.
        """
        return {
            "critical": Finding.query.filter_by(severity="Critical").count(),
            "high": Finding.query.filter_by(severity="High").count(),
            "medium": Finding.query.filter_by(severity="Medium").count(),
            "low": Finding.query.filter_by(severity="Low").count(),
            "open": Finding.query.filter_by(status="Open").count(),
            "resolved": Finding.query.filter_by(status="Resolved").count(),
            "total": Finding.query.count(),
        }

    @staticmethod
    def top_assets(limit=5):
        """
        Assets with the highest number of findings.
        """
        return (
            db.session.query(Finding.asset_id, db.func.count(Finding.id).label("count"))
            .group_by(Finding.asset_id)
            .order_by(db.func.count(Finding.id).desc())
            .limit(limit)
            .all()
        )

    @staticmethod
    def top_assets(limit=5):
        """
        Assets with the highest number of findings.
        """

        results = (
            db.session.query(Finding.asset_id, db.func.count(Finding.id).label("count"))
            .group_by(Finding.asset_id)
            .order_by(db.func.count(Finding.id).desc())
            .limit(limit)
            .all()
        )

        return [{"asset_id": row.asset_id, "count": row.count} for row in results]

    @staticmethod
    def top_projects(limit=5):
        """
        Projects with the highest number of findings.
        """

        results = (
            db.session.query(
                Finding.project_id, db.func.count(Finding.id).label("count")
            )
            .group_by(Finding.project_id)
            .order_by(db.func.count(Finding.id).desc())
            .limit(limit)
            .all()
        )

        return [{"project_id": row.project_id, "count": row.count} for row in results]

    @staticmethod
    def risk_score():
        """
        Calculate enterprise risk score.
        """
        weights = {"Critical": 10, "High": 7, "Medium": 4, "Low": 2, "Info": 0}

        score = 0

        findings = Finding.query.all()

        for finding in findings:

            score += weights.get(finding.severity, 0)

        return score

    @staticmethod
    def dashboard():
        """
        Complete dashboard data.
        """
        counts = FindingsService.counts()

        findings = Finding.query.all()

        if findings:

            average_cvss = round(sum(f.cvss or 0 for f in findings) / len(findings), 1)

            maximum_cvss = max(f.cvss or 0 for f in findings)

        else:

            average_cvss = 0

            maximum_cvss = 0

        return {
            "summary": counts,
            "risk_score": FindingsService.risk_score(),
            "cvss": {"average": average_cvss, "maximum": maximum_cvss},
            "top_assets": FindingsService.top_assets(),
            "top_projects": FindingsService.top_projects(),
        }

    @staticmethod
    def export_csv():
        """
        Export all findings as CSV.
        """
        output = io.StringIO()

        writer = csv.writer(output)

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
                "Created",
            ]
        )

        findings = Finding.query.order_by(Finding.created_at.desc()).all()

        for finding in findings:

            writer.writerow(
                [
                    finding.id,
                    finding.title,
                    finding.severity,
                    finding.cvss,
                    finding.category,
                    finding.status,
                    finding.project.name if finding.project else "",
                    finding.asset.name if finding.asset else "",
                    finding.created_at.strftime("%Y-%m-%d %H:%M"),
                ]
            )

        return output.getvalue()

    @staticmethod
    def export_json():
        """
        Export all findings as JSON.
        """

        findings = Finding.query.order_by(Finding.created_at.desc()).all()

        data = []

        for finding in findings:

            data.append(
                {
                    "id": finding.id,
                    "title": finding.title,
                    "severity": finding.severity,
                    "cvss": finding.cvss,
                    "category": finding.category,
                    "status": finding.status,
                    "project": finding.project.name if finding.project else None,
                    "asset": finding.asset.name if finding.asset else None,
                    "description": finding.description,
                    "recommendation": finding.recommendation,
                    "created_at": finding.created_at.isoformat(),
                }
            )

        return json.dumps(data, indent=4)

    @staticmethod
    def filter_findings(search=None, severity=None, status=None, category=None):
        """
        Enterprise search and filtering.
        """

        query = Finding.query

        # -------------------------
        # Search
        # -------------------------

        if search:

            query = query.filter(
                or_(
                    Finding.title.ilike(f"%{search}%"),
                    Finding.description.ilike(f"%{search}%"),
                    Finding.category.ilike(f"%{search}%"),
                )
            )

        # -------------------------
        # Severity
        # -------------------------

        if severity:

            query = query.filter(Finding.severity == severity)

        # -------------------------
        # Status
        # -------------------------

        if status:

            query = query.filter(Finding.status == status)

        # -------------------------
        # Category
        # -------------------------

        if category:

            query = query.filter(Finding.category.ilike(f"%{category}%"))

        return query.order_by(Finding.created_at.desc())

    @staticmethod
    def sort(query, sort_by="created_at", order="desc"):

        columns = {
            "title": Finding.title,
            "severity": Finding.severity,
            "cvss": Finding.cvss,
            "status": Finding.status,
            "created_at": Finding.created_at,
        }

        column = columns.get(sort_by, Finding.created_at)

        if order == "asc":
            return query.order_by(column.asc())

        return query.order_by(column.desc())

    @staticmethod
    def bulk_delete(ids):

        if not ids:

            return

        Finding.query.filter(Finding.id.in_(ids)).delete(synchronize_session=False)

        db.session.commit()

    @staticmethod
    def bulk_resolve(ids):

        if not ids:

            return

        Finding.query.filter(Finding.id.in_(ids)).update(
            {Finding.status: "Resolved"}, synchronize_session=False
        )

        db.session.commit()

    @staticmethod
    def export_selected_csv(ids):

        import csv
        import io

        output = io.StringIO()

        writer = csv.writer(output)

        writer.writerow(["ID", "Title", "Severity", "CVSS", "Category", "Status"])

        findings = Finding.query.filter(Finding.id.in_(ids)).all()

        for finding in findings:

            writer.writerow(
                [
                    finding.id,
                    finding.title,
                    finding.severity,
                    finding.cvss,
                    finding.category,
                    finding.status,
                ]
            )

        return output.getvalue()

    @staticmethod
    def export_selected_json(ids):

        import json

        findings = Finding.query.filter(Finding.id.in_(ids)).all()

        data = []

        for finding in findings:

            data.append(
                {
                    "id": finding.id,
                    "title": finding.title,
                    "severity": finding.severity,
                    "cvss": finding.cvss,
                    "category": finding.category,
                    "status": finding.status,
                }
            )

        return json.dumps(data, indent=4)
