from flask import render_template
from flask_login import login_required

from app.dashboard import dashboard
from app.models import SecurityScan

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@dashboard.route("/history")
@login_required
def history():

<<<<<<< HEAD
    scans = SecurityScan.query.order_by(SecurityScan.started_at.desc()).all()

    return render_template("scanner/history.html", scans=scans)
=======
    scans = (
        SecurityScan.query
        .order_by(SecurityScan.started_at.desc())
        .all()
    )

    return render_template(
        "scanner/history.html",
        scans=scans
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
