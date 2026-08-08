"""
CloudShield Enterprise
Findings UI Module
"""

from flask import Blueprint

findings_ui = Blueprint("findings_ui", __name__, url_prefix="/findings")

from app.findings_ui import routes
