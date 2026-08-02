"""
CloudShield Enterprise
Universal Scanner Routes
"""
from flask import redirect, url_for
from app.extensions import db
from flask import render_template, request, jsonify
from flask_login import login_required, current_user

from app.scanner import scanner
from app.scanner.forms import ScanForm
from app.scanner.helpers import get_tools
from app.scanner.validators import validate_target
from app.notifications.services import NotificationService

# Deep Scanner
from app.scanner.universal.services import ScanService

# Quick Scanner
from app.scanner.basic.services import BasicScanService


@scanner.route("/", methods=["GET", "POST"])
@login_required
def home():

    form = ScanForm()

    deep_service = ScanService()
    quick_service = BasicScanService()
    notification_service = NotificationService()

    # ----------------------------
    # Open scanner from an Asset
    # ----------------------------

    asset_id = request.args.get("asset")
    if asset_id:

        from app.models.asset import Asset

        asset = Asset.query.get(asset_id)

        if asset:

            form.target.data = asset.target
            form.asset_id.data = asset.id


    result = None

    dashboard = {

        "status": "Waiting",

        "score": "--",

        "duration": "0",

        "findings": 0,

        "ports": 0

    }

    mode = form.mode.data or "quick"
    category = form.category.data or "network"

    form.tool.choices = get_tools(category, mode)

    if request.method == "POST":

        asset_id = form.asset_id.data

        mode = request.form.get("mode", "quick")
        category = request.form.get("category", "network")

        form.tool.choices = get_tools(category, mode)

        # -------------------------------------------------
        # QUICK MODE DOES NOT USE TOOL DROPDOWN
        # -------------------------------------------------

        if mode == "basic":

            tool = "quick_scan"

        else:

            tool = (form.tool.data or "").strip()

        target = (form.target.data or "").strip()

        arguments = (form.arguments.data or "").strip()

        if not validate_target(target):

            result = {
                "success": False,
                "error": "Invalid Target"
            }

        else:

            args = arguments.split() if arguments else None

            print("\n" + "=" * 60)
            print("MODE   :", mode)
            print("TOOL   :", tool)
            print("TARGET :", target)
            print("=" * 60)

            try:

                if mode == "basic":

                    print(">>> USING BASIC SCANNER <<<")

                    response = quick_service.execute(

                        user_id=current_user.id,
                        asset_id=asset_id,
                        category=category,
                        tool=tool,
                        target=target,
                        arguments=args

                    )

                else:

                    print(">>> USING UNIVERSAL SCANNER <<<")

                    response = deep_service.execute(

                        user_id=current_user.id,
                        asset_id=asset_id,
                        category=category,
                        tool=tool,
                        target=target,
                        arguments=args

                    )

                result = response["result"]

                result["mode"] = mode
                result["category"] = category
                result["tool"] = tool
                result["target"] = target
                result["arguments"] = arguments

                if result.get("success") is False:

                    result["message"] = result.get(
                        "error",
                        "Failed"
                    )

                else:

                    result["message"] = "Completed"
                # ------------------------------------
                # Dashboard Data
                # ------------------------------------

                scan = response["scan"]

                from app.models.finding import Finding

                findings = Finding.query.filter_by(
                scan_id=scan.id
                ).count()

                ports = 0

                if isinstance(result.get("ports"), list):

                    ports = len(result["ports"])

                dashboard = {

                "status": result["message"],

                "score": scan.score,

                "duration": round(scan.duration, 2),

                "findings": findings,

                "ports": ports

            }
            except Exception as e:

                print(e)

                notification_service.create(

                    user_id=current_user.id,

                    title="Scan Failed",

                    message=str(e),

                    severity="High"

                )

                result = {

                    "success": False,

                    "error": str(e),

                    "message": str(e)

                }

    return render_template(

        "scanner/scan.html",

        form=form,

        result=result,

        dashboard=dashboard,

        asset_id=asset_id

    )


@scanner.route("/tools/<mode>/<category>")
@login_required
def tools(mode, category):

    return jsonify(

        get_tools(category, mode)

    )

@scanner.route("/history")
@login_required
def history():

    from app.models import SecurityScan

    scans = SecurityScan.query.order_by(
        SecurityScan.started_at.desc()
    ).all()

    return render_template(
        "scanner/history.html",
        scans=scans
    )

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
@scanner.route("/delete/<int:scan_id>")
@login_required
def delete_scan(scan_id):

    from app.extensions import db
    from app.models import SecurityScan
    from app.models.finding import Finding
    from app.models.report import Report

    scan = SecurityScan.query.get_or_404(scan_id)

    # Delete Findings
    Finding.query.filter_by(
        scan_id=scan.id
    ).delete()

    # Delete Reports
    Report.query.filter_by(
        scan_id=scan.id
    ).delete()

    db.session.delete(scan)

    db.session.commit()

    return redirect(
        url_for("scanner.history")
    )

@scanner.route("/progress/<int:scan_id>")
@login_required
def progress(scan_id):

    from flask import jsonify
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

@scanner.route("/status/<int:scan_id>")
@login_required
def status(scan_id):

    from flask import jsonify
    from app.scanner.live import live_manager

    progress = live_manager.get(scan_id)

    if progress is None:

        return jsonify({

            "status": "Unknown"

        })

    return jsonify({

        "status": progress.status.value

    })
    @scanner.route("/live/<int:scan_id>")
@login_required
def live(scan_id):

    from flask import render_template

    return render_template(

        "scanner/live.html",

        scan_id=scan_id

    )
