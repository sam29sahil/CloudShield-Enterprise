"""
CloudShield Enterprise
Authentication API
"""

from flask import request
from flask_login import login_required, current_user

from app.api import api
from app.api.responses import success_response, error_response


@api.route("/auth/profile", methods=["GET"])
@login_required
def profile():
    """
    Current logged-in user.
    """

    return success_response(
        data={
            "id": current_user.id,
            "username": current_user.username,
            "email": current_user.email,
        },
        message="Profile fetched successfully",
    )


@api.route("/auth/status", methods=["GET"])
def status():

    if current_user.is_authenticated:

        return success_response(
            data={"authenticated": True, "username": current_user.username}
        )

    return error_response(message="Not authenticated", status_code=401)
