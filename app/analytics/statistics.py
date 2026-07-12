"""
CloudShield Enterprise
Analytics Statistics
"""

from app.models import SecurityScan


class Statistics:

    @staticmethod
    def risk_distribution():
        """
        Risk distribution.
        """

        return {

            "Low": SecurityScan.query.filter_by(
                risk="Low"
            ).count(),

            "Medium": SecurityScan.query.filter_by(
                risk="Medium"
            ).count(),

            "High": SecurityScan.query.filter_by(
                risk="High"
            ).count()

        }

    @staticmethod
    def latest_scores(limit=10):
        """
        Latest security scores.
        """

        scans = (
            SecurityScan.query
            .order_by(
                Scan.started_at.desc()
            )
            .limit(limit)
            .all()
        )

        return [

            scan.score

            for scan in scans

        ]