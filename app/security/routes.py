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

    result = None

    if form.validate_on_submit():

        result = service.scan(

            tool=form.tool.data,

            target=form.target.data,

            arguments=None

        )

    return render_template(

        "security/dashboard.html",

        form=form,

        result=result,

        tools=service.available_tools(),

        categories=service.categories()

    )