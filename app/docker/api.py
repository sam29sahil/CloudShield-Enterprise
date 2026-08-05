"""
CloudShield Enterprise
Docker API
"""

from flask import Blueprint

from flask_login import login_required

from app.api.responses import success_response

from app.docker.services import DockerDashboardService
from app.docker.report import DockerReport

<<<<<<< HEAD
docker_api = Blueprint("docker_api", __name__, url_prefix="/api/docker")
=======
docker_api = Blueprint(

    "docker_api",

    __name__,

    url_prefix="/api/docker"

)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

service = DockerDashboardService()

report = DockerReport()


# ----------------------------------
# Dashboard
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker_api.route("/dashboard")
@login_required
def dashboard():

<<<<<<< HEAD
    return success_response(data=service.dashboard(), message="Docker dashboard")
=======
    return success_response(

        data=service.dashboard(),

        message="Docker dashboard"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# ----------------------------------
# Containers
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker_api.route("/containers")
@login_required
def containers():

<<<<<<< HEAD
    return success_response(data=service.containers())
=======
    return success_response(

        data=service.containers()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# ----------------------------------
# Images
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker_api.route("/images")
@login_required
def images():

<<<<<<< HEAD
    return success_response(data=service.images())
=======
    return success_response(

        data=service.images()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# ----------------------------------
# Networks
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker_api.route("/networks")
@login_required
def networks():

<<<<<<< HEAD
    return success_response(data=service.networks())
=======
    return success_response(

        data=service.networks()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# ----------------------------------
# Volumes
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker_api.route("/volumes")
@login_required
def volumes():

<<<<<<< HEAD
    return success_response(data=service.volumes())
=======
    return success_response(

        data=service.volumes()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# ----------------------------------
# Report
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker_api.route("/report")
@login_required
def docker_report():

<<<<<<< HEAD
    return success_response(data=report.generate(), message="Docker report generated")
=======
    return success_response(

        data=report.generate(),

        message="Docker report generated"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
