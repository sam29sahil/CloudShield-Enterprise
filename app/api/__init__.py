from flask import Blueprint

# Main API Blueprint
<<<<<<< HEAD
api = Blueprint("api", __name__, url_prefix="/api")

# Import routes so Flask registers them
from app.api import routes
=======
api = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)

# Import routes so Flask registers them
from app.api import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
