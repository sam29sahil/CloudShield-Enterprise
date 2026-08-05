"""
CloudShield Enterprise
Settings Routes
"""

<<<<<<< HEAD
from flask import render_template, redirect, url_for, flash, request

from flask_login import login_required, current_user
=======
from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from flask_login import (
    login_required,
    current_user
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

from app.settings import settings
from app.settings.forms import (
    ProfileForm,
    PasswordForm,
    ScannerSettingsForm,
    ReportSettingsForm,
<<<<<<< HEAD
    NotificationSettingsForm,
=======
    NotificationSettingsForm
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
)

from app.settings.services import SettingsService

service = SettingsService()


@settings.route("/", methods=["GET", "POST"])
@login_required
def index():

    profile_form = ProfileForm(prefix="profile")

    password_form = PasswordForm(prefix="password")

    scanner_form = ScannerSettingsForm(prefix="scanner")

    report_form = ReportSettingsForm(prefix="report")

    notification_form = NotificationSettingsForm(prefix="notification")

    # -----------------------------
    # Load Current User
    # -----------------------------

    if request.method == "GET":

<<<<<<< HEAD
        profile_form.full_name.data = getattr(current_user, "full_name", "")
=======
        profile_form.full_name.data = getattr(
            current_user,
            "full_name",
            ""
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        profile_form.username.data = current_user.username

        profile_form.email.data = current_user.email

    # -----------------------------
    # Profile
    # -----------------------------

<<<<<<< HEAD
    if profile_form.submit.data and profile_form.validate_on_submit():

        service.update_profile(current_user, profile_form)

        flash("Profile updated successfully.", "success")

        return redirect(url_for("settings.index"))
=======
    if (

        profile_form.submit.data

        and

        profile_form.validate_on_submit()

    ):

        service.update_profile(

            current_user,

            profile_form

        )

        flash(

            "Profile updated successfully.",

            "success"

        )

        return redirect(

            url_for("settings.index")

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # -----------------------------
    # Password
    # -----------------------------

<<<<<<< HEAD
    if password_form.submit.data and password_form.validate_on_submit():

        success, message = service.change_password(current_user, password_form)

        flash(message, "success" if success else "danger")

        return redirect(url_for("settings.index"))
=======
    if (

        password_form.submit.data

        and

        password_form.validate_on_submit()

    ):

        success, message = service.change_password(

            current_user,

            password_form

        )

        flash(

            message,

            "success" if success else "danger"

        )

        return redirect(

            url_for("settings.index")

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # -----------------------------
    # Scanner
    # -----------------------------

<<<<<<< HEAD
    if scanner_form.submit.data and scanner_form.validate_on_submit():

        flash("Scanner settings saved.", "success")

        return redirect(url_for("settings.index"))
=======
    if (

        scanner_form.submit.data

        and

        scanner_form.validate_on_submit()

    ):

        flash(

            "Scanner settings saved.",

            "success"

        )

        return redirect(

            url_for("settings.index")

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # -----------------------------
    # Reports
    # -----------------------------

<<<<<<< HEAD
    if report_form.submit.data and report_form.validate_on_submit():

        flash("Report settings saved.", "success")

        return redirect(url_for("settings.index"))
=======
    if (

        report_form.submit.data

        and

        report_form.validate_on_submit()

    ):

        flash(

            "Report settings saved.",

            "success"

        )

        return redirect(

            url_for("settings.index")

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # -----------------------------
    # Notifications
    # -----------------------------

<<<<<<< HEAD
    if notification_form.submit.data and notification_form.validate_on_submit():

        flash("Notification settings saved.", "success")

        return redirect(url_for("settings.index"))

    return render_template(
        "settings/index.html",
        user=current_user,
        profile_form=profile_form,
        password_form=password_form,
        scanner_form=scanner_form,
        report_form=report_form,
        notification_form=notification_form,
        system=service.system_information(),
    )
=======
    if (

        notification_form.submit.data

        and

        notification_form.validate_on_submit()

    ):

        flash(

            "Notification settings saved.",

            "success"

        )

        return redirect(

            url_for("settings.index")

        )

    return render_template(

        "settings/index.html",

        user=current_user,

        profile_form=profile_form,

        password_form=password_form,

        scanner_form=scanner_form,

        report_form=report_form,

        notification_form=notification_form,

        system=service.system_information()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
