"""
CloudShield Enterprise
Threat Intelligence Blueprint
"""

from flask import Blueprint

threat = Blueprint(
    "threat",
    __name__,
    url_prefix="/threat"
)

from app.threat import routes