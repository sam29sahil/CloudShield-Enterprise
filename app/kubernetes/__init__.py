"""
CloudShield Enterprise
Kubernetes Module
"""

from flask import Blueprint

kubernetes = Blueprint(
    "kubernetes",
    __name__,
    url_prefix="/kubernetes"
)

from app.kubernetes import routes