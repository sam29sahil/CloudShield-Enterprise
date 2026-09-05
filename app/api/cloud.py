"""
CloudShield Enterprise
Cloud API
"""

from flask_login import login_required

from app.api import api
from app.api.responses import success_response, error_response

from app.cloud.aws.services import AWSScanner
from app.cloud.aws.scanner import AWSReadOnlyScanner
from app.cloud.azure.services import AzureService

aws = AWSScanner()


def aws_result():
    return AWSReadOnlyScanner().scan()

class LazyAzureService:

    def __init__(self):
        self._service = None

    def _get_service(self):
        if self._service is None:
            self._service = AzureService()
        return self._service

    def __getattr__(self, name):
        return getattr(self._get_service(), name)


azure = LazyAzureService()


# =====================================================
# Cloud Dashboard
# =====================================================


@api.route("/cloud", methods=["GET"])
@login_required
def cloud_dashboard():
    """
    Cloud dashboard summary.
    """

    return success_response(
        data={"aws": aws_result(), "azure": azure.summary()},
        message="Cloud summary retrieved successfully",
    )


# =====================================================
# AWS
# =====================================================


@api.route("/cloud/aws", methods=["GET"])
@login_required
def aws_dashboard():

    return success_response(data=aws_result(), message="AWS security scan completed")


@api.route("/aws/status", methods=["GET"])
@login_required
def aws_status():
    return success_response(data=AWSReadOnlyScanner().connection_status(), message="AWS connection status retrieved")


@api.route("/aws/scan", methods=["GET"])
@login_required
def aws_full_scan():
    return success_response(data=aws_result(), message="AWS scan completed")


@api.route("/cloud/aws/iam", methods=["GET"])
@login_required
def iam_scan():

    return success_response(data=aws_result().get("services", {}).get("iam", {}), message="IAM scan completed")


@api.route("/cloud/aws/s3", methods=["GET"])
@login_required
def s3_scan():

    return success_response(data=aws_result().get("services", {}).get("s3", {}), message="S3 scan completed")


@api.route("/cloud/aws/ec2", methods=["GET"])
@login_required
def ec2_scan():

    return success_response(data=aws_result().get("services", {}).get("ec2", {}), message="EC2 scan completed")


@api.route("/cloud/aws/security-groups", methods=["GET"])
@login_required
def security_groups_scan():

    return success_response(
        data=aws_result().get("services", {}).get("security_groups", {}), message="Security Groups scan completed"
    )


@api.route("/aws/ebs", methods=["GET"])
@login_required
def ebs_scan():
    return success_response(data=aws_result().get("services", {}).get("ebs", {}), message="EBS scan completed")


@api.route("/aws/elastic-ips", methods=["GET"])
@login_required
def elastic_ips_scan():
    return success_response(data=aws_result().get("services", {}).get("elastic_ips", {}), message="Elastic IP scan completed")


@api.route("/cloud/aws/guardduty", methods=["GET"])
@login_required
def guardduty_scan():

    return success_response(
        data=aws.guardduty.scan(), message="GuardDuty scan completed"
    )


@api.route("/cloud/aws/inspector", methods=["GET"])
@login_required
def inspector_scan():

    return success_response(
        data=aws.inspector.scan(), message="Inspector scan completed"
    )


@api.route("/cloud/aws/cloudtrail", methods=["GET"])
@login_required
def cloudtrail_scan():

    return success_response(
        data=aws.cloudtrail.scan(), message="CloudTrail scan completed"
    )


@api.route("/cloud/aws/config", methods=["GET"])
@login_required
def config_scan():

    return success_response(data=aws.config.scan(), message="AWS Config scan completed")


# =====================================================
# Azure
# =====================================================


@api.route("/cloud/azure", methods=["GET"])
@login_required
def azure_dashboard():

    if not azure.connected():

        return error_response(
            azure.configuration_error()
            or "Azure is not connected.",
            400,
        )

    return success_response(
        data=azure.summary(), message="Azure dashboard retrieved successfully"
    )


@api.route("/cloud/azure/virtual-machines", methods=["GET"])
@login_required
def azure_virtual_machines():

    return success_response(
        data=azure.virtual_machines.list(), message="Azure virtual machines retrieved"
    )


@api.route("/cloud/azure/storage", methods=["GET"])
@login_required
def azure_storage():

    return success_response(
        data=azure.storage.list(), message="Azure storage accounts retrieved"
    )


@api.route("/cloud/azure/resource-groups", methods=["GET"])
@login_required
def azure_resource_groups():

    return success_response(
        data=azure.resource_groups.list(), message="Azure resource groups retrieved"
    )


@api.route("/cloud/azure/keyvault", methods=["GET"])
@login_required
def azure_keyvault():

    return success_response(
        data=azure.keyvault.list(), message="Azure Key Vault retrieved"
    )


@api.route("/cloud/azure/network", methods=["GET"])
@login_required
def azure_network():

    return success_response(
        data={
            "virtual_networks": azure.virtual_networks(),
            "network_security_groups": azure.network_security_groups(),
            "public_ips": azure.public_ips(),
            "network_interfaces": azure.network_interfaces(),
            "load_balancers": azure.load_balancers(),
        },
        message="Azure network resources retrieved",
    )
