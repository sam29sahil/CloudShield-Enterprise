from flask import Blueprint

# Main API Blueprint
api = Blueprint("api", __name__, url_prefix="/api")

# Import routes so Flask registers them
from app.api import routes
