"""
CloudShield Enterprise
Report Service
"""

from datetime import datetime

from app.extensions import db
from app.models.report import Report


class ReportService:

    def create(self, scan_id, report_type, file_name):

        report = Report(
            scan_id=scan_id,
            report_type=report_type,
            file_name=file_name,
            created_at=datetime.utcnow(),
        )

        db.session.add(report)

        db.session.commit()

        return report

    def get(self, report_id):

        return Report.query.get(report_id)

    def all(self):

        return Report.query.order_by(Report.created_at.desc()).all()

    def scan_reports(self, scan_id):

        return Report.query.filter_by(scan_id=scan_id).all()

    def delete(self, report_id):

        report = self.get(report_id)

        if report:

            db.session.delete(report)

            db.session.commit()

            return True

        return False
