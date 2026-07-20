"""
CloudShield Enterprise
Projects Module
"""

from flask import Blueprint

projects = Blueprint(

    "projects",

    __name__,

    url_prefix="/projects"

)

from app.projects import routes