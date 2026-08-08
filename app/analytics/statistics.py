"""
CloudShield Enterprise
Analytics Statistics
"""

from sqlalchemy import func

from app.extensions import db
from app.models import SecurityScan


class Statistics:
    """
    Analytics Statistics
    """

    # ------------------------------------------
    # Risk Distribution
    # ------------------------------------------

    @staticmethod
    def risk_distribution():
        """
        Risk distribution.
        """

        return {
            "Low": SecurityScan.query.filter_by(risk="Low").count(),
            "Medium": SecurityScan.query.filter_by(risk="Medium").count(),
            "High": SecurityScan.query.filter_by(risk="High").count(),
            "Critical": SecurityScan.query.filter_by(risk="Critical").count(),
            "Unknown": SecurityScan.query.filter_by(risk="Unknown").count(),
        }

    # ------------------------------------------
    # Latest Security Scores
    # ------------------------------------------

    @staticmethod
    def latest_scores(limit=10):
        """
        Latest security scores.
        """

        scans = (
            SecurityScan.query.order_by(SecurityScan.started_at.desc())
            .limit(limit)
            .all()
        )

        scans.reverse()

        return [scan.score for scan in scans]

    # ------------------------------------------
    # Scan Status
    # ------------------------------------------

    @staticmethod
    def scan_status():
        """
        Scan status statistics.
        """

        return {
            "Completed": SecurityScan.query.filter_by(status="Completed").count(),
            "Failed": SecurityScan.query.filter_by(status="Failed").count(),
            "Running": SecurityScan.query.filter_by(status="Running").count(),
            "Pending": SecurityScan.query.filter_by(status="Pending").count(),
        }

    # ------------------------------------------
    # Tool Usage
    # ------------------------------------------

    @staticmethod
    def tool_usage():
        """
        Scanner tool usage.
        """

        rows = (
            db.session.query(SecurityScan.tool, func.count(SecurityScan.id))
            .group_by(SecurityScan.tool)
            .all()
        )

        return {
            "labels": [row[0] or "Unknown" for row in rows],
            "values": [row[1] for row in rows],
        }

    # ------------------------------------------
    # Average Score
    # ------------------------------------------

    @staticmethod
    def average_score():
        """
        Average security score.
        """

        score = db.session.query(func.avg(SecurityScan.score)).scalar()

        return round(score or 0)

    # ------------------------------------------
    # Scan Performance
    # ------------------------------------------

    @staticmethod
    def performance():
        """
        Scan performance statistics.
        """

        average = db.session.query(func.avg(SecurityScan.duration)).scalar() or 0

        maximum = db.session.query(func.max(SecurityScan.duration)).scalar() or 0

        minimum = db.session.query(func.min(SecurityScan.duration)).scalar() or 0

        return {
            "average": round(average, 2),
            "maximum": round(maximum, 2),
            "minimum": round(minimum, 2),
        }

    # ------------------------------------------
    # Total Scans
    # ------------------------------------------

    @staticmethod
    def total_scans():
        """
        Total scans.
        """

        return SecurityScan.query.count()

    # ------------------------------------------
    # Dashboard Statistics
    # ------------------------------------------

    @staticmethod
    def dashboard():
        """
        Complete dashboard statistics.
        """

        return {
            "risk": Statistics.risk_distribution(),
            "scores": Statistics.latest_scores(),
            "status": Statistics.scan_status(),
            "tools": Statistics.tool_usage(),
            "average_score": Statistics.average_score(),
            "performance": Statistics.performance(),
            "total_scans": Statistics.total_scans(),
        }
