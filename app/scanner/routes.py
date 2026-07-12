"""
CloudShield Enterprise
Universal Scanner Routes
"""

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


    result = None

    mode = form.mode.data or "quick"
    category = form.category.data or "network"

    form.tool.choices = get_tools(category, mode)

    if request.method == "POST":

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

        result=result

    )


@scanner.route("/tools/<mode>/<category>")
@login_required
def tools(mode, category):

    return jsonify(

        get_tools(category, mode)

    )