"""
CloudShield Enterprise
Projects API
"""

from flask import request
from flask_login import login_required

from app.api import api
from app.api.responses import success_response, error_response
from app.services.project_service import ProjectService

project_service = ProjectService()


@api.route("/projects", methods=["GET"])
@login_required
def get_projects():
    """
    Get all projects.
    """

    projects = project_service.all()

    data = []

    for project in projects:

<<<<<<< HEAD
        data.append(
            {
                "id": project.id,
                "name": project.name,
                "description": project.description,
                "owner": project.owner,
                "created_at": (
                    project.created_at.isoformat() if project.created_at else None
                ),
            }
        )

    return success_response(data=data, message="Projects retrieved successfully")
=======
        data.append({

            "id": project.id,

            "name": project.name,

            "description": project.description,

            "owner": project.owner,

            "created_at": (
                project.created_at.isoformat()
                if project.created_at
                else None
            )

        })

    return success_response(

        data=data,

        message="Projects retrieved successfully"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@api.route("/projects/<int:project_id>", methods=["GET"])
@login_required
def get_project(project_id):
    """
    Get project by ID.
    """

    project = project_service.get(project_id)

    if not project:

<<<<<<< HEAD
        return error_response("Project not found", 404)

    data = {
        "id": project.id,
        "name": project.name,
        "description": project.description,
        "owner": project.owner,
        "created_at": (project.created_at.isoformat() if project.created_at else None),
    }

    return success_response(data=data, message="Project retrieved successfully")
=======
        return error_response(

            "Project not found",

            404

        )

    data = {

        "id": project.id,

        "name": project.name,

        "description": project.description,

        "owner": project.owner,

        "created_at": (
            project.created_at.isoformat()
            if project.created_at
            else None
        )

    }

    return success_response(

        data=data,

        message="Project retrieved successfully"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@api.route("/projects", methods=["POST"])
@login_required
def create_project():
    """
    Create a new project.
    """

    data = request.get_json()

    if not data:

<<<<<<< HEAD
        return error_response("JSON data is required", 400)
=======
        return error_response(

            "JSON data is required",

            400

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    name = data.get("name")
    description = data.get("description", "")
    owner = data.get("owner", "")

    if not name:

<<<<<<< HEAD
        return error_response("Project name is required", 400)

    project = project_service.create(name=name, description=description, owner=owner)

    return success_response(
        data={"id": project.id, "name": project.name},
        message="Project created successfully",
        status_code=201,
=======
        return error_response(

            "Project name is required",

            400

        )

    project = project_service.create(

        name=name,

        description=description,

        owner=owner

    )

    return success_response(

        data={

            "id": project.id,

            "name": project.name

        },

        message="Project created successfully",

        status_code=201

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/projects/<int:project_id>", methods=["DELETE"])
@login_required
def delete_project(project_id):
    """
    Delete project.
    """

    project = project_service.get(project_id)

    if not project:

<<<<<<< HEAD
        return error_response("Project not found", 404)

    project_service.delete(project_id)

    return success_response(message="Project deleted successfully")
=======
        return error_response(

            "Project not found",

            404

        )

    project_service.delete(project_id)

    return success_response(

        message="Project deleted successfully"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
