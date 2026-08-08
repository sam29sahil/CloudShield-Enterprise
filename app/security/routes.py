"""
CloudShield Enterprise
Security Routes
"""

from flask import render_template
from flask_login import login_required

from app.security import security
from app.security.forms import SecurityScanForm
from app.security.services import SecurityService


service = SecurityService()


@security.route("/", methods=["GET", "POST"])
@login_required
def home():
    """
    Security Dashboard
    """

    form = SecurityScanForm()

    form.tool.choices = [
        ("", "-- Select Individual Tool --")
    ] + [
        (tool, tool.title())
        for tool in service.available_tools()
    ]

    result = None

    if form.validate_on_submit():

        if form.tool.data:

            result = service.scan(
                target=form.target.data,
                tool=form.tool.data
            )

        else:

            result = service.scan(
                target=form.target.data,
                profile=form.profile.data
            )

    return render_template(

        "security/dashboard.html",

        form=form,

        result=result,

        tools=service.available_tools(),

        categories=service.categories()

    )