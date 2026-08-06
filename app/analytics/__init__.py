"""
CloudShield Enterprise
Analytics Module
"""

from flask import Blueprint

analytics = Blueprint("analytics", __name__, url_prefix="/analytics")

from app.analytics import routes
