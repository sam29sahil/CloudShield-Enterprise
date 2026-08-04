"""
CloudShield Enterprise
Security Routes
"""

from flask import render_template
from flask import jsonify

from flask_login import login_required

from app.security import security
from app.security.services.security_service import SecurityService


# ==========================================================
# Security Dashboard
# ==========================================================

@security.route("/")
@login_required
def dashboard():

    service = SecurityService()

    dashboard = service.dashboard()

    return render_template(

        "security/dashboard.html",

        dashboard=dashboard

    )


# ==========================================================
# Findings
# ==========================================================

@security.route("/findings")
@login_required
def findings():

    service = SecurityService()

    findings = service.findings()

    return render_template(

        "security/findings.html",

        findings=findings

    )


# ==========================================================
# Reports
# ==========================================================

@security.route("/reports")
@login_required
def reports():

    service = SecurityService()

    reports = service.reports()

    return render_template(

        "security/reports.html",

        reports=reports

    )


# ==========================================================
# Threats
# ==========================================================

@security.route("/threats")
@login_required
def threats():

    service = SecurityService()

    threats = service.threats()

    return render_template(

        "security/threats.html",

        threats=threats

    )


# ==========================================================
# Statistics
# ==========================================================

@security.route("/statistics")
@login_required
def statistics():

    service = SecurityService()

    statistics = service.statistics()

    return render_template(

        "security/statistics.html",

        statistics=statistics

    )


# ==========================================================
# Dashboard API
# ==========================================================

@security.route("/api/dashboard")
@login_required
def dashboard_api():

    service = SecurityService()

    return jsonify(

        service.dashboard()

    )


# ==========================================================
# Findings API
# ==========================================================

@security.route("/api/findings")
@login_required
def findings_api():

    service = SecurityService()

    return jsonify(

        service.findings()

    )


# ==========================================================
# Reports API
# ==========================================================

@security.route("/api/reports")
@login_required
def reports_api():

    service = SecurityService()

    return jsonify(

        service.reports()

    )


# ==========================================================
# Threats API
# ==========================================================

@security.route("/api/threats")
@login_required
def threats_api():

    service = SecurityService()

    return jsonify(

        service.threats()

    )


# ==========================================================
# Statistics API
# ==========================================================

@security.route("/api/statistics")
@login_required
def statistics_api():

    service = SecurityService()

    return jsonify(

        service.statistics()

    )