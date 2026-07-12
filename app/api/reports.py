"""
CloudShield Enterprise
Reports API
"""

from flask import request
from flask_login import login_required

from app.api import api
from app.api.responses import success_response, error_response
from app.services.report_service import ReportService

report_service = ReportService()


@api.route("/reports", methods=["GET"])
@login_required
def get_reports():
    """
    Get all reports.
    """

    reports = report_service.all()

    data = []

    for report in reports:

        data.append({

            "id": report.id,

            "scan_id": report.scan_id,

            "report_type": report.report_type,

            "file_name": report.file_name,

            "created_at": (
                report.created_at.isoformat()
                if report.created_at
                else None
            )

        })

    return success_response(

        data=data,

        message="Reports retrieved successfully"

    )


@api.route("/reports/<int:report_id>", methods=["GET"])
@login_required
def get_report(report_id):
    """
    Get report by ID.
    """

    report = report_service.get(report_id)

    if not report:

        return error_response(

            "Report not found",

            404

        )

    return success_response(

        data={

            "id": report.id,

            "scan_id": report.scan_id,

            "report_type": report.report_type,

            "file_name": report.file_name,

            "created_at": (
                report.created_at.isoformat()
                if report.created_at
                else None
            )

        }

    )


@api.route("/reports", methods=["POST"])
@login_required
def create_report():
    """
    Create report.
    """

    data = request.get_json()

    if not data:

        return error_response(

            "JSON data required",

            400

        )

    required = [

        "scan_id",

        "report_type",

        "file_name"

    ]

    for field in required:

        if field not in data:

            return error_response(

                f"{field} is required",

                400

            )

    report = report_service.create(

        scan_id=data["scan_id"],

        report_type=data["report_type"],

        file_name=data["file_name"]

    )

    return success_response(

        data={

            "id": report.id

        },

        message="Report created successfully",

        status_code=201

    )


@api.route("/reports/<int:report_id>", methods=["DELETE"])
@login_required
def delete_report(report_id):
    """
    Delete report.
    """

    deleted = report_service.delete(report_id)

    if not deleted:

        return error_response(

            "Report not found",

            404

        )

    return success_response(

        message="Report deleted successfully"

    )