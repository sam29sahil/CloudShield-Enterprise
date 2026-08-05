"""
CloudShield Enterprise
API Error Handlers
"""

from app.api import api
from app.api.responses import error_response


@api.app_errorhandler(400)
def bad_request(error):
<<<<<<< HEAD
    return error_response(message="Bad Request", status_code=400)
=======
    return error_response(
        message="Bad Request",
        status_code=400
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@api.app_errorhandler(401)
def unauthorized(error):
<<<<<<< HEAD
    return error_response(message="Unauthorized", status_code=401)
=======
    return error_response(
        message="Unauthorized",
        status_code=401
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@api.app_errorhandler(403)
def forbidden(error):
<<<<<<< HEAD
    return error_response(message="Forbidden", status_code=403)
=======
    return error_response(
        message="Forbidden",
        status_code=403
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@api.app_errorhandler(404)
def not_found(error):
<<<<<<< HEAD
    return error_response(message="Resource Not Found", status_code=404)
=======
    return error_response(
        message="Resource Not Found",
        status_code=404
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@api.app_errorhandler(405)
def method_not_allowed(error):
<<<<<<< HEAD
    return error_response(message="Method Not Allowed", status_code=405)
=======
    return error_response(
        message="Method Not Allowed",
        status_code=405
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@api.app_errorhandler(500)
def internal_server_error(error):
<<<<<<< HEAD
    return error_response(message="Internal Server Error", status_code=500)
=======
    return error_response(
        message="Internal Server Error",
        status_code=500
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
