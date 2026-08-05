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

<<<<<<< HEAD
    page = request.args.get("page", 1, type=int)

    per_page = request.args.get("per_page", 20, type=int)
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    report_type = request.args.get("report_type")

    query = report_service.query()

    if report_type:

<<<<<<< HEAD
        query = query.filter_by(report_type=report_type)

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
=======
        query = query.filter_by(
            report_type=report_type
        )

    pagination = query.paginate(

        page=page,

        per_page=per_page,

        error_out=False

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    reports = pagination.items

    data = []

    for report in reports:

<<<<<<< HEAD
        data.append(
            {
                "id": report.id,
                "scan_id": report.scan_id,
                "report_type": report.report_type,
                "file_name": report.file_name,
                "created_at": (
                    report.created_at.isoformat() if report.created_at else None
                ),
            }
        )

    return success_response(
        data={
            "items": data,
            "page": pagination.page,
            "pages": pagination.pages,
            "per_page": pagination.per_page,
            "total": pagination.total,
        },
        message="Reports retrieved successfully",
=======
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

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/reports/<int:report_id>", methods=["GET"])
@login_required
def get_report(report_id):
    """
    Get report by ID.
    """

    report = report_service.get(report_id)

    if not report:

<<<<<<< HEAD
        return error_response("Report not found", 404)

    return success_response(
        data={
            "id": report.id,
            "scan_id": report.scan_id,
            "report_type": report.report_type,
            "file_name": report.file_name,
            "created_at": (
                report.created_at.isoformat() if report.created_at else None
            ),
        }
=======
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

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/reports", methods=["POST"])
@login_required
def create_report():
    """
    Create report.
    """

    data = request.get_json()

    if not data:

<<<<<<< HEAD
        return error_response("JSON data required", 400)

    required = ["scan_id", "report_type", "file_name"]
=======
        return error_response(

            "JSON data required",

            400

        )

    required = [

        "scan_id",

        "report_type",

        "file_name"

    ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    for field in required:

        if field not in data:

<<<<<<< HEAD
            return error_response(f"{field} is required", 400)

    report = report_service.create(
        scan_id=data["scan_id"],
        report_type=data["report_type"],
        file_name=data["file_name"],
    )

    return success_response(
        data={"id": report.id}, message="Report created successfully", status_code=201
=======
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

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


@api.route("/reports/<int:report_id>", methods=["DELETE"])
@login_required
def delete_report(report_id):
    """
    Delete report.
    """

    deleted = report_service.delete(report_id)

    if not deleted:

<<<<<<< HEAD
        return error_response("Report not found", 404)

    return success_response(message="Report deleted successfully")

=======
        return error_response(

            "Report not found",

            404

        )

    return success_response(

        message="Report deleted successfully"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@api.route("/reports/<int:report_id>/pdf", methods=["GET"])
@login_required
def download_pdf(report_id):

    report = report_service.get(report_id)

    if not report:

<<<<<<< HEAD
        return error_response("Report not found", 404)

    return success_response(
        data={"file": report.file_name, "type": "PDF"}, message="PDF report ready"
    )


=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@api.route("/reports/<int:report_id>/csv", methods=["GET"])
@login_required
def download_csv(report_id):

    report = report_service.get(report_id)

    if not report:

<<<<<<< HEAD
        return error_response("Report not found", 404)

    return success_response(
        data={"file": report.file_name, "type": "CSV"}, message="CSV report ready"
    )


=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@api.route("/reports/<int:report_id>/json", methods=["GET"])
@login_required
def download_json(report_id):

    report = report_service.get(report_id)

    if not report:

<<<<<<< HEAD
        return error_response("Report not found", 404)

    return success_response(
        data={"file": report.file_name, "type": "JSON"}, message="JSON report ready"
    )


=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@api.route("/reports/statistics", methods=["GET"])
@login_required
def report_statistics():

    return success_response(
<<<<<<< HEAD
        data=report_service.statistics(), message="Report statistics"
    )
=======

        data=report_service.statistics(),

        message="Report statistics"

    )    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
