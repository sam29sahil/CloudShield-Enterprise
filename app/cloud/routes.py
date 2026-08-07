"""
CloudShield Enterprise
Cloud Routes
"""

from flask import render_template
from flask_login import login_required

from app.cloud import cloud
from app.cloud.services import CloudService

service = CloudService()


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

    return render_template("cloud/azure/dashboard.html", data=data, findings=data["findings"],  virtual_machines=service.azure_virtual_machines()["data"],)


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

@cloud.route("/azure/network-security-groups")
@login_required
def azure_network_security_groups():

    data = service.azure_network_security_groups()

    if isinstance(data, dict):
        data = data.get("data", [])

    return render_template(
        "cloud/azure/network_security_groups.html",
        data=data,
    )


@cloud.route("/azure/load-balancers")
@login_required
def azure_load_balancers():

    data = service.load_balancers()

    return render_template("cloud/azure/load_balancers.html", data=data)

@cloud.route("/azure/public-ips")
@login_required
def azure_public_ips():

    data = service.azure_public_ips()

    return render_template(
        "cloud/azure/public_ips.html",
        data=data,
    )

@cloud.route("/azure/route-tables")
@login_required
def azure_route_tables():

    data = service.azure_route_tables()

    return render_template(
        "cloud/azure/route_tables.html",
        data=data["data"],
    )
    
@cloud.route("/azure/firewalls")
@login_required
def azure_firewalls():

    data = service.azure_firewalls()

    return render_template(
        "cloud/azure/firewall.html",
        data=data["data"],
    )  
    
@cloud.route("/azure/nat-gateways")
@login_required
def azure_nat_gateways():

    data = service.azure_nat_gateways()

    return render_template(
        "cloud/azure/nat_gateway.html",
        data=data["data"],
    )   
    
@cloud.route("/azure/application-gateways")
@login_required
def azure_application_gateways():

    result = service.azure_application_gateways()

    return render_template(
        "cloud/azure/application_gateway.html",
        data=result["data"],
    )  
    
@cloud.route("/azure/vpn-gateways")
@login_required
def azure_vpn_gateways():

    result = service.azure_vpn_gateways()

    return render_template(
        "cloud/azure/vpn_gateway.html",
        data=result["data"],
    )         