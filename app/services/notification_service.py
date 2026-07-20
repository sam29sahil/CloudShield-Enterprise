"""
CloudShield Enterprise
Notification Service
"""

from app.extensions import db
from app.models.notification import Notification


class NotificationService:

    def all(self):
        """
        Return all notifications.
        """
        return (
            Notification.query
            .order_by(Notification.created_at.desc())
            .all()
        )

    def get(self, notification_id):
        """
        Get notification by ID.
        """
        return Notification.query.get(notification_id)

    def unread(self):
        """
        Return unread notifications.
        """
        return (
            Notification.query
            .filter_by(is_read=False)
            .order_by(Notification.created_at.desc())
            .all()
        )

    def create(
        self,
        title,
        message,
        category="General"
    ):
        """
        Create notification.
        """

        notification = Notification(
            title=title,
            message=message,
            category=category
        )

        db.session.add(notification)
        db.session.commit()

        return notification

    def mark_read(
        self,
        notification
    ):
        """
        Mark notification as read.
        """

        notification.is_read = True

        db.session.commit()

        return notification

    def mark_all_read(self):
        """
        Mark all notifications as read.
        """

        notifications = Notification.query.filter_by(
            is_read=False
        ).all()

        for notification in notifications:
            notification.is_read = True

        db.session.commit()

        return notifications

    def delete(
        self,
        notification_id
    ):
        """
        Delete notification.
        """

        notification = self.get(notification_id)

        if not notification:
            return None

        db.session.delete(notification)
        db.session.commit()

        return True

    def clear(self):
        """
        Delete all notifications.
        """

        Notification.query.delete()

        db.session.commit()

        return True