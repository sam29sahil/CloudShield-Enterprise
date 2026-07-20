"""
CloudShield Enterprise
Notification Routes
"""

from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from app.notifications import notifications
from app.notifications.services import NotificationService

service = NotificationService()


@notifications.route("/")
@login_required
def index():

    notifications_list = service.all(current_user.id)

    unread_count = service.unread_count(current_user.id)

    return render_template(
        "notifications/index.html",
        notifications=notifications_list,
        unread_count=unread_count
    )


@notifications.route("/read/<int:id>")
@login_required
def read(id):

    service.mark_read(
        id,
        current_user.id
    )

    return redirect(
        url_for("notifications.index")
    )


@notifications.route("/read-all")
@login_required
def read_all():

    service.mark_all_read(current_user.id)

    return redirect(
        url_for("notifications.index")
    )


@notifications.route("/delete/<int:id>")
@login_required
def delete(id):

    service.delete(
        id,
        current_user.id
    )

    return redirect(
        url_for("notifications.index")
    )


@notifications.route("/delete-all")
@login_required
def delete_all():

    service.delete_all(current_user.id)

    return redirect(
        url_for("notifications.index")
    )