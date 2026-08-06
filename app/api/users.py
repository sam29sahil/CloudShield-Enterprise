"""
CloudShield Enterprise
Users API
"""

from flask import request
from flask_login import login_required

from app.api import api
from app.api.responses import success_response, error_response
from app.services.user_service import UserService

user_service = UserService()


@api.route("/users", methods=["GET"])
@login_required
def get_users():

    users = user_service.all()

    data = []

    for user in users:

        data.append(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
                "created_at": (
                    user.created_at.isoformat() if user.created_at else None
                ),
            }
        )

    return success_response(data=data, message="Users retrieved successfully")


@api.route("/users/<int:user_id>", methods=["GET"])
@login_required
def get_user(user_id):

    user = user_service.get(user_id)

    if not user:
        return error_response("User not found", 404)

    return success_response(
        data={
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "created_at": (user.created_at.isoformat() if user.created_at else None),
        }
    )


@api.route("/users", methods=["POST"])
@login_required
def create_user():

    data = request.get_json()

    if not data:
        return error_response("No JSON data received", 400)

    required = ["username", "email", "password"]

    for field in required:

        if field not in data:
            return error_response(f"{field} is required", 400)

    user = user_service.create(
        username=data["username"],
        email=data["email"],
        password=data["password"],
        role=data.get("role", "User"),
    )

    return success_response(
        data={"id": user.id}, message="User created successfully", status_code=201
    )


@api.route("/users/<int:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id):

    deleted = user_service.delete(user_id)

    if not deleted:
        return error_response("User not found", 404)

    return success_response(message="User deleted successfully")
