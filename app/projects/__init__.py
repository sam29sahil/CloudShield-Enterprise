"""
CloudShield Enterprise
Projects Module
"""

from flask import Blueprint

<<<<<<< HEAD
projects = Blueprint("projects", __name__, url_prefix="/projects")

from app.projects import routes
=======
projects = Blueprint(

    "projects",

    __name__,

    url_prefix="/projects"

)

from app.projects import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
