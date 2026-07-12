"""
CloudShield Enterprise
Notification Service
"""

from app.extensions import db
from app.notifications.models import Notification


class NotificationService:

    def create(
        self,
        user_id,
        title="Scan Completed",
        message="Your scan has completed successfully.",
        severity="Info"
    ):

        notification = Notification(
            user_id=user_id,
            title=title,
            message=message,
            severity=severity
        )

        db.session.add(notification)
        db.session.commit()

        return notification

    def all(self, user_id):

        return (
            Notification.query
            .filter_by(user_id=user_id)
            .order_by(Notification.created_at.desc())
            .all()
        )

    def unread_count(self, user_id):

        return (
            Notification.query
            .filter_by(
                user_id=user_id,
                is_read=False
            )
            .count()
        )

    def mark_read(self, notification_id, user_id):

        notification = (
            Notification.query
            .filter_by(
                id=notification_id,
                user_id=user_id
            )
            .first()
        )

        if notification:
            notification.is_read = True
            db.session.commit()

        return notification

    def mark_all_read(self, user_id):

        (
            Notification.query
            .filter_by(
                user_id=user_id,
                is_read=False
            )
            .update(
                {
                    "is_read": True
                }
            )
        )

        db.session.commit()

    def delete(self, notification_id, user_id):

        notification = (
            Notification.query
            .filter_by(
                id=notification_id,
                user_id=user_id
            )
            .first()
        )

        if notification:
            db.session.delete(notification)
            db.session.commit()

    def delete_all(self, user_id):

        (
            Notification.query
            .filter_by(
                user_id=user_id
            )
            .delete()
        )

        db.session.commit()