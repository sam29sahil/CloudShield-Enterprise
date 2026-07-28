"""
CloudShield Enterprise

Cloud Blueprint

Cloud Module

"""

from flask import Blueprint

cloud = Blueprint(
    "cloud",
    __name__,
    url_prefix="/cloud",
    template_folder="../templates/cloud"
)

# Import routes after creating blueprint

from app.cloud import routes