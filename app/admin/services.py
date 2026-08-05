"""
CloudShield Enterprise
Admin Services
"""

from app.models import User
from app.models import SecurityScan


class AdminService:
    """
    Admin business logic.
    """

    @staticmethod
    def dashboard_stats():
        """
        Dashboard statistics.
        """

        return {
<<<<<<< HEAD
            "total_users": User.query.count(),
            "total_scans": SecurityScan.query.count(),
            "completed": SecurityScan.query.filter_by(status="Completed").count(),
            "running": SecurityScan.query.filter_by(status="Running").count(),
            "failed": SecurityScan.query.filter_by(status="Failed").count(),
            "critical": SecurityScan.query.filter_by(risk="Critical").count(),
            "high": SecurityScan.query.filter_by(risk="High").count(),
            "medium": SecurityScan.query.filter_by(risk="Medium").count(),
            "low": SecurityScan.query.filter_by(risk="Low").count(),
=======

            "total_users": User.query.count(),

            "total_scans": SecurityScan.query.count(),

            "completed": SecurityScan.query.filter_by(
                status="Completed"
            ).count(),

            "running": SecurityScan.query.filter_by(
                status="Running"
            ).count(),

            "failed": SecurityScan.query.filter_by(
                status="Failed"
            ).count(),

            "critical": SecurityScan.query.filter_by(
                risk="Critical"
            ).count(),

            "high": SecurityScan.query.filter_by(
                risk="High"
            ).count(),

            "medium": SecurityScan.query.filter_by(
                risk="Medium"
            ).count(),

            "low": SecurityScan.query.filter_by(
                risk="Low"
            ).count()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    @staticmethod
    def recent_scans(limit=10):
        """
        Latest scans.
        """

        return (
<<<<<<< HEAD
            SecurityScan.query.order_by(SecurityScan.started_at.desc())
            .limit(limit)
            .all()
=======

            SecurityScan.query

            .order_by(

                SecurityScan.started_at.desc()

            )

            .limit(limit)

            .all()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

    @staticmethod
    def all_users():
        """
        Return all users.
        """

<<<<<<< HEAD
        return User.query.order_by(User.id.asc()).all()
=======
        return (

            User.query

            .order_by(

                User.id.asc()

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def all_scans():
        """
        Return every scan.
        """

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
    def completed_scans():
        """
        Completed scans.
        """

<<<<<<< HEAD
        return SecurityScan.query.filter_by(status="Completed").all()
=======
        return (

            SecurityScan.query

            .filter_by(

                status="Completed"

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def failed_scans():
        """
        Failed scans.
        """

<<<<<<< HEAD
        return SecurityScan.query.filter_by(status="Failed").all()
=======
        return (

            SecurityScan.query

            .filter_by(

                status="Failed"

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def critical_scans():
        """
        Critical findings.
        """

<<<<<<< HEAD
        return SecurityScan.query.filter_by(risk="Critical").all()
=======
        return (

            SecurityScan.query

            .filter_by(

                risk="Critical"

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def high_risk_scans():
        """
        High risk findings.
        """

<<<<<<< HEAD
        return SecurityScan.query.filter_by(risk="High").all()
=======
        return (

            SecurityScan.query

            .filter_by(

                risk="High"

            )

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    @staticmethod
    def get_user(user_id):
        """
        Get one user.
        """

        return User.query.get(user_id)

    @staticmethod
    def get_scan(scan_id):
        """
        Get one scan.
        """

        return SecurityScan.query.get(scan_id)

    @staticmethod
    def delete_scan(scan_id):
        """
        Delete scan.
        """

        scan = SecurityScan.query.get(scan_id)

        if not scan:

            return False

        from app.extensions import db

        db.session.delete(scan)

        db.session.commit()

        return True

    @staticmethod
    def delete_user(user_id):
        """
        Delete user.
        """

        user = User.query.get(user_id)

        if not user:

            return False

        from app.extensions import db

        db.session.delete(user)

        db.session.commit()

<<<<<<< HEAD
        return True
=======
        return True
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
