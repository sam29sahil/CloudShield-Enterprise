"""
CloudShield Enterprise
Findings API
"""

from flask import request
from flask_login import login_required

from app.api import api
from app.api.responses import success_response, error_response
from app.services.finding_service import FindingService

finding_service = FindingService()


@api.route("/findings", methods=["GET"])
@login_required
def get_findings():
    """
    Get all findings.
    """

    findings = finding_service.all()

    data = []

    for finding in findings:

        data.append(
            {
                "id": finding.id,
                "scan_id": finding.scan_id,
                "title": finding.title,
                "severity": finding.severity,
                "category": finding.category,
                "source": finding.source,
                "description": finding.description,
                "recommendation": finding.recommendation,
            }
        )

    return success_response(data=data, message="Findings retrieved successfully")


@api.route("/findings/<int:finding_id>", methods=["GET"])
@login_required
def get_finding(finding_id):
    """
    Get finding by ID.
    """

    finding = finding_service.get(finding_id)

    if not finding:

        return error_response("Finding not found", 404)

    return success_response(
        data={
            "id": finding.id,
            "scan_id": finding.scan_id,
            "title": finding.title,
            "severity": finding.severity,
            "category": finding.category,
            "source": finding.source,
            "description": finding.description,
            "recommendation": finding.recommendation,
        }
    )


@api.route("/findings", methods=["POST"])
@login_required
def create_finding():
    """
    Create finding.
    """

    data = request.get_json()

    if not data:

        return error_response("JSON data required", 400)

    required = ["scan_id", "title", "severity"]

    for field in required:

        if field not in data:

            return error_response(f"{field} is required", 400)

    finding = finding_service.create(
        scan_id=data["scan_id"],
        title=data["title"],
        severity=data["severity"],
        category=data.get("category"),
        source=data.get("source"),
        description=data.get("description"),
        recommendation=data.get("recommendation"),
    )

    return success_response(
        data={"id": finding.id}, message="Finding created successfully", status_code=201
    )


@api.route("/findings/<int:finding_id>", methods=["DELETE"])
@login_required
def delete_finding(finding_id):
    """
    Delete finding.
    """

    deleted = finding_service.delete(finding_id)

    if not deleted:

        return error_response("Finding not found", 404)

    return success_response(message="Finding deleted successfully")
