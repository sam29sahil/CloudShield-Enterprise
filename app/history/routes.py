"""
CloudShield Enterprise
History Routes
"""

from flask import render_template
from flask_login import login_required

from app.history import history
from app.models import SecurityScan


@history.route("/")
@login_required
def index():
    """
    Scan History
    """

    scans = SecurityScan.query.order_by(SecurityScan.started_at.desc()).all()

    return render_template("reports/history.html", scans=scans)
