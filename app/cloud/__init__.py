"""
CloudShield Enterprise
Cloud Security Module
"""

from flask import Blueprint

cloud = Blueprint(
    "cloud", __name__, template_folder="templates", static_folder="static"
)

from app.cloud import routes
