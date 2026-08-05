"""
CloudShield Enterprise
History Services
"""

from app.models import SecurityScan


class HistoryService:

    @staticmethod
    def all():

<<<<<<< HEAD
        return SecurityScan.query.order_by(SecurityScan.started_at.desc()).all()
=======
        return (

            SecurityScan.query

            .order_by(

                SecurityScan.started_at.desc()

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def latest(limit=10):

        return (
<<<<<<< HEAD
            SecurityScan.query.order_by(SecurityScan.started_at.desc())
            .limit(limit)
            .all()
        )
=======

            SecurityScan.query

            .order_by(

                SecurityScan.started_at.desc()

            )

            .limit(limit)

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
