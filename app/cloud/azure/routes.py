"""
CloudShield Enterprise
Azure Routes
"""

from __future__ import annotations

import logging

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from flask_login import login_required

from app.cloud.azure.client import AzureClient
from app.cloud.azure.security_service import AzureSecurityService

logger = logging.getLogger(__name__)

azure_bp = Blueprint("azure", __name__, url_prefix="/cloud/azure")

# --------------------------------------------------
# Azure Home
# --------------------------------------------------


@azure_bp.route("/")
@login_required
def index():

    return render_template("cloud/azure/index.html")


# --------------------------------------------------
# Azure Home
# --------------------------------------------------


@azure_bp.route("/")
@login_required
def index():

    return render_template("cloud/azure/index.html")


# --------------------------------------------------
# Dashboard
# --------------------------------------------------


@azure_bp.route("/dashboard")
@login_required
def dashboard():

    return render_template("cloud/azure/dashboard.html", report=None)


# --------------------------------------------------
# Run Azure Assessment
# --------------------------------------------------


@azure_bp.route("/scan", methods=["POST"])
@login_required
def scan():

    subscription_id = request.form.get("subscription_id")

    if not subscription_id:

        flash("Azure Subscription ID is required.", "danger")

        return redirect(url_for("azure.index"))

    try:

        client = AzureClient(subscription_id)

        if not client.test_connection():

            flash("Unable to connect to Azure.", "danger")

            return redirect(url_for("azure.index"))

        service = AzureSecurityService(client)

        report = service.scan()

        logger.info("Azure assessment completed.")

        return render_template("cloud/azure/dashboard.html", report=report)

    except Exception as error:

        logger.exception("Azure assessment failed: %s", error)

        flash(str(error), "danger")

        return redirect(url_for("azure.index"))


def init_app(app):

    app.register_blueprint(azure_bp)
