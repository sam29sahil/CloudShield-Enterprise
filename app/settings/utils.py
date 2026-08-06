"""
CloudShield Enterprise
Settings Utilities
"""

import platform
import socket
import sys

import flask

from app.extensions import db

# ==================================================
# Application Information
# ==================================================


def app_information():

    return {
        "application": "CloudShield Enterprise",
        "version": "1.0",
        "python": sys.version.split()[0],
        "flask": flask.__version__,
        "database": db.engine.name,
    }


# ==================================================
# System Information
# ==================================================


def system_information():

    return {
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "release": platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
    }


# ==================================================
# Default Scanner Settings
# ==================================================


def default_scanner_settings():

    return {
        "default_mode": "basic",
        "default_category": "network",
        "timeout": 60,
        "save_history": True,
    }


# ==================================================
# Default Report Settings
# ==================================================


def default_report_settings():

    return {
        "company_name": "CloudShield Enterprise",
        "company_email": "",
        "company_website": "",
        "default_format": "pdf",
        "include_summary": True,
        "include_recommendations": True,
        "include_raw": True,
    }


# ==================================================
# Default Notification Settings
# ==================================================


def default_notification_settings():

    return {
        "enable_notifications": True,
        "notify_scan_complete": True,
        "notify_scan_failed": True,
        "notify_critical": True,
        "notify_reports": True,
    }
