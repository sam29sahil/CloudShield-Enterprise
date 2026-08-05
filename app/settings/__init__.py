"""
CloudShield Enterprise
Settings Blueprint
"""

from flask import Blueprint

settings = Blueprint(
<<<<<<< HEAD
    "settings",
    __name__,
    url_prefix="/settings",
    template_folder="../templates/settings",
)

from app.settings import routes
=======

    "settings",

    __name__,

    url_prefix="/settings",

    template_folder="../templates/settings"

)

from app.settings import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
