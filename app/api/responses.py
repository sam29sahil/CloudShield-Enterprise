"""
CloudShield Enterprise
API Response Helpers
"""

from flask import jsonify


def success_response(
    data=None,
    message="Success",
    status_code=200
):
    """
    Standard success response.
    """

    response = {
        "success": True,
        "message": message,
        "data": data
    }

    return jsonify(response), status_code


def error_response(
    message="Error",
    status_code=400,
    errors=None
):
    """
    Standard error response.
    """

    response = {
        "success": False,
        "message": message,
        "errors": errors
    }

    return jsonify(response), status_code


def paginated_response(
    items,
    page,
    per_page,
    total,
    message="Success"
):
    """
    Standard paginated API response.
    """

    response = {
        "success": True,
        "message": message,
        "data": items,
        "pagination": {
            "page": page,
            "per_page": per_page,
            "total": total,
            "pages": (
                (total + per_page - 1) // per_page
                if per_page else 1
            )
        }
    }

    return jsonify(response), 200