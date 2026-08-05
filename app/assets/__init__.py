"""
CloudShield Enterprise
Assets Module
"""

from flask import Blueprint

<<<<<<< HEAD
assets = Blueprint("assets", __name__, url_prefix="/assets")

from app.assets import routes
=======
assets = Blueprint(

    "assets",

    __name__,

    url_prefix="/assets"

)

from app.assets import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
