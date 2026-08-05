"""
CloudShield Enterprise
Assets Module
"""

from flask import Blueprint

assets = Blueprint("assets", __name__, url_prefix="/assets")

from app.assets import routes
