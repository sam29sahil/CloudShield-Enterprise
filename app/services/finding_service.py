"""
CloudShield Enterprise
Finding Service
"""

from app.extensions import db
from app.models.finding import Finding


class FindingService:

    def create(
<<<<<<< HEAD
        self, scan_id, title, severity, category, source, description, recommendation
    ):

        finding = Finding(
            scan_id=scan_id,
            title=title,
            severity=severity,
            category=category,
            source=source,
            description=description,
            recommendation=recommendation,
=======

        self,

        scan_id,

        title,

        severity,

        category,

        source,

        description,

        recommendation

    ):

        finding = Finding(

            scan_id=scan_id,

            title=title,

            severity=severity,

            category=category,

            source=source,

            description=description,

            recommendation=recommendation

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        db.session.add(finding)

        db.session.commit()

        return finding

    def all(self):

        return Finding.query.all()

    def scan_findings(self, scan_id):

<<<<<<< HEAD
        return Finding.query.filter_by(scan_id=scan_id).all()

    def severity(self, level):

        return Finding.query.filter_by(severity=level).all()
=======
        return Finding.query.filter_by(

            scan_id=scan_id

        ).all()

    def severity(self, level):

        return Finding.query.filter_by(

            severity=level

        ).all()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
