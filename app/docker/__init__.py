"""
CloudShield Enterprise
Docker Module
"""

from flask import Blueprint

<<<<<<< HEAD
docker = Blueprint("docker", __name__, url_prefix="/docker")

from app.docker import routes
=======
docker = Blueprint(
    "docker",
    __name__,
    url_prefix="/docker"
)

from app.docker import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
