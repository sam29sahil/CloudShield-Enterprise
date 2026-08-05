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

<<<<<<< HEAD
    return jsonify(service.dashboard_data())
=======
    return jsonify(

        service.dashboard_data()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@analytics.route("/api/charts")
@login_required
def charts_api():

<<<<<<< HEAD
    return jsonify(service.chart_data())
=======
    return jsonify(

        service.chart_data()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@analytics.route("/api/statistics")
@login_required
def statistics_api():

<<<<<<< HEAD
    return jsonify(service.statistics())
=======
    return jsonify(

        service.statistics()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
