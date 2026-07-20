"""
CloudShield Enterprise
History Services
"""

from app.models import SecurityScan


class HistoryService:

    @staticmethod
    def all():

        return (

            SecurityScan.query

            .order_by(

                SecurityScan.started_at.desc()

            )

            .all()

        )

    @staticmethod
    def latest(limit=10):

        return (

            SecurityScan.query

            .order_by(

                SecurityScan.started_at.desc()

            )

            .limit(limit)

            .all()

        )