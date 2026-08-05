"""
CloudShield Enterprise
Docker Routes
"""

<<<<<<< HEAD
from flask import render_template, redirect, url_for, flash
=======
from flask import (
    render_template,
    redirect,
    url_for,
    flash
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

from flask_login import login_required

from app.docker import docker
from app.docker.services import DockerDashboardService

<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
service = DockerDashboardService()


# ----------------------------------
# Dashboard
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/")
@login_required
def index():

    return render_template(
<<<<<<< HEAD
        "docker/index.html",
        summary=service.summary(),
        info=service.information(),
        security=service.security_summary(),
        containers=service.containers(),
        images=service.images(),
        networks=service.networks(),
        volumes=service.volumes(),
=======

        "docker/index.html",

        summary=service.summary(),

        info=service.information(),

        security=service.security_summary(),

        containers=service.containers(),

        images=service.images(),

        networks=service.networks(),

        volumes=service.volumes()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# ----------------------------------
# Containers
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/containers")
@login_required
def containers():

    return render_template(
<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        "docker/containers.html",
        summary=service.summary(),
        security=service.security_summary(),
        images=service.images(),
        containers=service.containers(),
        networks=service.networks(),
<<<<<<< HEAD
        volumes=service.volumes(),
=======
        volumes=service.volumes()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# ----------------------------------
# Images
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/images")
@login_required
def images():

    return render_template(
<<<<<<< HEAD
        "docker/images.html",
        images=service.images(),
        summary=service.summary(),
        info=service.information(),
        security=service.security_summary(),
    )

=======

        "docker/images.html",

        images=service.images(),

        summary=service.summary(),

        info=service.information(),

        security=service.security_summary()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# ----------------------------------
# Networks
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/networks")
@login_required
def networks():

<<<<<<< HEAD
    return render_template("docker/networks.html", networks=service.networks())
=======
    return render_template(

        "docker/networks.html",

        networks=service.networks()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# ----------------------------------
# Volumes
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/volumes")
@login_required
def volumes():

<<<<<<< HEAD
    return render_template("docker/volumes.html", volumes=service.volumes())

=======
    return render_template(

        "docker/volumes.html",

        volumes=service.volumes()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# ----------------------------------
# Security
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/security")
@login_required
def security():

    return render_template(
        "docker/images.html",
        summary=service.summary(),
        security=service.security_summary(),
        images=service.images(),
        containers=service.containers(),
        networks=service.networks(),
<<<<<<< HEAD
        volumes=service.volumes(),
    )


=======
        volumes=service.volumes()
    )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# ----------------------------------
# Details
# ----------------------------------

<<<<<<< HEAD

@docker.route("/details/<container_id>")
@login_required
def details(container_id):

    service = DockerDashboardService()

=======
@docker.route("/details/<container_id>")
@login_required
def details(container_id):
     

    service = DockerDashboardService()
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    data = service.details(container_id)

    if not data:

<<<<<<< HEAD
        flash("Container not found.", "danger")

        return redirect(url_for("docker.containers"))

    return render_template("docker/details.html", data=data)
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# ----------------------------------
# Start
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/start/<container_id>")
@login_required
def start(container_id):

    service.start(container_id)

<<<<<<< HEAD
    flash("Container started.", "success")

    return redirect(url_for("docker.containers"))
=======
    flash(

        "Container started.",

        "success"

    )

    return redirect(

        url_for("docker.containers")

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# ----------------------------------
# Stop
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/stop/<container_id>")
@login_required
def stop(container_id):

    service.stop(container_id)

<<<<<<< HEAD
    flash("Container stopped.", "warning")

    return redirect(url_for("docker.containers"))
=======
    flash(

        "Container stopped.",

        "warning"

    )

    return redirect(

        url_for("docker.containers")

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# ----------------------------------
# Restart
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/restart/<container_id>")
@login_required
def restart(container_id):

    service.restart(container_id)

<<<<<<< HEAD
    flash("Container restarted.", "info")

    return redirect(url_for("docker.containers"))
=======
    flash(

        "Container restarted.",

        "info"

    )

    return redirect(

        url_for("docker.containers")

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# ----------------------------------
# Remove
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/remove/<container_id>")
@login_required
def remove(container_id):

    service.remove(container_id)

<<<<<<< HEAD
    flash("Container removed.", "danger")

    return redirect(url_for("docker.containers"))

=======
    flash(

        "Container removed.",

        "danger"

    )

    return redirect(

        url_for("docker.containers")

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# ----------------------------------
# Health
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/health")
@login_required
def health():

<<<<<<< HEAD
    return render_template("docker/health.html", health=service.health())

=======
    return render_template(

        "docker/health.html",

        health=service.health()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# ----------------------------------
# Dashboard API
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/dashboard")
@login_required
def dashboard():

    return service.dashboard()


# ----------------------------------
# Refresh
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/refresh")
@login_required
def refresh():

<<<<<<< HEAD
    flash("Docker information refreshed.", "success")

    return redirect(url_for("docker.index"))

=======
    flash(

        "Docker information refreshed.",

        "success"

    )

    return redirect(

        url_for("docker.index")

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# ----------------------------------
# Benchmark
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/benchmark")
@login_required
def benchmark():

<<<<<<< HEAD
    return render_template("docker/benchmark.html", benchmark=service.benchmark())
=======
    return render_template(

        "docker/benchmark.html",

        benchmark=service.benchmark()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# ----------------------------------
# Findings
# ----------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@docker.route("/findings")
@login_required
def findings():

<<<<<<< HEAD
    return render_template("docker/findings.html", findings=service.findings())
=======
    return render_template(

        "docker/findings.html",

        findings=service.findings()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
