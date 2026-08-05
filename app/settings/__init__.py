"""
CloudShield Enterprise
Settings Blueprint
"""

from flask import Blueprint

settings = Blueprint(
    "settings",
    __name__,
    url_prefix="/settings",
    template_folder="../templates/settings",
)

from app.settings import routes
