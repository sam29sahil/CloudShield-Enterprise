"""
CloudShield Enterprise
API Response Helpers
"""

from flask import jsonify


<<<<<<< HEAD
def success_response(data=None, message="Success", status_code=200):
=======
def success_response(
    data=None,
    message="Success",
    status_code=200
):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    """
    Standard success response.
    """

<<<<<<< HEAD
    response = {"success": True, "message": message, "data": data}
=======
    response = {
        "success": True,
        "message": message,
        "data": data
    }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    return jsonify(response), status_code


<<<<<<< HEAD
def error_response(message="Error", status_code=400, errors=None):
=======
def error_response(
    message="Error",
    status_code=400,
    errors=None
):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    """
    Standard error response.
    """

<<<<<<< HEAD
    response = {"success": False, "message": message, "errors": errors}
=======
    response = {
        "success": False,
        "message": message,
        "errors": errors
    }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    return jsonify(response), status_code


<<<<<<< HEAD
def paginated_response(items, page, per_page, total, message="Success"):
=======
def paginated_response(
    items,
    page,
    per_page,
    total,
    message="Success"
):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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
<<<<<<< HEAD
            "pages": ((total + per_page - 1) // per_page if per_page else 1),
        },
=======
            "pages": (
                (total + per_page - 1) // per_page
                if per_page else 1
            )
        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    }

    return jsonify(response), 200

<<<<<<< HEAD

def validation_error(errors):

    return error_response(message="Validation Error", status_code=422, errors=errors)
=======
def validation_error(errors):

    return error_response(

        message="Validation Error",

        status_code=422,

        errors=errors

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


def unauthorized():

<<<<<<< HEAD
    return error_response(message="Unauthorized", status_code=401)
=======
    return error_response(

        message="Unauthorized",

        status_code=401

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


def forbidden():

<<<<<<< HEAD
    return error_response(message="Forbidden", status_code=403)
=======
    return error_response(

        message="Forbidden",

        status_code=403

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


def not_found(resource="Resource"):

<<<<<<< HEAD
    return error_response(message=f"{resource} not found", status_code=404)
=======
    return error_response(

        message=f"{resource} not found",

        status_code=404

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
