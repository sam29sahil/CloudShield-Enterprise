from flask import Blueprint

<<<<<<< HEAD
dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")

from app.dashboard import routes
from app.dashboard import history_routes
=======
dashboard = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard"
)

from app.dashboard import routes
from app.dashboard import history_routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
