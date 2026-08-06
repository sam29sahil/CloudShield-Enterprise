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
            "total_users": User.query.count(),
            "total_scans": SecurityScan.query.count(),
            "completed": SecurityScan.query.filter_by(status="Completed").count(),
            "running": SecurityScan.query.filter_by(status="Running").count(),
            "failed": SecurityScan.query.filter_by(status="Failed").count(),
            "critical": SecurityScan.query.filter_by(risk="Critical").count(),
            "high": SecurityScan.query.filter_by(risk="High").count(),
            "medium": SecurityScan.query.filter_by(risk="Medium").count(),
            "low": SecurityScan.query.filter_by(risk="Low").count(),
        }

    @staticmethod
    def recent_scans(limit=10):
        """
        Latest scans.
        """

        return (
            SecurityScan.query.order_by(SecurityScan.started_at.desc())
            .limit(limit)
            .all()
        )

    @staticmethod
    def all_users():
        """
        Return all users.
        """

        return User.query.order_by(User.id.asc()).all()

    @staticmethod
    def all_scans():
        """
        Return every scan.
        """

        return SecurityScan.query.order_by(SecurityScan.started_at.desc()).all()

    @staticmethod
    def completed_scans():
        """
        Completed scans.
        """

        return SecurityScan.query.filter_by(status="Completed").all()

    @staticmethod
    def failed_scans():
        """
        Failed scans.
        """

        return SecurityScan.query.filter_by(status="Failed").all()

    @staticmethod
    def critical_scans():
        """
        Critical findings.
        """

        return SecurityScan.query.filter_by(risk="Critical").all()

    @staticmethod
    def high_risk_scans():
        """
        High risk findings.
        """

        return SecurityScan.query.filter_by(risk="High").all()

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

        return True
