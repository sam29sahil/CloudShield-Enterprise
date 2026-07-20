"""
CloudShield Enterprise
Notifications API
"""

from flask import request
from flask_login import login_required

from app.api import api
from app.api.responses import success_response, error_response
from app.services.notification_service import NotificationService

notification_service = NotificationService()


@api.route("/notifications", methods=["GET"])
@login_required
def get_notifications():
    """
    Get all notifications.
    """

    notifications = notification_service.all()

    data = []

    for notification in notifications:

        data.append({

            "id": notification.id,

            "title": notification.title,

            "message": notification.message,

            "category": notification.category,

            "is_read": notification.is_read,

            "created_at": (
                notification.created_at.isoformat()
                if notification.created_at
                else None
            )

        })

    return success_response(

        data=data,

        message="Notifications retrieved successfully"

    )


@api.route("/notifications/unread", methods=["GET"])
@login_required
def unread_notifications():

    notifications = notification_service.unread()

    data = []

    for notification in notifications:

        data.append({

            "id": notification.id,

            "title": notification.title,

            "message": notification.message,

            "category": notification.category,

            "created_at": (
                notification.created_at.isoformat()
                if notification.created_at
                else None
            )

        })

    return success_response(

        data=data,

        message="Unread notifications"

    )


@api.route("/notifications", methods=["POST"])
@login_required
def create_notification():

    data = request.get_json()

    if not data:

        return error_response(

            "JSON data required",

            400

        )

    required = [

        "title",

        "message"

    ]

    for field in required:

        if field not in data:

            return error_response(

                f"{field} is required",

                400

            )

    notification = notification_service.create(

        title=data["title"],

        message=data["message"],

        category=data.get("category", "General")

    )

    return success_response(

        data={

            "id": notification.id

        },

        message="Notification created successfully",

        status_code=201

    )


@api.route("/notifications/<int:notification_id>/read", methods=["PUT"])
@login_required
def mark_read(notification_id):

    notification = notification_service.get(notification_id)

    if not notification:

        return error_response(

            "Notification not found",

            404

        )

    notification_service.mark_read(notification)

    return success_response(

        message="Notification marked as read"

    )


@api.route("/notifications/read-all", methods=["PUT"])
@login_required
def mark_all_read():

    notification_service.mark_all_read()

    return success_response(

        message="All notifications marked as read"

    )


@api.route("/notifications/<int:notification_id>", methods=["DELETE"])
@login_required
def delete_notification(notification_id):

    deleted = notification_service.delete(notification_id)

    if not deleted:

        return error_response(

            "Notification not found",

            404

        )

    return success_response(

        message="Notification deleted successfully"

    )