"""
CloudShield Enterprise
Cloud Routes
"""

from flask import render_template
from flask_login import login_required

from app.cloud import cloud
from app.cloud.services import CloudService

service = CloudService()

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@cloud.route("/")
@login_required
def dashboard():

    cloud_data = service.dashboard()

    return render_template("cloud/dashboard.html", cloud=cloud_data)


@cloud.route("/aws")
@login_required
def aws():

    cloud_data = service.dashboard()

    return render_template("cloud/aws/dashboard.html", cloud=cloud_data)


@cloud.route("/ec2")
@login_required
def ec2():

    data = service.ec2()

    return render_template("cloud/aws/ec2.html", data=data)


@cloud.route("/s3")
@login_required
def s3():

    data = service.s3()

    return render_template("cloud/aws/s3.html", data=data)


@cloud.route("/iam")
@login_required
def iam():

    data = service.iam()

    return render_template("cloud/aws/iam.html", data=data)


@cloud.route("/security-groups")
@login_required
def security_groups():

    data = service.security_groups()

    return render_template("cloud/aws/security_groups.html", data=data)


@cloud.route("/cloudtrail")
@login_required
def cloudtrail():

    data = service.cloudtrail()

    return render_template("cloud/aws/cloudtrail.html", data=data)


@cloud.route("/guardduty")
@login_required
def guardduty():

    data = service.guardduty()

    return render_template("cloud/aws/guardduty.html", data=data)


@cloud.route("/inspector")
@login_required
def inspector():

    data = service.inspector()

    return render_template("cloud/aws/inspector.html", data=data)


# --------------------------------------------------
# Azure Dashboard
# --------------------------------------------------

@cloud.route("/azure")
@login_required
def azure():

    data = service.azure_dashboard()

    return render_template("cloud/azure/dashboard.html", data=data)


# --------------------------------------------------
# Azure Virtual Machines
# --------------------------------------------------

@cloud.route("/azure/virtual-machines")
@login_required
def azure_virtual_machines():

    data = service.azure_virtual_machines()

    return render_template("cloud/azure/virtual_machines.html", data=data)


# --------------------------------------------------
# Azure Storage
# --------------------------------------------------

@cloud.route("/azure/storage")
@login_required
def azure_storage():

    data = service.azure_storage()

    return render_template("cloud/azure/storage.html", data=data)


# --------------------------------------------------
# Azure Resource Groups
# --------------------------------------------------

@cloud.route("/azure/resource-groups")
@login_required
def azure_resource_groups():

    data = service.azure_resource_groups()

    return render_template("cloud/azure/resource_groups.html", data=data)


# --------------------------------------------------
# Azure Key Vault
# --------------------------------------------------

@cloud.route("/azure/keyvault")
@login_required
def azure_keyvault():

    data = service.azure_keyvault()

    return render_template("cloud/azure/keyvault.html", data=data)


# --------------------------------------------------
# Azure Monitor
# --------------------------------------------------

@cloud.route("/azure/monitor")
@login_required
def azure_monitor():

    data = service.azure_monitor()

    return render_template("cloud/azure/monitor.html", data=data)


# --------------------------------------------------
# Azure Defender
# --------------------------------------------------

@cloud.route("/azure/defender")
@login_required
def azure_defender():

    data = service.azure_defender()

    return render_template("cloud/azure/defender.html", data=data)


# --------------------------------------------------
# Azure Identity
# --------------------------------------------------

@cloud.route("/azure/identity")
@login_required
def azure_identity():

    data = service.azure_identity()

    return render_template("cloud/azure/identity.html", data=data)


@cloud.route("/azure/network-interfaces")
@login_required
def azure_network_interfaces():

    data = service.network_interfaces()

    return render_template("cloud/azure/network_interfaces.html", data=data)


@cloud.route("/azure/load-balancers")
@login_required
def azure_load_balancers():

    data = service.load_balancers()

    return render_template("cloud/azure/load_balancers.html", data=data)
