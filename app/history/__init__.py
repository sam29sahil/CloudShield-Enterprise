"""
CloudShield Enterprise
History Module
"""

from flask import Blueprint

<<<<<<< HEAD
history = Blueprint("history", __name__, url_prefix="/history")

from app.history import routes
=======
history = Blueprint(

    "history",

    __name__,

    url_prefix="/history"

)

from app.history import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
