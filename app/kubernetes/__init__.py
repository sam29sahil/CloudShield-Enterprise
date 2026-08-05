"""
CloudShield Enterprise
Kubernetes Module
"""

from flask import Blueprint

<<<<<<< HEAD
kubernetes = Blueprint("kubernetes", __name__, url_prefix="/kubernetes")

from app.kubernetes import routes
=======
kubernetes = Blueprint(
    "kubernetes",
    __name__,
    url_prefix="/kubernetes"
)

from app.kubernetes import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
