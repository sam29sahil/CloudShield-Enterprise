"""
CloudShield Enterprise
Analytics Service
"""

from sqlalchemy import func

from app.extensions import db
from app.models import SecurityScan


class AnalyticsService:

    def statistics(self):
        """
        Dashboard statistics.
        """

        total_scans = SecurityScan.query.count()

        average_score = db.session.query(
            func.avg(SecurityScan.score)
        ).scalar()

        if average_score is None:
            average_score = 0

        average_score = round(average_score)

        completed = SecurityScan.query.filter_by(
            status="Completed"
        ).count()

        failed = SecurityScan.query.filter_by(
            status="Failed"
        ).count()

        critical = SecurityScan.query.filter_by(
            risk="Critical"
        ).count()

        high = SecurityScan.query.filter_by(
            risk="High"
        ).count()

        medium = SecurityScan.query.filter_by(
            risk="Medium"
        ).count()

        low = SecurityScan.query.filter_by(
            risk="Low"
        ).count()

        return {

            "total_scans": total_scans,

            "average_score": average_score,

            "completed": completed,

            "failed": failed,

            "critical": critical,

            "high": high,

            "medium": medium,

            "low": low

        }

    def chart_data(self):
        """
        Chart data.
        """

        scans = (
            SecurityScan.query
            .order_by(SecurityScan.started_at.asc())
            .all()
        )

        labels = []
        scores = []

        for scan in scans:

            labels.append(

                scan.started_at.strftime("%d-%m")

            )

            scores.append(

                scan.score

            )

        return {

            "labels": labels,

            "scores": scores

        }