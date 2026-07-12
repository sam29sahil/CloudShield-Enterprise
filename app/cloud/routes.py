"""
CloudShield Enterprise
Cloud Routes
"""

from flask import render_template
from flask_login import login_required

from app.cloud import cloud


@cloud.route("/")
@login_required
def dashboard():

    return render_template(
        "cloud/dashboard.html"
    )


@cloud.route("/aws")
@login_required
def aws():

    return render_template(
        "cloud/aws.html"
    )