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
            return error_response(
                "Authentication required",
                401
            )

        if not getattr(current_user, "is_admin", False):
            return error_response(
                "Admin access required",
                403
            )

        return func(*args, **kwargs)

    return wrapper

# ------------------------------------------
# API Login Required
# ------------------------------------------

def api_login_required(func):

    @wraps(func)

    def wrapper(*args, **kwargs):

        if not current_user.is_authenticated:

            return error_response(

                "Authentication required",

                401

            )

        return func(*args, **kwargs)

    return wrapper


# ------------------------------------------
# Role Required
# ------------------------------------------

def role_required(role):

    def decorator(func):

        @wraps(func)

        def wrapper(*args, **kwargs):

            if not current_user.is_authenticated:

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

            return func(*args, **kwargs)

        return wrapper

    return decorator 