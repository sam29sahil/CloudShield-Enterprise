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

<<<<<<< HEAD
    return render_template("cloud/dashboard.html", cloud=cloud_data)


=======
    return render_template(

        "cloud/dashboard.html",

        cloud=cloud_data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@cloud.route("/aws")
@login_required
def aws():

    cloud_data = service.dashboard()

<<<<<<< HEAD
    return render_template("cloud/aws/dashboard.html", cloud=cloud_data)

=======
    return render_template(

        "cloud/aws/dashboard.html",

        cloud=cloud_data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@cloud.route("/ec2")
@login_required
def ec2():

    data = service.ec2()

<<<<<<< HEAD
    return render_template("cloud/aws/ec2.html", data=data)
=======
    return render_template(

        "cloud/aws/ec2.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@cloud.route("/s3")
@login_required
def s3():

    data = service.s3()

<<<<<<< HEAD
    return render_template("cloud/aws/s3.html", data=data)
=======
    return render_template(

        "cloud/aws/s3.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@cloud.route("/iam")
@login_required
def iam():

    data = service.iam()

<<<<<<< HEAD
    return render_template("cloud/aws/iam.html", data=data)
=======
    return render_template(

        "cloud/aws/iam.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@cloud.route("/security-groups")
@login_required
def security_groups():

    data = service.security_groups()

<<<<<<< HEAD
    return render_template("cloud/aws/security_groups.html", data=data)
=======
    return render_template(

        "cloud/aws/security_groups.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@cloud.route("/cloudtrail")
@login_required
def cloudtrail():

    data = service.cloudtrail()

<<<<<<< HEAD
    return render_template("cloud/aws/cloudtrail.html", data=data)
=======
    return render_template(

        "cloud/aws/cloudtrail.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@cloud.route("/guardduty")
@login_required
def guardduty():

    data = service.guardduty()

<<<<<<< HEAD
    return render_template("cloud/aws/guardduty.html", data=data)
=======
    return render_template(

        "cloud/aws/guardduty.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@cloud.route("/inspector")
@login_required
def inspector():

    data = service.inspector()

<<<<<<< HEAD
    return render_template("cloud/aws/inspector.html", data=data)

=======
    return render_template(

        "cloud/aws/inspector.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# Azure Dashboard
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@cloud.route("/azure")
@login_required
def azure():

    data = service.azure_dashboard()

<<<<<<< HEAD
    return render_template("cloud/azure/dashboard.html", data=data)

=======
    return render_template(

        "cloud/azure/dashboard.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# Azure Virtual Machines
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@cloud.route("/azure/virtual-machines")
@login_required
def azure_virtual_machines():

    data = service.azure_virtual_machines()

<<<<<<< HEAD
    return render_template("cloud/azure/virtual_machines.html", data=data)

=======
    return render_template(

        "cloud/azure/virtual_machines.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# Azure Storage
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@cloud.route("/azure/storage")
@login_required
def azure_storage():

    data = service.azure_storage()

<<<<<<< HEAD
    return render_template("cloud/azure/storage.html", data=data)

=======
    return render_template(

        "cloud/azure/storage.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# Azure Resource Groups
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@cloud.route("/azure/resource-groups")
@login_required
def azure_resource_groups():

    data = service.azure_resource_groups()

<<<<<<< HEAD
    return render_template("cloud/azure/resource_groups.html", data=data)

=======
    return render_template(

        "cloud/azure/resource_groups.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# Azure Key Vault
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@cloud.route("/azure/keyvault")
@login_required
def azure_keyvault():

    data = service.azure_keyvault()

<<<<<<< HEAD
    return render_template("cloud/azure/keyvault.html", data=data)

=======
    return render_template(

        "cloud/azure/keyvault.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# Azure Monitor
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@cloud.route("/azure/monitor")
@login_required
def azure_monitor():

    data = service.azure_monitor()

<<<<<<< HEAD
    return render_template("cloud/azure/monitor.html", data=data)

=======
    return render_template(

        "cloud/azure/monitor.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# Azure Defender
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@cloud.route("/azure/defender")
@login_required
def azure_defender():

    data = service.azure_defender()

<<<<<<< HEAD
    return render_template("cloud/azure/defender.html", data=data)

=======
    return render_template(

        "cloud/azure/defender.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# --------------------------------------------------
# Azure Identity
# --------------------------------------------------

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@cloud.route("/azure/identity")
@login_required
def azure_identity():

    data = service.azure_identity()

<<<<<<< HEAD
    return render_template("cloud/azure/identity.html", data=data)


=======
    return render_template(

        "cloud/azure/identity.html",

        data=data

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@cloud.route("/azure/network-interfaces")
@login_required
def azure_network_interfaces():

    data = service.network_interfaces()

<<<<<<< HEAD
    return render_template("cloud/azure/network_interfaces.html", data=data)


=======
    return render_template(

        "cloud/azure/network_interfaces.html",

        data=data

    )
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@cloud.route("/azure/load-balancers")
@login_required
def azure_load_balancers():

    data = service.load_balancers()

<<<<<<< HEAD
    return render_template("cloud/azure/load_balancers.html", data=data)
=======
    return render_template(

        "cloud/azure/load_balancers.html",

        data=data

    )    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
