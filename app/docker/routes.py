"""
CloudShield Enterprise
Docker Routes
"""

from flask import (
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import login_required

from app.docker import docker
from app.docker.services import DockerDashboardService


service = DockerDashboardService()


# ----------------------------------
# Dashboard
# ----------------------------------

@docker.route("/")
@login_required
def index():

    return render_template(

        "docker/index.html",

        summary=service.summary(),

        info=service.information()

    )


# ----------------------------------
# Containers
# ----------------------------------

@docker.route("/containers")
@login_required
def containers():

    return render_template(

        "docker/containers.html",

        containers=service.containers(),

    )


# ----------------------------------
# Images
# ----------------------------------

@docker.route("/images")
@login_required
def images():

    return render_template(

        "docker/images.html",

        images=service.images()

    )


# ----------------------------------
# Networks
# ----------------------------------

@docker.route("/networks")
@login_required
def networks():

    return render_template(

        "docker/networks.html",

        networks=service.networks()

    )


# ----------------------------------
# Volumes
# ----------------------------------

@docker.route("/volumes")
@login_required
def volumes():

    return render_template(

        "docker/volumes.html",

        volumes=service.volumes()

    )


# ----------------------------------
# Details
# ----------------------------------

@docker.route("/details/<container_id>")
@login_required
def details(container_id):

    data = service.details(container_id)

    if not data:

        flash(

            "Container not found.",

            "danger"

        )

        return redirect(

            url_for("docker.containers")

        )

    return render_template(

        "docker/details.html",

        data=data

    )


# ----------------------------------
# Start
# ----------------------------------

@docker.route("/start/<container_id>")
@login_required
def start(container_id):

    service.start(container_id)

    flash(

        "Container started.",

        "success"

    )

    return redirect(

        url_for("docker.containers")

    )


# ----------------------------------
# Stop
# ----------------------------------

@docker.route("/stop/<container_id>")
@login_required
def stop(container_id):

    service.stop(container_id)

    flash(

        "Container stopped.",

        "warning"

    )

    return redirect(

        url_for("docker.containers")

    )


# ----------------------------------
# Restart
# ----------------------------------

@docker.route("/restart/<container_id>")
@login_required
def restart(container_id):

    service.restart(container_id)

    flash(

        "Container restarted.",

        "info"

    )

    return redirect(

        url_for("docker.containers")

    )


# ----------------------------------
# Remove
# ----------------------------------

@docker.route("/remove/<container_id>")
@login_required
def remove(container_id):

    service.remove(container_id)

    flash(

        "Container removed.",

        "danger"

    )

    return redirect(

        url_for("docker.containers")

    )