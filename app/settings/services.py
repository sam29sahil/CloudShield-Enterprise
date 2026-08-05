"""
CloudShield Enterprise
Settings Service
"""

import platform
import sys

import flask

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app.extensions import db
<<<<<<< HEAD
from app.models import Asset, Finding, SecurityScan, User
=======
from app.models import (
    Asset,
    Finding,
    SecurityScan,
    User
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


class SettingsService:

    # ==================================================
    # Profile
    # ==================================================

<<<<<<< HEAD
    def update_profile(self, user, form):
=======
    def update_profile(

        self,

        user,

        form

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        user.full_name = form.full_name.data

        user.username = form.username.data

        user.email = form.email.data

        db.session.commit()

        return True

    # ==================================================
    # Password
    # ==================================================

<<<<<<< HEAD
    def change_password(self, user, form):

        if not check_password_hash(user.password, form.current_password.data):

            return False, "Current password is incorrect."

        user.password = generate_password_hash(form.new_password.data)
=======
    def change_password(

        self,

        user,

        form

    ):

        if not check_password_hash(

            user.password,

            form.current_password.data

        ):

            return False, "Current password is incorrect."

        user.password = generate_password_hash(

            form.new_password.data

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        db.session.commit()

        return True, "Password updated successfully."

    # ==================================================
    # Scanner Settings
    # ==================================================

<<<<<<< HEAD
    def scanner_settings(self, form):

        return {
            "default_mode": form.default_mode.data,
            "default_category": form.default_category.data,
            "timeout": form.timeout.data,
            "save_history": form.save_history.data,
=======
    def scanner_settings(

        self,

        form

    ):

        return {

            "default_mode":

                form.default_mode.data,

            "default_category":

                form.default_category.data,

            "timeout":

                form.timeout.data,

            "save_history":

                form.save_history.data

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # ==================================================
    # Report Settings
    # ==================================================

<<<<<<< HEAD
    def report_settings(self, form):

        return {
            "company_name": form.company_name.data,
            "company_email": form.company_email.data,
            "company_website": form.company_website.data,
            "default_format": form.default_format.data,
            "include_summary": form.include_summary.data,
            "include_recommendations": form.include_recommendations.data,
            "include_raw": form.include_raw.data,
=======
    def report_settings(

        self,

        form

    ):

        return {

            "company_name":

                form.company_name.data,

            "company_email":

                form.company_email.data,

            "company_website":

                form.company_website.data,

            "default_format":

                form.default_format.data,

            "include_summary":

                form.include_summary.data,

            "include_recommendations":

                form.include_recommendations.data,

            "include_raw":

                form.include_raw.data

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # ==================================================
    # Notification Settings
    # ==================================================

<<<<<<< HEAD
    def notification_settings(self, form):

        return {
            "enable_notifications": form.enable_notifications.data,
            "notify_scan_complete": form.notify_scan_complete.data,
            "notify_scan_failed": form.notify_scan_failed.data,
            "notify_critical": form.notify_critical.data,
            "notify_reports": form.notify_reports.data,
=======
    def notification_settings(

        self,

        form

    ):

        return {

            "enable_notifications":

                form.enable_notifications.data,

            "notify_scan_complete":

                form.notify_scan_complete.data,

            "notify_scan_failed":

                form.notify_scan_failed.data,

            "notify_critical":

                form.notify_critical.data,

            "notify_reports":

                form.notify_reports.data

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # ==================================================
    # System Information
    # ==================================================

    def system_information(self):

        return {
<<<<<<< HEAD
            "cloudshield": "Enterprise v1.0",
            "python": sys.version.split()[0],
            "flask": flask.__version__,
            "platform": platform.system(),
            "platform_release": platform.release(),
            "database": db.engine.name,
            "assets": Asset.query.count(),
            "scans": SecurityScan.query.count(),
            "findings": Finding.query.count(),
            "users": User.query.count(),
=======

            "cloudshield":

                "Enterprise v1.0",

            "python":

                sys.version.split()[0],

            "flask":

                flask.__version__,

            "platform":

                platform.system(),

            "platform_release":

                platform.release(),

            "database":

                db.engine.name,

            "assets":

                Asset.query.count(),

            "scans":

                SecurityScan.query.count(),

            "findings":

                Finding.query.count(),

            "users":

                User.query.count()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

    # ==================================================
    # Dashboard Data
    # ==================================================

<<<<<<< HEAD
    def dashboard(self, user):

        return {"user": user, "system": self.system_information()}
=======
    def dashboard(

        self,

        user

    ):

        return {

            "user": user,

            "system": self.system_information()

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
