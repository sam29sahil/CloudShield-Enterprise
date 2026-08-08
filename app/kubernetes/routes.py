"""
CloudShield Enterprise
Kubernetes Routes
"""

from flask import render_template, abort
from flask_login import login_required

from app.kubernetes import kubernetes
from app.kubernetes.report import KubernetesReport
from app.kubernetes.health import KubernetesHealth
from app.kubernetes.cluster import KubernetesCluster
from app.kubernetes.client import KubernetesClient

# --------------------------------------------------
# Helpers
# --------------------------------------------------


def _report():

    return KubernetesReport().generate()


# --------------------------------------------------
# Dashboard
# --------------------------------------------------


@kubernetes.route("/")
@login_required
def index():

    report = _report()

    return render_template(
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
    )


# --------------------------------------------------
# Cluster
# --------------------------------------------------


@kubernetes.route("/cluster")
@login_required
def cluster():

    client = KubernetesClient()

    cluster = KubernetesCluster(client).info()

    return render_template("kubernetes/cluster.html", cluster=cluster)


# --------------------------------------------------
# Nodes
# --------------------------------------------------


@kubernetes.route("/nodes")
@login_required
def nodes():

    report = _report()

    return render_template("kubernetes/nodes.html", nodes=report["dashboard"]["nodes"])


# --------------------------------------------------
# Pods
# --------------------------------------------------


@kubernetes.route("/pods")
@login_required
def pods():

    report = _report()

    return render_template("kubernetes/pods.html", pods=report["dashboard"]["pods"])


# --------------------------------------------------
# Deployments
# --------------------------------------------------


@kubernetes.route("/deployments")
@login_required
def deployments():

    report = _report()

    return render_template(
        "kubernetes/deployments.html", deployments=report["dashboard"]["deployments"]
    )


# --------------------------------------------------
# Services
# --------------------------------------------------


@kubernetes.route("/services")
@login_required
def services():

    report = _report()

    return render_template(
        "kubernetes/services.html", services=report["dashboard"]["services"]
    )


# --------------------------------------------------
# Namespaces
# --------------------------------------------------


@kubernetes.route("/namespaces")
@login_required
def namespaces():

    report = _report()

    return render_template(
        "kubernetes/namespaces.html", namespaces=report["dashboard"]["namespaces"]
    )


# --------------------------------------------------
# Ingress
# --------------------------------------------------


@kubernetes.route("/ingress")
@login_required
def ingress():

    report = _report()

    return render_template(
        "kubernetes/ingress.html", ingress=report["dashboard"]["ingress"]
    )


# --------------------------------------------------
# Security
# --------------------------------------------------


@kubernetes.route("/security")
@login_required
def security():

    report = _report()

    return render_template(
        "kubernetes/security.html",
        security=report["security"],
        recommendations=report["recommendations"],
    )


# --------------------------------------------------
# Health
# --------------------------------------------------


@kubernetes.route("/health")
@login_required
def health():

    health = KubernetesHealth().status()

    return render_template("kubernetes/health.html", health=health)


# --------------------------------------------------
# Details
# --------------------------------------------------


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

    return render_template("kubernetes/details.html", resource=resource)
