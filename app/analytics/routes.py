"""
CloudShield Enterprise
Analytics Routes
"""

from flask import render_template
from flask_login import login_required

from app.analytics import analytics
from app.analytics.services import AnalyticsService


service = AnalyticsService()


@analytics.route("/")
@login_required
def index():
    """
    Analytics Dashboard
    """

    statistics = service.statistics()

    charts = service.chart_data()

    return render_template(
        "analytics/index.html",
        statistics=statistics,
        charts=charts
    )