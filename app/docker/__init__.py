"""
CloudShield Enterprise
Docker Module
"""

from flask import Blueprint

docker = Blueprint("docker", __name__, url_prefix="/docker")

from app.docker import routes
