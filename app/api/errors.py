"""
CloudShield Enterprise
API Error Handlers
"""

from app.api import api
from app.api.responses import error_response


@api.app_errorhandler(400)
def bad_request(error):
    return error_response(message="Bad Request", status_code=400)


@api.app_errorhandler(401)
def unauthorized(error):
    return error_response(message="Unauthorized", status_code=401)


@api.app_errorhandler(403)
def forbidden(error):
    return error_response(message="Forbidden", status_code=403)


@api.app_errorhandler(404)
def not_found(error):
    return error_response(message="Resource Not Found", status_code=404)


@api.app_errorhandler(405)
def method_not_allowed(error):
    return error_response(message="Method Not Allowed", status_code=405)


@api.app_errorhandler(500)
def internal_server_error(error):
    return error_response(message="Internal Server Error", status_code=500)
