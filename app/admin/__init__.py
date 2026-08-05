"""
CloudShield Enterprise
Admin Module
"""

from flask import Blueprint

<<<<<<< HEAD
admin = Blueprint("admin", __name__, url_prefix="/admin")

from app.admin import routes
=======
admin = Blueprint(

    "admin",

    __name__,

    url_prefix="/admin"

)

from app.admin import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
