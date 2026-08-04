"""
CloudShield Enterprise
Unified Scanner Routes
"""
from app.extensions import db
from flask import (
    render_template,
    request,
    jsonify,
    redirect,
    url_for,
)

from flask_login import (
    login_required,
    current_user,
)

from app.scanner import scanner

from app.scanner.forms import ScanForm
from app.scanner.helpers import get_tools
from app.scanner.validators import validate_target

from app.notifications.services import NotificationService

from app.security.services import SecurityService

from app.models.finding import Finding


# ==========================================================
# Scanner Dashboard
# ==========================================================

@scanner.route("/", methods=["GET", "POST"])
@login_required
def home():

    form = ScanForm()

    security_service = SecurityService()

    notification_service = NotificationService()

    result = None

    scan = None

    asset_id = None

    dashboard = {

        "status": "Waiting",

        "score": "--",

        "duration": 0,

        "findings": 0,

        "ports": 0,

    }

    # ==========================================================
    # Statistics
    # ==========================================================

    from app.models import SecurityScan
    from app.models.finding import Finding

    total_scans = SecurityScan.query.count()

    completed = SecurityScan.query.filter_by(
        status="Completed"
    ).count()

    total_findings = Finding.query.count()

    average_score = db.session.query(
        db.func.avg(SecurityScan.score)
    ).scalar()

    if average_score is None:
        average_score = 0

    success_rate = 0

    if total_scans:

        success_rate = round(
            (completed / total_scans) * 100,
        1
        )

    stats = {

        "total_scans": total_scans,

        "success_rate": success_rate,

        "findings": total_findings,

        "security_score": round(average_score, 1)

    }

    #
    # Open scanner from Asset
    #

    asset = request.args.get("asset")

    if asset:

        from app.models.asset import Asset

        db_asset = Asset.query.get(asset)

        if db_asset:

            form.target.data = db_asset.target

            form.asset_id.data = db_asset.id

    #
    # Default selections
    #

    mode = form.mode.data or "basic"

    category = form.category.data or "network"

    form.tool.choices = get_tools(

        category,

        mode

    )

    #
    # Execute Scan
    #

    if request.method == "POST":

        print("=" * 60)
        print(request.form)
        print("=" * 60)

        asset_id = form.asset_id.data

        mode = request.form.get(

            "mode",

            "basic"

        )

        category = request.form.get(

            "category",

            "network"

        )

        form.tool.choices = get_tools(

            category,

            mode

        )

        tool = (

            form.tool.data or ""

        ).strip()

        if tool == "":

            tool = None

        target = (

            form.target.data or ""

        ).strip()

        arguments = (

            form.arguments.data or ""

        ).strip()

        if not validate_target(target):

            result = {

                "success": False,

                "message": "Invalid Target"

            }

        else:

            args = (

                arguments.split()

                if arguments

                else []

            )

            try:

                print("=" * 60)
                print("POST RECEIVED")
                print("MODE      :", mode)
                print("CATEGORY  :", category)
                print("TOOL      :", tool)
                print("TARGET    :", target)
                print("ARGS      :", args)
                print("=" * 60)

                response = security_service.execute(

                    user_id=current_user.id,

                    asset_id=asset_id,

                    mode=mode,

                    category=category,

                    tool=tool,

                    target=target,

                    arguments=args
                )
                print("=" * 60)
                print("SERVICE RESPONSE"),
                print(response),
                print("=" * 60),

                scan = response.get("scan")

                result = response.get("result")

                if result is None:

                    result = {

                        "success": False,

                        "message": "No response"

                    }

                result["mode"] = mode

                result["category"] = category

                result["target"] = target

                result["tool"] = tool

                result["arguments"] = arguments

                if result.get("success"):

                    result["message"] = "Completed"

                else:

                    result["message"] = result.get(

                        "error",

                        "Failed"

                    )

                findings = 0

                if scan:

                    findings = Finding.query.filter_by(

                        scan_id=scan.id

                    ).count()

                ports = 0

                if isinstance(

                    result.get("ports"),

                    list

                ):

                    ports = len(

                        result["ports"]

                    )

                dashboard = {

                    "status": result["message"],

                    "score": (

                        scan.score

                        if scan

                        else "--"

                    ),

                    "duration": (

                        round(scan.duration, 2)

                        if scan

                        else 0

                    ),

                    "findings": findings,

                    "ports": ports,

                }

            except Exception as e:

                notification_service.create(

                    user_id=current_user.id,

                    title="Scan Failed",

                    message=str(e),

                    severity="High",

                )

                result = {

                    "success": False,

                    "message": str(e),

                    "error": str(e),

                }

                

    return render_template(

        "scanner/dashboard.html",

        form=form,

        result=result,

        dashboard=dashboard,

        stats=stats,

        asset_id=asset_id,

        scan=scan,

    )

# ==========================================================
# Tool Loader
# ==========================================================

@scanner.route("/tools/<mode>/<category>")
@login_required
def tools(mode, category):
    """
    Return available tools for the selected category/mode.
    """

    return jsonify(
        get_tools(category, mode)
    )


# ==========================================================
# Scan History
# ==========================================================

@scanner.route("/history")
@login_required
def history():

    from app.models import SecurityScan

    scans = (

        SecurityScan.query

        .order_by(

            SecurityScan.started_at.desc()

        )

        .all()

    )

    return render_template(

        "scanner/history.html",

        scans=scans

    )


# ==========================================================
# Recent Scan API
# ==========================================================

@scanner.route("/api/recent")
@login_required
def recent_scans():

    from app.models import SecurityScan

    scans = (

        SecurityScan.query

        .order_by(

            SecurityScan.started_at.desc()

        )

        .limit(10)

        .all()

    )

    return jsonify([

        {

            "id": scan.id,

            "target": scan.target,

            "category": scan.category,

            "tool": scan.tool,

            "status": scan.status,

            "score": scan.score,

            "risk": scan.risk,

            "started_at": (

                scan.started_at.isoformat()

                if scan.started_at

                else None

            )

        }

        for scan in scans

    ])   
# ==========================================================
# Scan Details
# ==========================================================

@scanner.route("/details/<int:scan_id>")
@login_required
def details(scan_id):

    from app.models import SecurityScan
    from app.scanner.services.report_builder import ReportBuilder

    scan = SecurityScan.query.get_or_404(scan_id)

    report = ReportBuilder(scan).build()

    return render_template(

        "scanner/details.html",

        scan=scan,

        report=report,

        findings=scan.findings

    )


# ==========================================================
# Delete Scan
# ==========================================================

@scanner.route("/delete/<int:scan_id>")
@login_required
def delete_scan(scan_id):

    from app.models import SecurityScan
    from app.models.finding import Finding
    from app.models.report import Report
    from app.extensions import db

    scan = SecurityScan.query.get_or_404(scan_id)

    #
    # Delete Findings
    #

    Finding.query.filter_by(

        scan_id=scan.id

    ).delete()

    #
    # Delete Reports
    #

    Report.query.filter_by(

        scan_id=scan.id

    ).delete()

    #
    # Delete Scan
    #

    db.session.delete(scan)

    db.session.commit()

    return redirect(

        url_for(

            "scanner.history"

        )

    )   
# ==========================================================
# Live Progress
# ==========================================================

@scanner.route("/progress/<int:scan_id>")
@login_required
def progress(scan_id):

    from app.scanner.live import live_manager

    progress = live_manager.get(scan_id)

    if progress is None:

        return jsonify({

            "success": False,

            "error": "Scan not found"

        }), 404

    return jsonify({

        "success": True,

        "data": progress.to_dict()

    })


# ==========================================================
# Scan Status
# ==========================================================

@scanner.route("/status/<int:scan_id>")
@login_required
def status(scan_id):

    from app.scanner.live import live_manager

    progress = live_manager.get(scan_id)

    if progress is None:

        return jsonify({

            "status": "Unknown"

        })

    return jsonify({

        "status": progress.status.value

    })


# ==========================================================
# Live Scanner
# ==========================================================

@scanner.route("/live/<int:scan_id>")
@login_required
def live(scan_id):

    return render_template(

        "scanner/live.html",

        scan_id=scan_id

    )   