"""
CloudShield Enterprise
Analytics API
"""

from flask import jsonify
from flask_login import login_required

from app.analytics import analytics
from app.analytics.services import AnalyticsService

service = AnalyticsService()


@analytics.route("/api/dashboard")
@login_required
def dashboard_api():

    return jsonify(service.dashboard_data())


@analytics.route("/api/charts")
@login_required
def charts_api():

    return jsonify(service.chart_data())


@analytics.route("/api/statistics")
@login_required
def statistics_api():

    return jsonify(service.statistics())
