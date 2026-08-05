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

<<<<<<< HEAD
    scans = SecurityScan.query.order_by(SecurityScan.started_at.desc()).all()

    return render_template("reports/history.html", scans=scans)
=======
    scans = (
        SecurityScan.query
        .order_by(SecurityScan.started_at.desc())
        .all()
    )

    return render_template(
        "reports/history.html",
        scans=scans
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
