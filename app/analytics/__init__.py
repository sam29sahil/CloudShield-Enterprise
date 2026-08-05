"""
CloudShield Enterprise
Analytics Module
"""

from flask import Blueprint

<<<<<<< HEAD
analytics = Blueprint("analytics", __name__, url_prefix="/analytics")

from app.analytics import routes
=======
analytics = Blueprint(
    "analytics",
    __name__,
    url_prefix="/analytics"
)

from app.analytics import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
