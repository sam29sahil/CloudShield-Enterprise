"""
CloudShield Enterprise
Executive Dashboard Routes
"""

from flask import render_template
from flask_login import login_required

from app.executive import executive
from app.executive.services import ExecutiveService


service = ExecutiveService()


@executive.route("/")
@login_required
def dashboard():

    return render_template(

        "executive/dashboard.html",

        summary=service.summary(),

        risks=service.top_risks(),

        recommendations=service.recommendations(),

        compliance=service.compliance()

    )