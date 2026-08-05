from flask import Blueprint

<<<<<<< HEAD
auth = Blueprint("auth", __name__, url_prefix="/auth")

from app.auth import routes
=======
auth = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)

from app.auth import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
