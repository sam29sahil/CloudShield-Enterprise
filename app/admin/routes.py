"""
CloudShield Enterprise
Admin Routes
"""

from flask import render_template
from flask_login import login_required

from app.admin import admin
from app.models import User, SecurityScan


@admin.route("/")
@login_required
def dashboard():

    total_users = User.query.count()

    total_scans = SecurityScan.query.count()

    completed = SecurityScan.query.filter_by(
        status="Completed"
    ).count()

    failed = SecurityScan.query.filter_by(
        status="Failed"
    ).count()

    high_risk = SecurityScan.query.filter_by(
        risk="High"
    ).count()

    critical_risk = SecurityScan.query.filter_by(
        risk="Critical"
    ).count()

    recent_scans = (
        SecurityScan.query
        .order_by(
            SecurityScan.started_at.desc()
        )
        .limit(10)
        .all()
    )

    return render_template(
        "admin/dashboard.html",
        total_users=total_users,
        total_scans=total_scans,
        completed=completed,
        failed=failed,
        high_risk=high_risk,
        critical_risk=critical_risk,
        recent_scans=recent_scans
    )


@admin.route("/users")
@login_required
def users():

    users = (
        User.query
        .order_by(User.id.asc())
        .all()
    )

    return render_template(
        "admin/users.html",
        users=users
    )


@admin.route("/scans")
@login_required
def scans():

    scans = (
        SecurityScan.query
        .order_by(
            SecurityScan.started_at.desc()
        )
        .all()
    )

    total_scans = SecurityScan.query.count()

    completed = SecurityScan.query.filter_by(
        status="Completed"
    ).count()

    running = SecurityScan.query.filter_by(
        status="Running"
    ).count()

    failed = SecurityScan.query.filter_by(
        status="Failed"
    ).count()

    high_risk = SecurityScan.query.filter_by(
        risk="High"
    ).count()

    critical_risk = SecurityScan.query.filter_by(
        risk="Critical"
    ).count()

    medium_risk = SecurityScan.query.filter_by(
        risk="Medium"
    ).count()

    low_risk = SecurityScan.query.filter_by(
        risk="Low"
    ).count()

    return render_template(
        "admin/scans.html",
        scans=scans,
        total_scans=total_scans,
        completed=completed,
        running=running,
        failed=failed,
        high_risk=high_risk,
        critical_risk=critical_risk,
        medium_risk=medium_risk,
        low_risk=low_risk
    )