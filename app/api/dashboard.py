"""
CloudShield Enterprise
Dashboard API
"""

from flask_login import login_required

from app.api import api
from app.api.responses import success_response

from app.services.dashboard_service import DashboardService

dashboard_service = DashboardService()


@api.route("/dashboard", methods=["GET"])
@login_required
def dashboard_statistics():
    """
    Dashboard statistics.
    """

    return success_response(

        data=dashboard_service.statistics(),

        message="Dashboard statistics"

    )


@api.route("/dashboard/latest-scans", methods=["GET"])
@login_required
def latest_scans():
    """
    Latest scans.
    """

    scans = dashboard_service.latest_scans()

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
            )

        })

    return success_response(

        data=data,

        message="Latest scans"

    )