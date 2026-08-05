"""
CloudShield Enterprise
Executive Dashboard
"""

from flask import Blueprint

<<<<<<< HEAD
executive = Blueprint("executive", __name__, url_prefix="/executive")

from app.executive import routes
=======
executive = Blueprint(

    "executive",

    __name__,

    url_prefix="/executive"

)

from app.executive import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
