"""
CloudShield Enterprise
Findings Services
"""

from app.models import SecurityScan


class FindingsService:

    @staticmethod
    def all():

        return (

            SecurityScan.query

            .order_by(

                SecurityScan.score.desc()

            )

            .all()

        )

    @staticmethod
    def critical():

        return (

            SecurityScan.query

            .filter(

                SecurityScan.risk == "Critical"

            )

            .all()

        )

    @staticmethod
    def high():

        return (

            SecurityScan.query

            .filter(

                SecurityScan.risk == "High"

            )

            .all()

        ) 