"""
CloudShield Enterprise
Executive Dashboard
"""

from flask import Blueprint

executive = Blueprint("executive", __name__, url_prefix="/executive")

from app.executive import routes
