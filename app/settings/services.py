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
from app.models import Asset, Finding, SecurityScan, User


class SettingsService:

    # ==================================================
    # Profile
    # ==================================================

    def update_profile(self, user, form):

        user.full_name = form.full_name.data

        user.username = form.username.data

        user.email = form.email.data

        db.session.commit()

        return True

    # ==================================================
    # Password
    # ==================================================

    def change_password(self, user, form):

        if not check_password_hash(user.password, form.current_password.data):

            return False, "Current password is incorrect."

        user.password = generate_password_hash(form.new_password.data)

        db.session.commit()

        return True, "Password updated successfully."

    # ==================================================
    # Scanner Settings
    # ==================================================

    def scanner_settings(self, form):

        return {
            "default_mode": form.default_mode.data,
            "default_category": form.default_category.data,
            "timeout": form.timeout.data,
            "save_history": form.save_history.data,
        }

    # ==================================================
    # Report Settings
    # ==================================================

    def report_settings(self, form):

        return {
            "company_name": form.company_name.data,
            "company_email": form.company_email.data,
            "company_website": form.company_website.data,
            "default_format": form.default_format.data,
            "include_summary": form.include_summary.data,
            "include_recommendations": form.include_recommendations.data,
            "include_raw": form.include_raw.data,
        }

    # ==================================================
    # Notification Settings
    # ==================================================

    def notification_settings(self, form):

        return {
            "enable_notifications": form.enable_notifications.data,
            "notify_scan_complete": form.notify_scan_complete.data,
            "notify_scan_failed": form.notify_scan_failed.data,
            "notify_critical": form.notify_critical.data,
            "notify_reports": form.notify_reports.data,
        }

    # ==================================================
    # System Information
    # ==================================================

    def system_information(self):

        return {
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
        }

    # ==================================================
    # Dashboard Data
    # ==================================================

    def dashboard(self, user):

        return {"user": user, "system": self.system_information()}
