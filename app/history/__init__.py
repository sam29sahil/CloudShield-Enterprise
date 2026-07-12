"""
CloudShield Enterprise
History Module
"""

from flask import Blueprint

history = Blueprint(

    "history",

    __name__,

    url_prefix="/history"

)

from app.history import routes