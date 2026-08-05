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

<<<<<<< HEAD
        scans = SecurityScan.query.order_by(SecurityScan.started_at.asc()).all()

        return {
            "labels": [scan.started_at.strftime("%d-%m") for scan in scans],
            "datasets": [
                {"label": "Security Score", "data": [scan.score for scan in scans]}
            ],
=======
        scans = (
            SecurityScan.query
            .order_by(SecurityScan.started_at.asc())
            .all()
        )

        return {

            "labels": [

                scan.started_at.strftime("%d-%m")

                for scan in scans

            ],

            "datasets": [

                {

                    "label": "Security Score",

                    "data": [

                        scan.score

                        for scan in scans

                    ]

                }

            ]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    @staticmethod
    def risk_chart():
        """
        Risk distribution.
        """

        risks = {
<<<<<<< HEAD
            "Critical": SecurityScan.query.filter_by(risk="Critical").count(),
            "High": SecurityScan.query.filter_by(risk="High").count(),
            "Medium": SecurityScan.query.filter_by(risk="Medium").count(),
            "Low": SecurityScan.query.filter_by(risk="Low").count(),
            "Unknown": SecurityScan.query.filter_by(risk="Unknown").count(),
        }

        return {
            "labels": list(risks.keys()),
            "datasets": [{"label": "Risk Distribution", "data": list(risks.values())}],
=======

            "Critical": SecurityScan.query.filter_by(
                risk="Critical"
            ).count(),

            "High": SecurityScan.query.filter_by(
                risk="High"
            ).count(),

            "Medium": SecurityScan.query.filter_by(
                risk="Medium"
            ).count(),

            "Low": SecurityScan.query.filter_by(
                risk="Low"
            ).count(),

            "Unknown": SecurityScan.query.filter_by(
                risk="Unknown"
            ).count()

        }

        return {

            "labels": list(risks.keys()),

            "datasets": [

                {

                    "label": "Risk Distribution",

                    "data": list(risks.values())

                }

            ]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    @staticmethod
    def tool_chart():
        """
        Scanner tool usage.
        """

        rows = (
<<<<<<< HEAD
            db.session.query(SecurityScan.tool, func.count(SecurityScan.id))
            .group_by(SecurityScan.tool)
            .all()
        )

        return {
            "labels": [row[0] or "Unknown" for row in rows],
            "datasets": [{"label": "Scanner Usage", "data": [row[1] for row in rows]}],
=======

            db.session.query(

                SecurityScan.tool,

                func.count(SecurityScan.id)

            )

            .group_by(

                SecurityScan.tool

            )

            .all()

        )

        return {

            "labels": [

                row[0] or "Unknown"

                for row in rows

            ],

            "datasets": [

                {

                    "label": "Scanner Usage",

                    "data": [

                        row[1]

                        for row in rows

                    ]

                }

            ]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    @staticmethod
    def charts():
        """
        Return all charts.
        """

        return {
<<<<<<< HEAD
            "score": ChartData.score_chart(),
            "risk": ChartData.risk_chart(),
            "tools": ChartData.tool_chart(),
        }
=======

            "score": ChartData.score_chart(),

            "risk": ChartData.risk_chart(),

            "tools": ChartData.tool_chart()

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
