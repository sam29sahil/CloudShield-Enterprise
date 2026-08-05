"""
CloudShield Enterprise
Report Service
"""

from datetime import datetime

from app.extensions import db
from app.models.report import Report


class ReportService:

<<<<<<< HEAD
    def create(self, scan_id, report_type, file_name):

        report = Report(
            scan_id=scan_id,
            report_type=report_type,
            file_name=file_name,
            created_at=datetime.utcnow(),
=======
    def create(

        self,

        scan_id,

        report_type,

        file_name

    ):

        report = Report(

            scan_id=scan_id,

            report_type=report_type,

            file_name=file_name,

            created_at=datetime.utcnow()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        db.session.add(report)

        db.session.commit()

        return report

    def get(self, report_id):

        return Report.query.get(report_id)

    def all(self):

<<<<<<< HEAD
        return Report.query.order_by(Report.created_at.desc()).all()

    def scan_reports(self, scan_id):

        return Report.query.filter_by(scan_id=scan_id).all()
=======
        return Report.query.order_by(

            Report.created_at.desc()

        ).all()

    def scan_reports(self, scan_id):

        return Report.query.filter_by(

            scan_id=scan_id

        ).all()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def delete(self, report_id):

        report = self.get(report_id)

        if report:

            db.session.delete(report)

            db.session.commit()

            return True

<<<<<<< HEAD
        return False
=======
        return False
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
