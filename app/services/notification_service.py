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
<<<<<<< HEAD
        return Notification.query.order_by(Notification.created_at.desc()).all()
=======
        return (
            Notification.query
            .order_by(Notification.created_at.desc())
            .all()
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

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
<<<<<<< HEAD
            Notification.query.filter_by(is_read=False)
=======
            Notification.query
            .filter_by(is_read=False)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            .order_by(Notification.created_at.desc())
            .all()
        )

<<<<<<< HEAD
    def create(self, title, message, category="General"):
=======
    def create(
        self,
        title,
        message,
        category="General"
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        """
        Create notification.
        """

<<<<<<< HEAD
        notification = Notification(title=title, message=message, category=category)
=======
        notification = Notification(
            title=title,
            message=message,
            category=category
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        db.session.add(notification)
        db.session.commit()

        return notification

<<<<<<< HEAD
    def mark_read(self, notification):
=======
    def mark_read(
        self,
        notification
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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

<<<<<<< HEAD
        notifications = Notification.query.filter_by(is_read=False).all()
=======
        notifications = Notification.query.filter_by(
            is_read=False
        ).all()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        for notification in notifications:
            notification.is_read = True

        db.session.commit()

        return notifications

<<<<<<< HEAD
    def delete(self, notification_id):
=======
    def delete(
        self,
        notification_id
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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

<<<<<<< HEAD
        return True
=======
        return True
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
