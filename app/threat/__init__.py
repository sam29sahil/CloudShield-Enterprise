"""
CloudShield Enterprise
Threat Intelligence Blueprint
"""

from flask import Blueprint

<<<<<<< HEAD
threat = Blueprint("threat", __name__, url_prefix="/threat")

from app.threat import routes
=======
threat = Blueprint(
    "threat",
    __name__,
    url_prefix="/threat"
)

from app.threat import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
