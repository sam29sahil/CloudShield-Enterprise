"""
CloudShield Enterprise
<<<<<<< HEAD
Cloud Security Module
=======

Cloud Blueprint

Cloud Module

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
"""

from flask import Blueprint

<<<<<<< HEAD
cloud_bp = Blueprint(
    "cloud", __name__, template_folder="templates", static_folder="static"
)

from app.cloud import routes
=======
cloud = Blueprint(
    "cloud",
    __name__,
    url_prefix="/cloud",
    template_folder="../templates/cloud"
)

# Import routes after creating blueprint

from app.cloud import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
