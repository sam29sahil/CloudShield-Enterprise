"""
CloudShield Enterprise
Security Module
"""

from flask import Blueprint

security = Blueprint(
    "security",
    __name__,
    url_prefix="/security"
)

from app.security import routes