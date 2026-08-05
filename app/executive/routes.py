"""
CloudShield Enterprise
Executive Dashboard Routes
"""

from flask import render_template
from flask_login import login_required

from app.executive import executive
from app.executive.services import ExecutiveService

<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
service = ExecutiveService()


@executive.route("/")
@login_required
def dashboard():

    return render_template(
<<<<<<< HEAD
        "executive/dashboard.html",
        summary=service.summary(),
        risks=service.top_risks(),
        recommendations=service.recommendations(),
        compliance=service.compliance(),
    )
=======

        "executive/dashboard.html",

        summary=service.summary(),

        risks=service.top_risks(),

        recommendations=service.recommendations(),

        compliance=service.compliance()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
