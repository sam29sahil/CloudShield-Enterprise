"""
CloudShield Enterprise
Cloud API
"""

from flask_login import login_required

from app.api import api
from app.api.responses import success_response, error_response

from app.cloud.aws.services import AWSScanner
from app.cloud.azure.services import AzureService

<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
aws = AWSScanner()
azure = AzureService()


# =====================================================
# Cloud Dashboard
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@api.route("/cloud", methods=["GET"])
@login_required
def cloud_dashboard():
    """
    Cloud dashboard summary.
    """

    return success_response(
<<<<<<< HEAD
        data={"aws": aws.scan(), "azure": azure.summary()},
        message="Cloud summary retrieved successfully",
=======

        data={

            "aws": aws.scan(),

            "azure": azure.summary()

        },

        message="Cloud summary retrieved successfully"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# =====================================================
# AWS
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@api.route("/cloud/aws", methods=["GET"])
@login_required
def aws_dashboard():

<<<<<<< HEAD
    return success_response(data=aws.scan(), message="AWS security scan completed")
=======
    return success_response(

        data=aws.scan(),

        message="AWS security scan completed"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@api.route("/cloud/aws/iam", methods=["GET"])
@login_required
def iam_scan():

<<<<<<< HEAD
    return success_response(data=aws.iam.scan(), message="IAM scan completed")
=======
    return success_response(

        data=aws.iam.scan(),

        message="IAM scan completed"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@api.route("/cloud/aws/s3", methods=["GET"])
@login_required
def s3_scan():

<<<<<<< HEAD
    return success_response(data=aws.s3.scan(), message="S3 scan completed")
=======
    return success_response(

        data=aws.s3.scan(),

        message="S3 scan completed"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@api.route("/cloud/aws/ec2", methods=["GET"])
@login_required
def ec2_scan():

<<<<<<< HEAD
    return success_response(data=aws.ec2.scan(), message="EC2 scan completed")
=======
    return success_response(

        data=aws.ec2.scan(),

        message="EC2 scan completed"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@api.route("/cloud/aws/security-groups", methods=["GET"])
@login_required
def security_groups_scan():

    return success_response(
<<<<<<< HEAD
        data=aws.security_groups.scan(), message="Security Groups scan completed"
=======

        data=aws.security_groups.scan(),

        message="Security Groups scan completed"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/cloud/aws/guardduty", methods=["GET"])
@login_required
def guardduty_scan():

    return success_response(
<<<<<<< HEAD
        data=aws.guardduty.scan(), message="GuardDuty scan completed"
=======

        data=aws.guardduty.scan(),

        message="GuardDuty scan completed"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/cloud/aws/inspector", methods=["GET"])
@login_required
def inspector_scan():

    return success_response(
<<<<<<< HEAD
        data=aws.inspector.scan(), message="Inspector scan completed"
=======

        data=aws.inspector.scan(),

        message="Inspector scan completed"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/cloud/aws/cloudtrail", methods=["GET"])
@login_required
def cloudtrail_scan():

    return success_response(
<<<<<<< HEAD
        data=aws.cloudtrail.scan(), message="CloudTrail scan completed"
=======

        data=aws.cloudtrail.scan(),

        message="CloudTrail scan completed"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/cloud/aws/config", methods=["GET"])
@login_required
def config_scan():

<<<<<<< HEAD
    return success_response(data=aws.config.scan(), message="AWS Config scan completed")
=======
    return success_response(

        data=aws.config.scan(),

        message="AWS Config scan completed"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# Azure
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@api.route("/cloud/azure", methods=["GET"])
@login_required
def azure_dashboard():

    if not azure.connected():

<<<<<<< HEAD
        return error_response("Azure is not connected.", 400)

    return success_response(
        data=azure.summary(), message="Azure dashboard retrieved successfully"
=======
        return error_response(

            "Azure is not connected.",

            400

        )

    return success_response(

        data=azure.summary(),

        message="Azure dashboard retrieved successfully"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/cloud/azure/virtual-machines", methods=["GET"])
@login_required
def azure_virtual_machines():

    return success_response(
<<<<<<< HEAD
        data=azure.virtual_machines.list(), message="Azure virtual machines retrieved"
=======

        data=azure.virtual_machines.list(),

        message="Azure virtual machines retrieved"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/cloud/azure/storage", methods=["GET"])
@login_required
def azure_storage():

    return success_response(
<<<<<<< HEAD
        data=azure.storage.list(), message="Azure storage accounts retrieved"
=======

        data=azure.storage.list(),

        message="Azure storage accounts retrieved"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/cloud/azure/resource-groups", methods=["GET"])
@login_required
def azure_resource_groups():

    return success_response(
<<<<<<< HEAD
        data=azure.resource_groups.list(), message="Azure resource groups retrieved"
=======

        data=azure.resource_groups.list(),

        message="Azure resource groups retrieved"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/cloud/azure/keyvault", methods=["GET"])
@login_required
def azure_keyvault():

    return success_response(
<<<<<<< HEAD
        data=azure.keyvault.list(), message="Azure Key Vault retrieved"
=======

        data=azure.keyvault.list(),

        message="Azure Key Vault retrieved"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/cloud/azure/network", methods=["GET"])
@login_required
def azure_network():

    return success_response(
<<<<<<< HEAD
        data={
            "virtual_networks": azure.virtual_networks(),
            "network_security_groups": azure.network_security_groups(),
            "public_ips": azure.public_ips(),
            "network_interfaces": azure.network_interfaces(),
            "load_balancers": azure.load_balancers(),
        },
        message="Azure network resources retrieved",
    )
=======

        data={

            "virtual_networks": azure.virtual_networks(),

            "network_security_groups": azure.network_security_groups(),

            "public_ips": azure.public_ips(),

            "network_interfaces": azure.network_interfaces(),

            "load_balancers": azure.load_balancers()

        },

        message="Azure network resources retrieved"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
