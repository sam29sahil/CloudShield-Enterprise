"""
CloudShield Enterprise
<<<<<<< HEAD
Cloud Blueprint
=======
Cloud Module
>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
"""

from flask import Blueprint

cloud = Blueprint(
    "cloud",
    __name__,
<<<<<<< HEAD
    url_prefix="/cloud",
    template_folder="../templates/cloud"
)

# Import routes after creating blueprint
=======
    url_prefix="/cloud"
)

>>>>>>> 85b73280dbe0ae93cb04b6fe019fa37bd58bbd40
from app.cloud import routes