"""
CloudShield Enterprise
Analytics Charts
"""

from app.models import SecurityScan


class ChartData:

    @staticmethod
    def score_chart():
        """
        Security score chart.
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

            "datasets": [

                {

                    "label": "Security Score",

                    "data": scores

                }

            ]

        }

    @staticmethod
    def risk_chart():
        """
        Risk distribution.
        """

        low = SecurityScan.query.filter_by(
            risk="Low"
        ).count()

        medium = SecurityScan.query.filter_by(
            risk="Medium"
        ).count()

        high = SecurityScan.query.filter_by(
            risk="High"
        ).count()

        return {

            "labels": [

                "Low",

                "Medium",

                "High"

            ],

            "datasets": [

                {

                    "data": [

                        low,

                        medium,

                        high

                    ]

                }

            ]

        }