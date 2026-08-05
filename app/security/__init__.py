"""
CloudShield Enterprise
Security Module
"""

from flask import Blueprint

<<<<<<< HEAD
security = Blueprint("security", __name__, url_prefix="/security")

from app.security import routes
=======
security = Blueprint(
    "security",
    __name__,
    url_prefix="/security"
)

from app.security import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
