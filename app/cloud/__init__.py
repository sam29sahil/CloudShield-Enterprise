"""
CloudShield Enterprise
Cloud Module
"""

from flask import Blueprint

cloud = Blueprint(
    "cloud",
    __name__,
    url_prefix="/cloud"
)

from app.cloud import routes