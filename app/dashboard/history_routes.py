from flask import render_template
from flask_login import login_required

from app.dashboard import dashboard
from app.models import SecurityScan


@dashboard.route("/history")
@login_required
def history():

    scans = SecurityScan.query.order_by(SecurityScan.started_at.desc()).all()

    return render_template("scanner/history.html", scans=scans)
