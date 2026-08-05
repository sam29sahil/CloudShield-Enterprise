"""
CloudShield Enterprise
Findings UI Module
"""

from flask import Blueprint

<<<<<<< HEAD
findings_ui = Blueprint("findings_ui", __name__, url_prefix="/findings")

from app.findings_ui import routes
=======
findings_ui = Blueprint(

    "findings_ui",

    __name__,

    url_prefix="/findings"

)

from app.findings_ui import routes
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
