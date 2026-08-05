"""
CloudShield Enterprise
Notifications Blueprint
"""

from flask import Blueprint

<<<<<<< HEAD
notifications = Blueprint("notifications", __name__, url_prefix="/notifications")

from app.notifications import routes
=======
notifications = Blueprint(

    "notifications",

    __name__,

    url_prefix="/notifications"

)

from app.notifications import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
