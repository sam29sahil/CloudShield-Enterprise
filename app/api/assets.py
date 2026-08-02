"""
CloudShield Enterprise
Assets API
"""

from flask import request
from flask_login import login_required

from app.api import api
from app.api.responses import success_response, error_response
from app.services.asset_service import AssetService

asset_service = AssetService()


@api.route("/assets", methods=["GET"])
@login_required
def get_assets():
    """
    Get all assets with pagination and filters.
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

    risk = request.args.get("risk")
    asset_type = request.args.get("asset_type")
    project_id = request.args.get("project_id", type=int)
    search = request.args.get("q")

    query = asset_service.query()

    if risk:
        query = query.filter_by(
            risk=risk
        )

    if asset_type:
        query = query.filter_by(
            asset_type=asset_type
        )

    if project_id:
        query = query.filter_by(
            project_id=project_id
        )

    if search:

        from app.models import Asset

        query = query.filter(
            Asset.name.ilike(f"%{search}%")
        )

    pagination = query.paginate(

        page=page,

        per_page=per_page,

        error_out=False

    )

    assets = pagination.items

    data = []

    for asset in assets:

        data.append({

            "id": asset.id,

            "project_id": asset.project_id,

            "name": asset.name,

            "target": asset.target,

            "asset_type": asset.asset_type,

            "score": asset.score,

            "risk": asset.risk,

            "created_at": (
                asset.created_at.isoformat()
                if asset.created_at
                else None
            )

        })

    return success_response(

        data={

            "items": data,

            "page": pagination.page,

            "pages": pagination.pages,

            "per_page": pagination.per_page,

            "total": pagination.total,

            "has_next": pagination.has_next,

            "has_prev": pagination.has_prev

        },

        message="Assets retrieved successfully"

    )


@api.route("/assets/<int:asset_id>", methods=["GET"])
@login_required
def get_asset(asset_id):
    """
    Get asset by ID.
    """

    asset = asset_service.get(asset_id)

    if not asset:

        return error_response(

            "Asset not found",

            404

        )

    data = {

        "id": asset.id,

        "project_id": asset.project_id,

        "name": asset.name,

        "target": asset.target,

        "asset_type": asset.asset_type,

        "score": asset.score,

        "risk": asset.risk,

        "created_at": (
            asset.created_at.isoformat()
            if asset.created_at
            else None
        )

    }

    return success_response(

        data=data,

        message="Asset retrieved successfully"

    )


@api.route("/assets", methods=["POST"])
@login_required
def create_asset():
    """
    Create a new asset.
    """

    data = request.get_json()

    if not data:

        return error_response(

            "JSON data is required",

            400

        )

    required = [

        "project_id",

        "name",

        "target",

        "asset_type"

    ]

    for field in required:

        if field not in data:

            return error_response(

                f"{field} is required",

                400

            )

    asset = asset_service.create(

        project_id=data["project_id"],

        name=data["name"],

        target=data["target"],

        asset_type=data["asset_type"]

    )

    return success_response(

        data={

            "id": asset.id,

            "name": asset.name

        },

        message="Asset created successfully",

        status_code=201

    )


@api.route("/assets/<int:asset_id>/score", methods=["PUT"])
@login_required
def update_asset_score(asset_id):
    """
    Update asset score and risk.
    """

    asset = asset_service.get(asset_id)

    if not asset:

        return error_response(

            "Asset not found",

            404

        )

    data = request.get_json()

    if not data:

        return error_response(

            "JSON data is required",

            400

        )

    score = data.get("score")
    risk = data.get("risk")

    if score is None or risk is None:

        return error_response(

            "score and risk are required",

            400

        )

    asset_service.update_score(

        asset,

        score,

        risk

    )

    return success_response(

        message="Asset score updated successfully"

    )


@api.route("/assets/<int:asset_id>", methods=["DELETE"])
@login_required
def delete_asset(asset_id):
    """
    Delete asset.
    """

    asset = asset_service.get(asset_id)

    if not asset:

        return error_response(

            "Asset not found",

            404

        )

    from app.extensions import db

    db.session.delete(asset)
    db.session.commit()

    return success_response(

        message="Asset deleted successfully"

    )