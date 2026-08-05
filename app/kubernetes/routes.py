"""
CloudShield Enterprise
Kubernetes Routes
"""

<<<<<<< HEAD
from flask import render_template, abort
=======
from flask import (
    render_template,
    abort
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
from flask_login import login_required

from app.kubernetes import kubernetes
from app.kubernetes.report import KubernetesReport
from app.kubernetes.health import KubernetesHealth
from app.kubernetes.cluster import KubernetesCluster
from app.kubernetes.client import KubernetesClient

<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# --------------------------------------------------
# Helpers
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
def _report():

    return KubernetesReport().generate()


# --------------------------------------------------
# Dashboard
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@kubernetes.route("/")
@login_required
def index():

    report = _report()

    return render_template(
<<<<<<< HEAD
        "kubernetes/index.html",
        summary=report["dashboard"]["summary"],
        nodes=report["dashboard"]["nodes"],
        pods=report["dashboard"]["pods"],
        deployments=report["dashboard"]["deployments"],
        services=report["dashboard"]["services"],
        namespaces=report["dashboard"]["namespaces"],
        ingress=report["dashboard"]["ingress"],
        security=report["security"],
        recommendations=report["recommendations"],
=======

        "kubernetes/index.html",

        summary=report["dashboard"]["summary"],

        nodes=report["dashboard"]["nodes"],

        pods=report["dashboard"]["pods"],

        deployments=report["dashboard"]["deployments"],

        services=report["dashboard"]["services"],

        namespaces=report["dashboard"]["namespaces"],

        ingress=report["dashboard"]["ingress"],

        security=report["security"],

        recommendations=report["recommendations"]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# --------------------------------------------------
# Cluster
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@kubernetes.route("/cluster")
@login_required
def cluster():

    client = KubernetesClient()

    cluster = KubernetesCluster(client).info()

<<<<<<< HEAD
    return render_template("kubernetes/cluster.html", cluster=cluster)
=======
    return render_template(

        "kubernetes/cluster.html",

        cluster=cluster

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# --------------------------------------------------
# Nodes
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@kubernetes.route("/nodes")
@login_required
def nodes():

    report = _report()

<<<<<<< HEAD
    return render_template("kubernetes/nodes.html", nodes=report["dashboard"]["nodes"])
=======
    return render_template(

        "kubernetes/nodes.html",

        nodes=report["dashboard"]["nodes"]

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# --------------------------------------------------
# Pods
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@kubernetes.route("/pods")
@login_required
def pods():

    report = _report()

<<<<<<< HEAD
    return render_template("kubernetes/pods.html", pods=report["dashboard"]["pods"])
=======
    return render_template(

        "kubernetes/pods.html",

        pods=report["dashboard"]["pods"]

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# --------------------------------------------------
# Deployments
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@kubernetes.route("/deployments")
@login_required
def deployments():

    report = _report()

    return render_template(
<<<<<<< HEAD
        "kubernetes/deployments.html", deployments=report["dashboard"]["deployments"]
=======

        "kubernetes/deployments.html",

        deployments=report["dashboard"]["deployments"]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# --------------------------------------------------
# Services
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@kubernetes.route("/services")
@login_required
def services():

    report = _report()

    return render_template(
<<<<<<< HEAD
        "kubernetes/services.html", services=report["dashboard"]["services"]
=======

        "kubernetes/services.html",

        services=report["dashboard"]["services"]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# --------------------------------------------------
# Namespaces
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@kubernetes.route("/namespaces")
@login_required
def namespaces():

    report = _report()

    return render_template(
<<<<<<< HEAD
        "kubernetes/namespaces.html", namespaces=report["dashboard"]["namespaces"]
=======

        "kubernetes/namespaces.html",

        namespaces=report["dashboard"]["namespaces"]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# --------------------------------------------------
# Ingress
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@kubernetes.route("/ingress")
@login_required
def ingress():

    report = _report()

    return render_template(
<<<<<<< HEAD
        "kubernetes/ingress.html", ingress=report["dashboard"]["ingress"]
=======

        "kubernetes/ingress.html",

        ingress=report["dashboard"]["ingress"]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# --------------------------------------------------
# Security
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@kubernetes.route("/security")
@login_required
def security():

    report = _report()

    return render_template(
<<<<<<< HEAD
        "kubernetes/security.html",
        security=report["security"],
        recommendations=report["recommendations"],
=======

        "kubernetes/security.html",

        security=report["security"],

        recommendations=report["recommendations"]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# --------------------------------------------------
# Health
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@kubernetes.route("/health")
@login_required
def health():

    health = KubernetesHealth().status()

<<<<<<< HEAD
    return render_template("kubernetes/health.html", health=health)
=======
    return render_template(

        "kubernetes/health.html",

        health=health

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# --------------------------------------------------
# Details
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@kubernetes.route("/details/<resource_type>/<name>")
@login_required
def details(resource_type, name):

    report = _report()

    resources = report["dashboard"].get(resource_type)

    if not resources:

        abort(404)

    resource = None

    for item in resources:

        if item.get("name") == name:

            resource = item

            break

    if resource is None:

        abort(404)

<<<<<<< HEAD
    return render_template("kubernetes/details.html", resource=resource)
=======
    return render_template(

        "kubernetes/details.html",

        resource=resource

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
