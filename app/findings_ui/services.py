"""
CloudShield Enterprise
Findings Service
"""
<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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

<<<<<<< HEAD
        return Finding.query.order_by(
            Finding.severity.desc(), Finding.created_at.desc()
        ).all()
=======
        return (

            Finding.query

            .order_by(

                Finding.severity.desc(),

                Finding.created_at.desc()

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def critical():

<<<<<<< HEAD
        return Finding.query.filter_by(severity="Critical").all()
=======
        return (

            Finding.query

            .filter_by(

                severity="Critical"

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def high():

<<<<<<< HEAD
        return Finding.query.filter_by(severity="High").all()
=======
        return (

            Finding.query

            .filter_by(

                severity="High"

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def medium():

<<<<<<< HEAD
        return Finding.query.filter_by(severity="Medium").all()
=======
        return (

            Finding.query

            .filter_by(

                severity="Medium"

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def low():

<<<<<<< HEAD
        return Finding.query.filter_by(severity="Low").all()
=======
        return (

            Finding.query

            .filter_by(

                severity="Low"

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def open():

<<<<<<< HEAD
        return Finding.query.filter_by(status="Open").all()
=======
        return (

            Finding.query

            .filter_by(

                status="Open"

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def resolved():

<<<<<<< HEAD
        return Finding.query.filter_by(status="Resolved").all()

=======
        return (

            Finding.query

            .filter_by(

                status="Resolved"

            )

            .all()

        )
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    @staticmethod
    def get(finding_id):

        from app.models.finding import Finding

        return Finding.query.get_or_404(finding_id)

<<<<<<< HEAD
    @staticmethod
    def update(finding_id, status, recommendation):
=======

    @staticmethod
    def update(

        finding_id,

        status,

        recommendation

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        from app.models.finding import Finding
        from app.extensions import db

<<<<<<< HEAD
        finding = Finding.query.get_or_404(finding_id)
=======
        finding = Finding.query.get_or_404(

            finding_id

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        finding.status = status

        finding.recommendation = recommendation

        db.session.commit()

        return finding
<<<<<<< HEAD

=======
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    @staticmethod
    def latest(limit=10):
        """
        Return the most recent findings.
        """
<<<<<<< HEAD
        return Finding.query.order_by(Finding.created_at.desc()).limit(limit).all()
=======
        return (
            Finding.query
            .order_by(Finding.created_at.desc())
            .limit(limit)
            .all()
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def search(keyword):
        """
        Search findings by title, description or category.
        """
        if not keyword:
            return FindingsService.all()

        return (
<<<<<<< HEAD
            Finding.query.filter(
                or_(
                    Finding.title.ilike(f"%{keyword}%"),
                    Finding.description.ilike(f"%{keyword}%"),
                    Finding.category.ilike(f"%{keyword}%"),
=======
            Finding.query
            .filter(
                or_(
                    Finding.title.ilike(f"%{keyword}%"),
                    Finding.description.ilike(f"%{keyword}%"),
                    Finding.category.ilike(f"%{keyword}%")
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                )
            )
            .order_by(Finding.created_at.desc())
            .all()
        )
<<<<<<< HEAD

    @staticmethod
    def filter_findings(search=None, severity=None, status=None, category=None):
=======
    
    @staticmethod
    def filter_findings(
        search=None,
        severity=None,
        status=None,
        category=None
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        """
        Enterprise search and filtering.
        """

        query = Finding.query

        if search:
            query = query.filter(
                or_(
                    Finding.title.ilike(f"%{search}%"),
                    Finding.description.ilike(f"%{search}%"),
<<<<<<< HEAD
                    Finding.category.ilike(f"%{search}%"),
=======
                    Finding.category.ilike(f"%{search}%")
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                )
            )

        if severity:
<<<<<<< HEAD
            query = query.filter(Finding.severity == severity)

        if status:
            query = query.filter(Finding.status == status)

        if category:
            query = query.filter(Finding.category.ilike(f"%{category}%"))

        return query.order_by(Finding.created_at.desc()).all()
=======
            query = query.filter(
                Finding.severity == severity
            )

        if status:
            query = query.filter(
                Finding.status == status
            )

        if category:
            query = query.filter(
                Finding.category.ilike(f"%{category}%")
            )

        return (
            query
            .order_by(Finding.created_at.desc())
            .all()
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def related(finding_id, limit=10):
        """
        Return findings related to the given finding
        based on project, asset or category.
        """
        finding = Finding.query.get_or_404(finding_id)

        return (
<<<<<<< HEAD
            Finding.query.filter(
=======
            Finding.query
            .filter(
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
                Finding.id != finding.id,
                or_(
                    Finding.project_id == finding.project_id,
                    Finding.asset_id == finding.asset_id,
<<<<<<< HEAD
                    Finding.category == finding.category,
                ),
=======
                    Finding.category == finding.category
                )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )
            .limit(limit)
            .all()
        )
<<<<<<< HEAD

=======
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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
<<<<<<< HEAD

=======
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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
<<<<<<< HEAD
            "total": Finding.query.count(),
=======
            "total": Finding.query.count()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    @staticmethod
    def top_assets(limit=5):
        """
        Assets with the highest number of findings.
        """
        return (
<<<<<<< HEAD
            db.session.query(Finding.asset_id, db.func.count(Finding.id).label("count"))
=======
            db.session.query(
                Finding.asset_id,
                db.func.count(Finding.id).label("count")
            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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
<<<<<<< HEAD
            db.session.query(Finding.asset_id, db.func.count(Finding.id).label("count"))
=======
            db.session.query(
                Finding.asset_id,
                db.func.count(Finding.id).label("count")
            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            .group_by(Finding.asset_id)
            .order_by(db.func.count(Finding.id).desc())
            .limit(limit)
            .all()
        )

<<<<<<< HEAD
        return [{"asset_id": row.asset_id, "count": row.count} for row in results]
=======
        return [
            {
                "asset_id": row.asset_id,
                "count": row.count
            }
            for row in results
        ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def top_projects(limit=5):
        """
        Projects with the highest number of findings.
        """

        results = (
            db.session.query(
<<<<<<< HEAD
                Finding.project_id, db.func.count(Finding.id).label("count")
=======
                Finding.project_id,
                db.func.count(Finding.id).label("count")
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )
            .group_by(Finding.project_id)
            .order_by(db.func.count(Finding.id).desc())
            .limit(limit)
            .all()
        )

<<<<<<< HEAD
        return [{"project_id": row.project_id, "count": row.count} for row in results]
=======
        return [
            {
                "project_id": row.project_id,
                "count": row.count
            }
            for row in results
        ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def risk_score():
        """
        Calculate enterprise risk score.
        """
<<<<<<< HEAD
        weights = {"Critical": 10, "High": 7, "Medium": 4, "Low": 2, "Info": 0}
=======
        weights = {
            "Critical": 10,
            "High": 7,
            "Medium": 4,
            "Low": 2,
            "Info": 0
        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        score = 0

        findings = Finding.query.all()

        for finding in findings:

<<<<<<< HEAD
            score += weights.get(finding.severity, 0)

        return score

=======
            score += weights.get(

                finding.severity,

                0

            )

        return score
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    @staticmethod
    def dashboard():
        """
        Complete dashboard data.
        """
        counts = FindingsService.counts()

        findings = Finding.query.all()

        if findings:

<<<<<<< HEAD
            average_cvss = round(sum(f.cvss or 0 for f in findings) / len(findings), 1)

            maximum_cvss = max(f.cvss or 0 for f in findings)
=======
            average_cvss = round(

                sum(f.cvss or 0 for f in findings)

                / len(findings),

                1

            )

            maximum_cvss = max(

                f.cvss or 0

                for f in findings

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        else:

            average_cvss = 0

            maximum_cvss = 0

        return {
<<<<<<< HEAD
            "summary": counts,
            "risk_score": FindingsService.risk_score(),
            "cvss": {"average": average_cvss, "maximum": maximum_cvss},
            "top_assets": FindingsService.top_assets(),
            "top_projects": FindingsService.top_projects(),
        }

=======

            "summary": counts,

            "risk_score": FindingsService.risk_score(),

            "cvss": {

                "average": average_cvss,

                "maximum": maximum_cvss

            },

            "top_assets": FindingsService.top_assets(),

            "top_projects": FindingsService.top_projects()

        }
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    @staticmethod
    def export_csv():
        """
        Export all findings as CSV.
        """
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
            "Created"
        ])

        findings = Finding.query.order_by(
            Finding.created_at.desc()
        ).all()

        for finding in findings:

            writer.writerow([

                finding.id,

                finding.title,

                finding.severity,

                finding.cvss,

                finding.category,

                finding.status,

                finding.project.name if finding.project else "",

                finding.asset.name if finding.asset else "",

                finding.created_at.strftime(
                    "%Y-%m-%d %H:%M"
                )

            ])
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return output.getvalue()

    @staticmethod
    def export_json():
        """
        Export all findings as JSON.
        """

<<<<<<< HEAD
        findings = Finding.query.order_by(Finding.created_at.desc()).all()
=======
        findings = Finding.query.order_by(
            Finding.created_at.desc()
        ).all()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        data = []

        for finding in findings:

<<<<<<< HEAD
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
=======
            data.append({

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

                "created_at": finding.created_at.isoformat()

            })

        return json.dumps(

            data,

            indent=4

        )
    @staticmethod
    def filter_findings(
        search=None,
        severity=None,
        status=None,
        category=None
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        """
        Enterprise search and filtering.
        """

        query = Finding.query

        # -------------------------
        # Search
        # -------------------------

        if search:

            query = query.filter(
<<<<<<< HEAD
                or_(
                    Finding.title.ilike(f"%{search}%"),
                    Finding.description.ilike(f"%{search}%"),
                    Finding.category.ilike(f"%{search}%"),
                )
=======

                or_(

                    Finding.title.ilike(f"%{search}%"),

                    Finding.description.ilike(f"%{search}%"),

                    Finding.category.ilike(f"%{search}%")

                )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )

        # -------------------------
        # Severity
        # -------------------------

        if severity:

<<<<<<< HEAD
            query = query.filter(Finding.severity == severity)
=======
            query = query.filter(

                Finding.severity == severity

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # -------------------------
        # Status
        # -------------------------

        if status:

<<<<<<< HEAD
            query = query.filter(Finding.status == status)
=======
            query = query.filter(

                Finding.status == status

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # -------------------------
        # Category
        # -------------------------

        if category:

<<<<<<< HEAD
            query = query.filter(Finding.category.ilike(f"%{category}%"))

        return query.order_by(Finding.created_at.desc())

=======
            query = query.filter(

                Finding.category.ilike(

                    f"%{category}%"

                )

            )

        return (

            query

            .order_by(

                Finding.created_at.desc()

            )
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    @staticmethod
    def sort(query, sort_by="created_at", order="desc"):

        columns = {
            "title": Finding.title,
            "severity": Finding.severity,
            "cvss": Finding.cvss,
            "status": Finding.status,
<<<<<<< HEAD
            "created_at": Finding.created_at,
=======
            "created_at": Finding.created_at
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

        column = columns.get(sort_by, Finding.created_at)

        if order == "asc":
            return query.order_by(column.asc())

        return query.order_by(column.desc())
<<<<<<< HEAD

=======
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    @staticmethod
    def bulk_delete(ids):

        if not ids:

            return

<<<<<<< HEAD
        Finding.query.filter(Finding.id.in_(ids)).delete(synchronize_session=False)
=======
        Finding.query.filter(

            Finding.id.in_(ids)

        ).delete(

            synchronize_session=False

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        db.session.commit()

    @staticmethod
    def bulk_resolve(ids):

        if not ids:

            return

<<<<<<< HEAD
        Finding.query.filter(Finding.id.in_(ids)).update(
            {Finding.status: "Resolved"}, synchronize_session=False
        )

        db.session.commit()
=======
        Finding.query.filter(

            Finding.id.in_(ids)

        ).update(

            {

                Finding.status: "Resolved"

            },

            synchronize_session=False

        )

        db.session.commit()    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def export_selected_csv(ids):

        import csv
        import io

        output = io.StringIO()

        writer = csv.writer(output)

<<<<<<< HEAD
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

=======
        writer.writerow([
            "ID",
            "Title",
            "Severity",
            "CVSS",
            "Category",
            "Status"
        ])

        findings = Finding.query.filter(
        Finding.id.in_(ids)
        ).all()

        for finding in findings:

            writer.writerow([
                finding.id,
                finding.title,
                finding.severity,
                finding.cvss,
                finding.category,
                finding.status
            ])

        return output.getvalue()    
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    @staticmethod
    def export_selected_json(ids):

        import json

<<<<<<< HEAD
        findings = Finding.query.filter(Finding.id.in_(ids)).all()
=======
        findings = Finding.query.filter(
            Finding.id.in_(ids)
        ).all()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        data = []

        for finding in findings:

<<<<<<< HEAD
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
=======
            data.append({

                "id": finding.id,
                "title": finding.title,
                "severity": finding.severity,
                "cvss": finding.cvss,
               "category": finding.category,
                "status": finding.status

            })

        return json.dumps(
            data,
            indent=4
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
