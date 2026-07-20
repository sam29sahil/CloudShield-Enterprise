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

    return render_template(

        "cloud/dashboard.html",

        cloud=cloud_data

    )
@cloud.route("/aws")
@login_required
def aws():

    cloud_data = service.dashboard()

    return render_template(

        "cloud/aws.html",

        cloud=cloud_data

    )

@cloud.route("/ec2")
@login_required
def ec2():

    data = service.ec2()

    return render_template(

        "cloud/ec2.html",

        data=data

    )


@cloud.route("/s3")
@login_required
def s3():

    data = service.s3()

    return render_template(

        "cloud/s3.html",

        data=data

    )


@cloud.route("/iam")
@login_required
def iam():

    data = service.iam()

    return render_template(

        "cloud/iam.html",

        data=data

    )


@cloud.route("/security-groups")
@login_required
def security_groups():

    data = service.security_groups()

    return render_template(

        "cloud/security_groups.html",

        data=data

    )


@cloud.route("/cloudtrail")
@login_required
def cloudtrail():

    data = service.cloudtrail()

    return render_template(

        "cloud/cloudtrail.html",

        data=data

    )


@cloud.route("/guardduty")
@login_required
def guardduty():

    data = service.guardduty()

    return render_template(

        "cloud/guardduty.html",

        data=data

    )


@cloud.route("/inspector")
@login_required
def inspector():

    data = service.inspector()

    return render_template(

        "cloud/inspector.html",

        data=data

    )
