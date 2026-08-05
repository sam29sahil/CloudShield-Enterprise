"""
CloudShield Enterprise
Settings Utilities
"""

import platform
import socket
import sys

import flask

from app.extensions import db

<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# ==================================================
# Application Information
# ==================================================

<<<<<<< HEAD

def app_information():

    return {
        "application": "CloudShield Enterprise",
        "version": "1.0",
        "python": sys.version.split()[0],
        "flask": flask.__version__,
        "database": db.engine.name,
=======
def app_information():

    return {

        "application": "CloudShield Enterprise",

        "version": "1.0",

        "python": sys.version.split()[0],

        "flask": flask.__version__,

        "database": db.engine.name

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    }


# ==================================================
# System Information
# ==================================================

<<<<<<< HEAD

def system_information():

    return {
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "release": platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
=======
def system_information():

    return {

        "hostname": socket.gethostname(),

        "operating_system": platform.system(),

        "release": platform.release(),

        "architecture": platform.machine(),

        "processor": platform.processor()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    }


# ==================================================
# Default Scanner Settings
# ==================================================

<<<<<<< HEAD

def default_scanner_settings():

    return {
        "default_mode": "basic",
        "default_category": "network",
        "timeout": 60,
        "save_history": True,
=======
def default_scanner_settings():

    return {

        "default_mode": "basic",

        "default_category": "network",

        "timeout": 60,

        "save_history": True

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    }


# ==================================================
# Default Report Settings
# ==================================================

<<<<<<< HEAD

def default_report_settings():

    return {
        "company_name": "CloudShield Enterprise",
        "company_email": "",
        "company_website": "",
        "default_format": "pdf",
        "include_summary": True,
        "include_recommendations": True,
        "include_raw": True,
=======
def default_report_settings():

    return {

        "company_name": "CloudShield Enterprise",

        "company_email": "",

        "company_website": "",

        "default_format": "pdf",

        "include_summary": True,

        "include_recommendations": True,

        "include_raw": True

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    }


# ==================================================
# Default Notification Settings
# ==================================================

<<<<<<< HEAD

def default_notification_settings():

    return {
        "enable_notifications": True,
        "notify_scan_complete": True,
        "notify_scan_failed": True,
        "notify_critical": True,
        "notify_reports": True,
    }
=======
def default_notification_settings():

    return {

        "enable_notifications": True,

        "notify_scan_complete": True,

        "notify_scan_failed": True,

        "notify_critical": True,

        "notify_reports": True

    }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
