"""
CloudShield Enterprise
Cloud Routes
"""

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app.cloud import cloud
from app.cloud.services import CloudService
from app.models.project import Project

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

    project = Project.query.order_by(Project.id.asc()).first()

    return render_template(
        "cloud/azure/dashboard.html",
        data=data,
        findings=data.get("findings", []),
        virtual_machines=service.azure_virtual_machines()["data"],
        default_project_id=project.id if project else None,
        scan_result=None,
    )


@cloud.route("/azure/security-scan", methods=["POST"])
@login_required
def azure_security_scan():

    project_id = request.form.get("project_id", type=int)

    try:
        result = service.azure_security_scan(
            user_id=current_user.id,
            project_id=project_id,
        )

        if result.get("persistence", {}).get("scan_id"):
            flash(
                "Azure security scan completed and findings were linked successfully.",
                "success",
            )
        else:
            flash(
                result.get("persistence", {}).get("message", "Azure scan completed."),
                "warning",
            )

        data = service.azure_dashboard()

        project = Project.query.order_by(Project.id.asc()).first()

        return render_template(
            "cloud/azure/dashboard.html",
            data=data,
            findings=result.get("findings", []),
            virtual_machines=service.azure_virtual_machines()["data"],
            default_project_id=project.id if project else None,
            scan_result=result,
        )

    except Exception as error:

        flash(f"Azure security scan failed: {error}", "danger")
        return redirect(url_for("cloud.azure"))


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

    result = service.azure_identity()

    return render_template(
        "cloud/azure/identity.html",
        data=result["data"],
    )


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
    
# --------------------------------------------------
# Azure Managed Identity
# --------------------------------------------------

@cloud.route("/azure/managed-identity")
@login_required
def azure_managed_identity():

    result = service.azure_managed_identity()

    return render_template(
        "cloud/azure/managed_identity.html",
        data=result["data"],
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
    
@cloud.route("/azure/expressroute")
@login_required
def azure_express_routes():

    result = service.azure_express_routes()

    return render_template(
        "cloud/azure/expressroute.html",
        data=result["data"],
    )  
    
@cloud.route("/azure/private-endpoints")
@login_required
def azure_private_endpoints():

    result = service.azure_private_endpoints()

    return render_template(
        "cloud/azure/private_endpoints.html",
        data=result["data"],
    ) 
    
@cloud.route("/azure/bastion")
@login_required
def azure_bastion_hosts():

    result = service.azure_bastion_hosts()

    return render_template(
        "cloud/azure/bastion.html",
        data=result["data"],
    ) 
    
@cloud.route("/azure/vm-scale-sets")
@login_required
def azure_vm_scale_sets():

    result = service.azure_vm_scale_sets()

    return render_template(
        "cloud/azure/vm_scale_sets.html",
        data=result["data"],
    )
    
@cloud.route("/azure/managed-disks")
@login_required
def azure_managed_disks():

    result = service.azure_managed_disks()

    return render_template(
        "cloud/azure/managed_disks.html",
        data=result["data"],
    )
    
@cloud.route("/azure/snapshots")
@login_required
def azure_snapshots():

    result = service.azure_snapshots()

    return render_template(
        "cloud/azure/snapshots.html",
        data=result["data"],
    ) 
    
@cloud.route("/azure/images")
@login_required
def azure_images():

    result = service.azure_images()

    return render_template(
        "cloud/azure/images.html",
        data=result["data"],
    ) 
    
@cloud.route("/azure/availability-sets")
@login_required
def azure_availability_sets():

    result = service.azure_availability_sets()

    return render_template(
        "cloud/azure/availability_sets.html",
        data=result["data"],
    ) 
    
@cloud.route("/azure/blob-containers")
@login_required
def azure_blob_containers():

    result = service.azure_blob_containers()

    return render_template(
        "cloud/azure/blob_containers.html",
        data=result["data"],
    )    
    
@cloud.route("/azure/file-shares")
@login_required
def azure_file_shares():

    result = service.azure_file_shares()

    return render_template(
        "cloud/azure/file_shares.html",
        data=result["data"],
    )                                
    
@cloud.route("/azure/queues")
@login_required
def azure_queues():

    result = service.azure_queues()

    return render_template(
        "cloud/azure/queues.html",
        data=result["data"],
    )  
    
@cloud.route("/azure/tables")
@login_required
def azure_tables():

    result = service.azure_tables()

    return render_template(
        "cloud/azure/tables.html",
        data=result["data"],
    )   
    
@cloud.route("/azure/policies")
@login_required
def azure_policies():

    result = service.azure_policies()

    return render_template(
        "cloud/azure/policies.html",
        data=result["data"],
    )
    
@cloud.route("/azure/rbac")
@login_required
def azure_rbac():

    result = service.azure_rbac()

    return render_template(
        "cloud/azure/rbac.html",
        data=result["data"],
    )
    
@cloud.route("/azure/advisor")
@login_required
def azure_advisor():

    result = service.azure_advisor()

    return render_template(
        "cloud/azure/advisor.html",
        data=result["data"],
    )
    
@cloud.route("/azure/log-analytics")
@login_required
def azure_log_analytics():

    result = service.azure_log_analytics()

    return render_template(
        "cloud/azure/log_analytics.html",
        data=result["data"],
    ) 
    
@cloud.route("/azure/sql")
@login_required
def azure_sql():

    result = service.azure_sql_databases()

    return render_template(
        "cloud/azure/sql_database.html",
        data=result["data"],
    ) 
    
@cloud.route("/azure/cosmos-db")
@login_required
def azure_cosmos_db():

    result = service.azure_cosmos_db()

    return render_template(
        "cloud/azure/cosmos_db.html",
        data=result["data"],
    )  
    
@cloud.route("/azure/postgresql")
@login_required
def azure_postgresql():

    result = service.azure_postgresql()

    return render_template(
        "cloud/azure/postgresql.html",
        data=result["data"],
    ) 
    
                              