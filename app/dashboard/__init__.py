from flask import Blueprint

dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")

from app.dashboard import routes
from app.dashboard import history_routes
