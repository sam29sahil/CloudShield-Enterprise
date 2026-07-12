"""
CloudShield Enterprise
Scans API
"""

from flask import request
from flask_login import login_required, current_user

from app.api import api
from app.api.responses import success_response, error_response
from app.services.legacy_scan_service import ScanService

scan_service = ScanService()


@api.route("/scans", methods=["GET"])
@login_required
def get_scans():
    """
    Return all scans.
    """

    scans = scan_service.all()

    data = []

    for scan in scans:

        data.append({

            "id": scan.id,

            "asset_id": scan.asset_id,

            "user_id": scan.user_id,

            "score": scan.score,

            "risk": scan.risk,

            "scan_type": scan.scan_type,

            "started_at": (
                scan.started_at.isoformat()
                if scan.started_at
                else None
            ),

            "completed_at": (
                scan.completed_at.isoformat()
                if scan.completed_at
                else None
            )

        })

    return success_response(

        data=data,

        message="Scans retrieved successfully"

    )


@api.route("/scans/<int:scan_id>", methods=["GET"])
@login_required
def get_scan(scan_id):
    """
    Get a single scan.
    """

    scan = scan_service.get(scan_id)

    if not scan:

        return error_response(

            "Scan not found",

            404

        )

    return success_response(

        data={

            "id": scan.id,

            "asset_id": scan.asset_id,

            "user_id": scan.user_id,

            "score": scan.score,

            "risk": scan.risk,

            "scan_type": scan.scan_type,

            "started_at": (
                scan.started_at.isoformat()
                if scan.started_at
                else None
            ),

            "completed_at": (
                scan.completed_at.isoformat()
                if scan.completed_at
                else None
            )

        }

    )


@api.route("/scans", methods=["POST"])
@login_required
def create_scan():
    """
    Create a scan record.
    """

    data = request.get_json()

    if not data:

        return error_response(

            "JSON data required",

            400

        )

    required = [

        "asset_id",

        "score",

        "risk",

        "scan_type"

    ]

    for field in required:

        if field not in data:

            return error_response(

                f"{field} is required",

                400

            )

    scan = scan_service.create(

        asset_id=data["asset_id"],

        user_id=current_user.id,

        score=data["score"],

        risk=data["risk"],

        scan_type=data["scan_type"]

    )

    return success_response(

        data={

            "id": scan.id

        },

        message="Scan created successfully",

        status_code=201

    )


@api.route("/scans/<int:scan_id>", methods=["DELETE"])
@login_required
def delete_scan(scan_id):
    """
    Delete a scan.
    """

    deleted = scan_service.delete(scan_id)

    if not deleted:

        return error_response(

            "Scan not found",

            404

        )

    return success_response(

        message="Scan deleted successfully"

    )