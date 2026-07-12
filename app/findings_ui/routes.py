"""
CloudShield Enterprise
Findings Routes
"""

from flask import render_template
from flask_login import login_required

from app.findings_ui import findings_ui
from app.models import SecurityScan


@findings_ui.route("/")
@login_required
def index():

    scans = (

        SecurityScan.query

        .filter(

            SecurityScan.risk != "Unknown"

        )

        .order_by(

            SecurityScan.score.desc()

        )

        .all()

    )

    return render_template(

        "findings/index.html",

        scans=scans

    )