"""
CloudShield Enterprise
Enterprise Notification Service
"""

from app.extensions import db
from app.notifications.models import Notification


class NotificationService:

    # ----------------------------------------
    # Create Notification
    # ----------------------------------------

    def create(
        self,
        user_id,
        title,
        message,
        severity="Info",
        source="System",
        icon="bi-bell-fill",
        url=None,
    ):

        notification = Notification(
            user_id=user_id,
            title=title,
            message=message,
            severity=severity,
            source=source,
            icon=icon,
            url=url,
        )

        db.session.add(notification)

        db.session.commit()

        return notification

    # ----------------------------------------
    # Scanner Notification
    # ----------------------------------------

    def scan_completed(self, user_id, target):

        return self.create(
            user_id=user_id,
            title="Scan Completed",
            message=f"Security scan completed for {target}.",
            severity="Info",
            source="Scanner",
            icon="bi-search",
        )

    # ----------------------------------------
    # High Risk Finding
    # ----------------------------------------

    def high_risk(self, user_id, finding):

        return self.create(
            user_id=user_id,
            title="High Risk Finding",
            message=f"{finding} detected.",
            severity="High",
            source="Scanner",
            icon="bi-exclamation-triangle-fill",
        )

    # ----------------------------------------
    # Report Generated
    # ----------------------------------------

    def report_generated(self, user_id, report):

        return self.create(
            user_id=user_id,
            title="Report Generated",
            message=f"{report} is ready.",
            severity="Info",
            source="Reports",
            icon="bi-file-earmark-pdf",
        )

    # ----------------------------------------
    # Asset Added
    # ----------------------------------------

    def asset_added(self, user_id, asset):

        return self.create(
            user_id=user_id,
            title="New Asset Added",
            message=f"{asset} added successfully.",
            severity="Info",
            source="Assets",
            icon="bi-hdd-network",
        )

    # ----------------------------------------
    # Get All
    # ----------------------------------------

    def all(self, user_id):

        return (
            Notification.query.filter_by(user_id=user_id)
            .order_by(Notification.created_at.desc())
            .all()
        )

    # ----------------------------------------
    # Recent
    # ----------------------------------------

    def recent(self, user_id, limit=5):

        return (
            Notification.query.filter_by(user_id=user_id)
            .order_by(Notification.created_at.desc())
            .limit(limit)
            .all()
        )

    # ----------------------------------------
    # Unread
    # ----------------------------------------

    def unread(self, user_id):

        return (
            Notification.query.filter_by(user_id=user_id, is_read=False)
            .order_by(Notification.created_at.desc())
            .all()
        )

    # ----------------------------------------
    # Count
    # ----------------------------------------

    def unread_count(self, user_id):

        return Notification.query.filter_by(user_id=user_id, is_read=False).count()

    # ----------------------------------------
    # Mark Read
    # ----------------------------------------

    def mark_read(self, notification_id, user_id):

        notification = Notification.query.filter_by(
            id=notification_id, user_id=user_id
        ).first()

        if notification:

            notification.is_read = True

            db.session.commit()

        return notification

    # ----------------------------------------
    # Mark All
    # ----------------------------------------

    def mark_all_read(self, user_id):

        (
            Notification.query.filter_by(user_id=user_id, is_read=False).update(
                {"is_read": True}
            )
        )

        db.session.commit()

    # ----------------------------------------
    # Delete One
    # ----------------------------------------

    def delete(self, notification_id, user_id):

        notification = Notification.query.filter_by(
            id=notification_id, user_id=user_id
        ).first()

        if notification:

            db.session.delete(notification)

            db.session.commit()

    # ----------------------------------------
    # Delete All
    # ----------------------------------------

    def delete_all(self, user_id):

        (Notification.query.filter_by(user_id=user_id).delete())

        db.session.commit()

    # ----------------------------------------
    # Filter by Severity
    # ----------------------------------------

    def severity(self, user_id, severity):

        return (
            Notification.query.filter_by(user_id=user_id, severity=severity)
            .order_by(Notification.created_at.desc())
            .all()
        )
