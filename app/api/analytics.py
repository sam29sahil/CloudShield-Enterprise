"""
CloudShield Enterprise
Analytics API
"""

from flask_login import login_required
from sqlalchemy import func

from app.api import api
from app.api.responses import success_response

from app.extensions import db
from app.models import Asset
from app.models import SecurityScan
from app.models import Finding


@api.route("/analytics", methods=["GET"])
@login_required
def analytics():

    total_assets = Asset.query.count()

    total_scans = SecurityScan.query.count()

    total_findings = Finding.query.count()

    average_score = db.session.query(
        func.avg(Scan.score)
    ).scalar()

    if average_score is None:
        average_score = 0

    average_score = round(average_score)

    critical = Finding.query.filter_by(
        severity="Critical"
    ).count()

    high = Finding.query.filter_by(
        severity="High"
    ).count()

    medium = Finding.query.filter_by(
        severity="Medium"
    ).count()

    low = Finding.query.filter_by(
        severity="Low"
    ).count()

    return success_response(

        data={

            "assets": total_assets,

            "scans": total_scans,

            "findings": total_findings,

            "average_score": average_score,

            "critical": critical,

            "high": high,

            "medium": medium,

            "low": low

        },

        message="Analytics generated successfully"

    )


@api.route("/analytics/severity", methods=["GET"])
@login_required
def severity():

    return success_response(

        data={

            "critical": Finding.query.filter_by(
                severity="Critical"
            ).count(),

            "high": Finding.query.filter_by(
                severity="High"
            ).count(),

            "medium": Finding.query.filter_by(
                severity="Medium"
            ).count(),

            "low": Finding.query.filter_by(
                severity="Low"
            ).count()

        },

        message="Severity analytics"

    )


@api.route("/analytics/assets", methods=["GET"])
@login_required
def asset_analytics():

    assets = Asset.query.all()

    data = []

    for asset in assets:

        data.append({

            "id": asset.id,

            "name": asset.name,

            "target": asset.target,

            "score": asset.score,

            "risk": asset.risk

        })

    return success_response(

        data=data,

        message="Asset analytics"

    )


@api.route("/analytics/scans", methods=["GET"])
@login_required
def scan_analytics():

    scans = SecurityScan.query.all()

    data = []

    for scan in scans:

        data.append({

            "id": scan.id,

            "asset_id": scan.asset_id,

            "score": scan.score,

            "risk": scan.risk,

            "scan_type": scan.scan_type,

            "started_at": (
                scan.started_at.isoformat()
                if scan.started_at
                else None
            )

        })

    return success_response(

        data=data,

        message="Scan analytics"

    )