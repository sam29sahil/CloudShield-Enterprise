"""
CloudShield Enterprise
API Decorators
"""

from functools import wraps
from flask_login import current_user
from app.api.responses import error_response


def admin_required(func):
    """
    Restrict endpoint to admin users.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not current_user.is_authenticated:
<<<<<<< HEAD
            return error_response("Authentication required", 401)

        if not getattr(current_user, "is_admin", False):
            return error_response("Admin access required", 403)
=======
            return error_response(
                "Authentication required",
                401
            )

        if not getattr(current_user, "is_admin", False):
            return error_response(
                "Admin access required",
                403
            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return func(*args, **kwargs)

    return wrapper

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# ------------------------------------------
# API Login Required
# ------------------------------------------

<<<<<<< HEAD

def api_login_required(func):

    @wraps(func)
=======
def api_login_required(func):

    @wraps(func)

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    def wrapper(*args, **kwargs):

        if not current_user.is_authenticated:

<<<<<<< HEAD
            return error_response("Authentication required", 401)
=======
            return error_response(

                "Authentication required",

                401

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return func(*args, **kwargs)

    return wrapper


# ------------------------------------------
# Role Required
# ------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
def role_required(role):

    def decorator(func):

        @wraps(func)
<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        def wrapper(*args, **kwargs):

            if not current_user.is_authenticated:

<<<<<<< HEAD
                return error_response("Authentication required", 401)

            user_role = getattr(current_user, "role", None)

            if user_role != role:

                return error_response("Permission denied", 403)
=======
                return error_response(

                    "Authentication required",

                    401

                )

            user_role = getattr(

                current_user,

                "role",

                None

            )

            if user_role != role:

                return error_response(

                    "Permission denied",

                    403

                )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            return func(*args, **kwargs)

        return wrapper

<<<<<<< HEAD
    return decorator
=======
    return decorator 
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
