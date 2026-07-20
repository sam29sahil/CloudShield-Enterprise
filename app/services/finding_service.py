"""
CloudShield Enterprise
Finding Service
"""

from app.extensions import db
from app.models.finding import Finding


class FindingService:

    def create(

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

        )

        db.session.add(finding)

        db.session.commit()

        return finding

    def all(self):

        return Finding.query.all()

    def scan_findings(self, scan_id):

        return Finding.query.filter_by(

            scan_id=scan_id

        ).all()

    def severity(self, level):

        return Finding.query.filter_by(

            severity=level

        ).all()