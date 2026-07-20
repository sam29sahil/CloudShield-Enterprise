"""
CloudShield Enterprise
Docker Blueprint
"""

from flask import Blueprint

docker = Blueprint(

    "docker",

    __name__,

    url_prefix="/docker",

    template_folder="../templates/docker"

)

from app.docker import routes