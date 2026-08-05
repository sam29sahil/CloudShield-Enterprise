"""
CloudShield Enterprise
Analytics Routes
"""

from flask import render_template
from flask_login import login_required

from app.analytics import analytics
from app.analytics.services import AnalyticsService

<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
service = AnalyticsService()


@analytics.route("/")
@login_required
def index():
    """
    Enterprise Analytics Dashboard
    """

    data = service.dashboard_data()

    return render_template(
<<<<<<< HEAD
        "analytics/dashboard.html",
        summary=data["summary"],
        statistics=data["statistics"],
        severity=data["severity"],
        charts=data["charts"],
        trend=data["trend"],
        recent=data["recent_scans"],
        assets=data["top_assets"],
        scanner_usage=data["scanner_usage"],
        vulnerabilities=data["top_vulnerabilities"],
        performance=data["performance"],
        cloud=data["cloud"],
    )
=======

        "analytics/dashboard.html",

        summary=data["summary"],

        statistics=data["statistics"],

        severity=data["severity"],

        charts=data["charts"],

        trend=data["trend"],

        recent=data["recent_scans"],

        assets=data["top_assets"],

        scanner_usage=data["scanner_usage"],

        vulnerabilities=data["top_vulnerabilities"],

        performance=data["performance"],

        cloud=data["cloud"]

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
