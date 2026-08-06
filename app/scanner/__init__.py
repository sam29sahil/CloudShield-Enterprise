from flask import Blueprint

scanner = Blueprint("scanner", __name__, url_prefix="/scanner")

from app.scanner import routes
