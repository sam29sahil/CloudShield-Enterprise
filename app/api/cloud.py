"""
CloudShield Enterprise
Cloud API
"""

from flask_login import login_required

from app.api import api
from app.api.responses import success_response
from app.cloud.aws.services import AWSScanner


@api.route("/cloud", methods=["GET"])
@login_required
def cloud_scan():

    aws = AWSScanner()
    """
    Run complete AWS security scan.
    """

    return success_response(

        data=aws.scan(),

        message="AWS security scan completed"

    )


@api.route("/cloud/iam", methods=["GET"])
@login_required
def iam_scan():

    return success_response(

        data=aws.iam.scan(),

        message="IAM scan completed"

    )


@api.route("/cloud/s3", methods=["GET"])
@login_required
def s3_scan():

    return success_response(

        data=aws.s3.scan(),

        message="S3 scan completed"

    )


@api.route("/cloud/ec2", methods=["GET"])
@login_required
def ec2_scan():

    return success_response(

        data=aws.ec2.scan(),

        message="EC2 scan completed"

    )


@api.route("/cloud/security-groups", methods=["GET"])
@login_required
def security_groups_scan():

    return success_response(

        data=aws.security_groups.scan(),

        message="Security Groups scan completed"

    )


@api.route("/cloud/guardduty", methods=["GET"])
@login_required
def guardduty_scan():

    return success_response(

        data=aws.guardduty.scan(),

        message="GuardDuty scan completed"

    )


@api.route("/cloud/inspector", methods=["GET"])
@login_required
def inspector_scan():

    return success_response(

        data=aws.inspector.scan(),

        message="Inspector scan completed"

    )


@api.route("/cloud/cloudtrail", methods=["GET"])
@login_required
def cloudtrail_scan():

    return success_response(

        data=aws.cloudtrail.scan(),

        message="CloudTrail scan completed"

    )


@api.route("/cloud/config", methods=["GET"])
@login_required
def config_scan():

    return success_response(

        data=aws.config.scan(),

        message="AWS Config scan completed"

    )