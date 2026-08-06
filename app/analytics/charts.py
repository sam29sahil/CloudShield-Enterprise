"""
CloudShield Enterprise
Analytics Charts
"""

from sqlalchemy import func

from app.extensions import db
from app.models import SecurityScan


class ChartData:
    """
    Chart Data Generator
    """

    @staticmethod
    def score_chart():
        """
        Security score trend.
        """

        scans = SecurityScan.query.order_by(SecurityScan.started_at.asc()).all()

        return {
            "labels": [scan.started_at.strftime("%d-%m") for scan in scans],
            "datasets": [
                {"label": "Security Score", "data": [scan.score for scan in scans]}
            ],
        }

    @staticmethod
    def risk_chart():
        """
        Risk distribution.
        """

        risks = {
            "Critical": SecurityScan.query.filter_by(risk="Critical").count(),
            "High": SecurityScan.query.filter_by(risk="High").count(),
            "Medium": SecurityScan.query.filter_by(risk="Medium").count(),
            "Low": SecurityScan.query.filter_by(risk="Low").count(),
            "Unknown": SecurityScan.query.filter_by(risk="Unknown").count(),
        }

        return {
            "labels": list(risks.keys()),
            "datasets": [{"label": "Risk Distribution", "data": list(risks.values())}],
        }

    @staticmethod
    def tool_chart():
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
            "datasets": [{"label": "Scanner Usage", "data": [row[1] for row in rows]}],
        }

    @staticmethod
    def charts():
        """
        Return all charts.
        """

        return {
            "score": ChartData.score_chart(),
            "risk": ChartData.risk_chart(),
            "tools": ChartData.tool_chart(),
        }
