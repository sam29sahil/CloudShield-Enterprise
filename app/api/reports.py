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
    Get reports with pagination.
    """

    page = request.args.get(
        "page",
        1,
        type=int
    )

    per_page = request.args.get(
        "per_page",
        20,
        type=int
    )

    report_type = request.args.get("report_type")

    query = report_service.query()

    if report_type:

        query = query.filter_by(
            report_type=report_type
        )

    pagination = query.paginate(

        page=page,

        per_page=per_page,

        error_out=False

    )

    reports = pagination.items

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

        data={

            "items": data,

            "page": pagination.page,

            "pages": pagination.pages,

            "per_page": pagination.per_page,

            "total": pagination.total

        },

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

@api.route("/reports/<int:report_id>/pdf", methods=["GET"])
@login_required
def download_pdf(report_id):

    report = report_service.get(report_id)

    if not report:

        return error_response(
            "Report not found",
            404
        )

    return success_response(

        data={

            "file": report.file_name,

            "type": "PDF"

        },

        message="PDF report ready"

    )
@api.route("/reports/<int:report_id>/csv", methods=["GET"])
@login_required
def download_csv(report_id):

    report = report_service.get(report_id)

    if not report:

        return error_response(
            "Report not found",
            404
        )

    return success_response(

        data={

            "file": report.file_name,

            "type": "CSV"

        },

        message="CSV report ready"

    )    
@api.route("/reports/<int:report_id>/json", methods=["GET"])
@login_required
def download_json(report_id):

    report = report_service.get(report_id)

    if not report:

        return error_response(
            "Report not found",
            404
        )

    return success_response(

        data={

            "file": report.file_name,

            "type": "JSON"

        },

        message="JSON report ready"

    )
@api.route("/reports/statistics", methods=["GET"])
@login_required
def report_statistics():

    return success_response(

        data=report_service.statistics(),

        message="Report statistics"

    )    