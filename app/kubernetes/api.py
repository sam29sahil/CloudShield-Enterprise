"""
CloudShield Enterprise
Kubernetes API
"""

from flask import jsonify
from flask_login import login_required

from app.kubernetes import kubernetes
from app.kubernetes.report import KubernetesReport


@kubernetes.route("/api/dashboard")
@login_required
def api_dashboard():

    report = KubernetesReport().generate()

    return jsonify(report)


@kubernetes.route("/api/security")
@login_required
def api_security():

    report = KubernetesReport().generate()

    return jsonify(report["security"])


@kubernetes.route("/api/health")
@login_required
def api_health():

    from app.kubernetes.health import KubernetesHealth

<<<<<<< HEAD
    return jsonify(KubernetesHealth().status())
=======
    return jsonify(

        KubernetesHealth().status()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
