"""
CloudShield Enterprise
Docker API
"""

from flask import Blueprint

from flask_login import login_required

from app.api.responses import success_response

from app.docker.services import DockerDashboardService
from app.docker.report import DockerReport

docker_api = Blueprint(

    "docker_api",

    __name__,

    url_prefix="/api/docker"

)

service = DockerDashboardService()

report = DockerReport()


# ----------------------------------
# Dashboard
# ----------------------------------

@docker_api.route("/dashboard")
@login_required
def dashboard():

    return success_response(

        data=service.dashboard(),

        message="Docker dashboard"

    )


# ----------------------------------
# Containers
# ----------------------------------

@docker_api.route("/containers")
@login_required
def containers():

    return success_response(

        data=service.containers()

    )


# ----------------------------------
# Images
# ----------------------------------

@docker_api.route("/images")
@login_required
def images():

    return success_response(

        data=service.images()

    )


# ----------------------------------
# Networks
# ----------------------------------

@docker_api.route("/networks")
@login_required
def networks():

    return success_response(

        data=service.networks()

    )


# ----------------------------------
# Volumes
# ----------------------------------

@docker_api.route("/volumes")
@login_required
def volumes():

    return success_response(

        data=service.volumes()

    )


# ----------------------------------
# Report
# ----------------------------------

@docker_api.route("/report")
@login_required
def docker_report():

    return success_response(

        data=report.generate(),

        message="Docker report generated"

    )