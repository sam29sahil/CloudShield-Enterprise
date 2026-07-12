"""
CloudShield Enterprise
Settings Routes
"""

from flask import render_template
from flask_login import login_required, current_user

from app.settings import settings


@settings.route("/")
@login_required
def index():

    return render_template(

        "settings/index.html",

        user=current_user

    )