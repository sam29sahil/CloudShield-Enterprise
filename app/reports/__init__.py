"""
CloudShield Enterprise
Reports Module
"""

from flask import Blueprint

<<<<<<< HEAD
reports = Blueprint("reports", __name__, url_prefix="/reports")

from app.reports import routes
=======
reports = Blueprint(
    "reports",
    __name__,
    url_prefix="/reports"
)

from app.reports import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
