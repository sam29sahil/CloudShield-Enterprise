"""
CloudShield Enterprise
Findings Routes
"""

<<<<<<< HEAD
from flask import render_template, request, redirect, url_for, flash
=======
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
from flask import jsonify
from flask import Response
from app.extensions import db
from app.models.finding import Finding
from app.models.project import Project
from flask_login import login_required
from app.models.asset import Asset
from app.findings.evidence_service import EvidenceService
from app.models.security_scan import SecurityScan
from app.findings_ui import findings_ui
from app.findings_ui.services import FindingsService
from app.findings_ui.forms import FindingUpdateForm

<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
service = FindingsService()


@findings_ui.route("/")
@login_required
def index():

    dashboard = FindingsService.dashboard()

    recent = FindingsService.latest(10)

    return render_template(
<<<<<<< HEAD
        "findings/index.html",
        dashboard=dashboard,
        recent=recent,
        findings=FindingsService.all(),
    )

=======

        "findings/index.html",

        dashboard=dashboard,

        recent=recent,

        findings=FindingsService.all()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@findings_ui.route("/view/<int:finding_id>")
@login_required
def view(finding_id):

    finding = Finding.query.get_or_404(finding_id)

<<<<<<< HEAD
    return render_template("findings/view.html", finding=finding)
=======
    return render_template(

        "findings/view.html",

        finding=finding

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@findings_ui.route("/edit/<int:finding_id>", methods=["GET", "POST"])
@login_required
def edit(finding_id):

    finding = Finding.query.get_or_404(finding_id)

    if request.method == "POST":

        finding.title = request.form["title"]
        finding.severity = request.form["severity"]
        finding.status = request.form["status"]
        finding.cvss = float(request.form["cvss"] or 0)
        finding.category = request.form["category"]
        finding.description = request.form["description"]
        finding.evidence = request.form["evidence"]
        finding.recommendation = request.form["recommendation"]

        db.session.commit()

        flash("Finding updated successfully.", "success")

<<<<<<< HEAD
        return redirect(url_for("findings_ui.view", finding_id=finding.id))

    return render_template("findings/edit.html", finding=finding)

=======
        return redirect(url_for(
            "findings_ui.view",
            finding_id=finding.id
        ))

    return render_template(
        "findings/edit.html",
        finding=finding
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@findings_ui.route("/delete/<int:finding_id>", methods=["GET", "POST"])
@login_required
def delete(finding_id):

    finding = Finding.query.get_or_404(finding_id)

    if request.method == "POST":

        db.session.delete(finding)

        db.session.commit()

        # AJAX request
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":

<<<<<<< HEAD
            return {"success": True, "message": "Finding deleted successfully."}

        flash("Finding deleted successfully.", "success")

        return redirect(url_for("findings_ui.list_findings"))

    return render_template("findings/delete.html", finding=finding)


=======
            return {
                "success": True,
                "message": "Finding deleted successfully."
            }

        flash(
            "Finding deleted successfully.",
            "success"
        )

        return redirect(
            url_for("findings_ui.list_findings")
        )

    return render_template(
        "findings/delete.html",
        finding=finding
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/create", methods=["GET", "POST"])
@login_required
def create():

    projects = Project.query.all()
    assets = Asset.query.all()
    scans = SecurityScan.query.all()

    if request.method == "POST":

        finding = Finding(
            project_id=request.form.get("project_id"),
            asset_id=request.form.get("asset_id"),
            scan_id=request.form.get("scan_id") or None,
            title=request.form.get("title"),
            severity=request.form.get("severity"),
            cvss=float(request.form.get("cvss") or 0),
            category=request.form.get("category"),
            description=request.form.get("description"),
            evidence=request.form.get("evidence"),
            recommendation=request.form.get("recommendation"),
<<<<<<< HEAD
            status=request.form.get("status"),
=======
            status=request.form.get("status")
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        db.session.add(finding)
        db.session.commit()

        flash("Finding created successfully.", "success")

        return redirect(url_for("findings_ui.index"))

    return render_template(
<<<<<<< HEAD
        "findings/create.html", projects=projects, assets=assets, scans=scans
    )


=======
        "findings/create.html",
        projects=projects,
        assets=assets,
        scans=scans
    )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# =====================================================
# Resolve Finding
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/resolve/<int:finding_id>", methods=["POST"])
@login_required
def resolve(finding_id):

    finding = Finding.query.get_or_404(finding_id)

    finding.status = "Resolved"

    db.session.commit()

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":

<<<<<<< HEAD
        return {"success": True, "message": "Finding resolved successfully."}
=======
        return {
            "success": True,
            "message": "Finding resolved successfully."
        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    flash("Finding resolved successfully.", "success")

    return redirect(url_for("findings_ui.list_findings"))

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# =====================================================
# Reopen Finding
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/reopen/<int:finding_id>", methods=["POST"])
@login_required
def reopen(finding_id):

    FindingsService.reopen(finding_id)

<<<<<<< HEAD
    flash("Finding reopened successfully.", "warning")

    return redirect(url_for("findings_ui.view", finding_id=finding_id))
=======
    flash(

        "Finding reopened successfully.",

        "warning"

    )

    return redirect(

        url_for(

            "findings_ui.view",

            finding_id=finding_id

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# False Positive
# =====================================================

<<<<<<< HEAD

@findings_ui.route("/false-positive/<int:finding_id>", methods=["POST"])
@login_required
def false_positive(finding_id):

    FindingsService.mark_false_positive(finding_id)

    flash("Finding marked as False Positive.", "info")

    return redirect(url_for("findings_ui.view", finding_id=finding_id))
=======
@findings_ui.route(
    "/false-positive/<int:finding_id>",
    methods=["POST"]
)
@login_required
def false_positive(finding_id):

    FindingsService.mark_false_positive(

        finding_id

    )

    flash(

        "Finding marked as False Positive.",

        "info"

    )

    return redirect(

        url_for(

            "findings_ui.view",

            finding_id=finding_id

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# Remove False Positive
# =====================================================

<<<<<<< HEAD

@findings_ui.route("/false-positive/remove/<int:finding_id>", methods=["POST"])
@login_required
def remove_false_positive(finding_id):

    FindingsService.unmark_false_positive(finding_id)

    flash("False Positive removed.", "success")

    return redirect(url_for("findings_ui.view", finding_id=finding_id))

=======
@findings_ui.route(
    "/false-positive/remove/<int:finding_id>",
    methods=["POST"]
)
@login_required
def remove_false_positive(finding_id):

    FindingsService.unmark_false_positive(

        finding_id

    )

    flash(

        "False Positive removed.",

        "success"

    )

    return redirect(

        url_for(

            "findings_ui.view",

            finding_id=finding_id

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# =====================================================
# Export CSV
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/export/csv")
@login_required
def export_csv():

    csv_data = FindingsService.export_csv()

    return Response(
<<<<<<< HEAD
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=findings.csv"},
    )


=======

        csv_data,

        mimetype="text/csv",

        headers={

            "Content-Disposition":

            "attachment; filename=findings.csv"

        }

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# =====================================================
# Export JSON
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/export/json")
@login_required
def export_json():

    json_data = FindingsService.export_json()

    return Response(
<<<<<<< HEAD
        json_data,
        mimetype="application/json",
        headers={"Content-Disposition": "attachment; filename=findings.json"},
    )


=======

        json_data,

        mimetype="application/json",

        headers={

            "Content-Disposition":

            "attachment; filename=findings.json"

        }

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# =====================================================
# PDF Report
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/report/pdf")
@login_required
def pdf_report():

    flash(
<<<<<<< HEAD
        "Enterprise PDF reporting will be integrated with the Reports module.", "info"
    )

    return redirect(url_for("reports.index"))


=======

        "Enterprise PDF reporting will be integrated with the Reports module.",

        "info"

    )

    return redirect(

        url_for(

            "reports.index"

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# =====================================================
# Dashboard API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/api/dashboard")
@login_required
def api_dashboard():

<<<<<<< HEAD
    return jsonify(FindingsService.dashboard())

=======
    return jsonify(

        FindingsService.dashboard()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# =====================================================
# Severity Statistics
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/api/severity")
@login_required
def api_severity():

    counts = FindingsService.counts()

<<<<<<< HEAD
    return jsonify(
        {
            "Critical": counts["critical"],
            "High": counts["high"],
            "Medium": counts["medium"],
            "Low": counts["low"],
        }
    )

=======
    return jsonify({

        "Critical": counts["critical"],

        "High": counts["high"],

        "Medium": counts["medium"],

        "Low": counts["low"]

    })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

# =====================================================
# Category Statistics
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/api/categories")
@login_required
def api_categories():

    from sqlalchemy import func

    data = (
<<<<<<< HEAD
        db.session.query(Finding.category, func.count(Finding.id))
        .group_by(Finding.category)
        .all()
    )

    return jsonify({category or "Unknown": total for category, total in data})


=======

        db.session.query(

            Finding.category,

            func.count(Finding.id)

        )

        .group_by(

            Finding.category

        )

        .all()

    )

    return jsonify({

        category or "Unknown": total

        for category, total in data

    })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# =====================================================
# Monthly Trend
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/api/monthly")
@login_required
def api_monthly():

    from sqlalchemy import func

    rows = (
<<<<<<< HEAD
        db.session.query(
            func.strftime("%Y-%m", Finding.created_at), func.count(Finding.id)
        )
        .group_by(func.strftime("%Y-%m", Finding.created_at))
        .all()
    )

    return jsonify({month: total for month, total in rows})


=======

        db.session.query(

            func.strftime(

                "%Y-%m",

                Finding.created_at

            ),

            func.count(

                Finding.id

            )

        )

        .group_by(

            func.strftime(

                "%Y-%m",

                Finding.created_at

            )

        )

        .all()

    )

    return jsonify({

        month: total

        for month, total in rows

    })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/list")
@login_required
def list_findings():

<<<<<<< HEAD
    search = request.args.get("search", "").strip()
=======
    search = request.args.get("search","").strip()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    sort_by = request.args.get("sort", "created_at")

    order = request.args.get("order", "desc")

<<<<<<< HEAD
    severity = request.args.get("severity", "")

    status = request.args.get("status", "")

    category = request.args.get("category", "")

    query = FindingsService.filter_findings(
        search=search, severity=severity, status=status, category=category
    )
    query = FindingsService.sort(query, sort_by, order)

    page = request.args.get("page", 1, type=int)

    pagination = query.paginate(page=page, per_page=10, error_out=False)
=======
    severity = request.args.get("severity","")

    status = request.args.get("status","")

    category = request.args.get("category","")

    query = FindingsService.filter_findings(

        search=search,

        severity=severity,

        status=status,

        category=category

    )
    query = FindingsService.sort(

        query,

        sort_by,

        order

    )

    page = request.args.get("page", 1, type=int)

    pagination = query.paginate(

        page=page,

        per_page=10,

        error_out=False

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    findings = pagination.items

    return render_template(
<<<<<<< HEAD
        "findings/list.html",
=======

        "findings/list.html",

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        findings=findings,
        pagination=pagination,
        search=search,
        sort_by=sort_by,
        order=order,
        severity=severity,
        status=status,
<<<<<<< HEAD
        category=category,
    )

=======
        category=category

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@findings_ui.route("/bulk-delete", methods=["POST"])
@login_required
def bulk_delete():

    print("===== BULK DELETE =====")

    print(request.form)

    ids = request.form.getlist("finding_ids")

    print(ids)

    FindingsService.bulk_delete(ids)

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":

<<<<<<< HEAD
        return {"success": True, "message": f"{len(ids)} finding(s) deleted."}
=======
        return {

            "success": True,

            "message": f"{len(ids)} finding(s) deleted."

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    flash(f"{len(ids)} finding(s) deleted.", "success")

    return redirect(url_for("findings_ui.list_findings"))
<<<<<<< HEAD


=======
  
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/bulk-resolve", methods=["POST"])
@login_required
def bulk_resolve():

    ids = request.form.getlist("finding_ids")

    if not ids:

        flash("No findings selected.", "warning")

        return redirect(url_for("findings_ui.list_findings"))

    FindingsService.bulk_resolve(ids)

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":

<<<<<<< HEAD
        return {"success": True, "message": f"{len(ids)} finding(s) resolved."}

    flash(f"{len(ids)} finding(s) resolved.", "success")

    return redirect(url_for("findings_ui.list_findings"))

=======
        return {

            "success": True,

            "message": f"{len(ids)} finding(s) resolved."

        }

    flash(

        f"{len(ids)} finding(s) resolved.",

        "success"

    )

    return redirect(

        url_for("findings_ui.list_findings")

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@findings_ui.route("/export-selected/csv", methods=["POST"])
@login_required
def export_selected_csv():

    ids = request.form.getlist("finding_ids")

    print("EXPORT IDS:", ids)

    csv_data = FindingsService.export_selected_csv(ids)

    return Response(
        csv_data,
        mimetype="text/csv",
<<<<<<< HEAD
        headers={"Content-Disposition": "attachment; filename=selected_findings.csv"},
    )


=======
        headers={
            "Content-Disposition":
            "attachment; filename=selected_findings.csv"
        }
    )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/export-selected/json", methods=["POST"])
@login_required
def export_selected_json():

    ids = request.form.getlist("finding_ids")

    json_data = FindingsService.export_selected_json(ids)

    return Response(
<<<<<<< HEAD
        json_data,
        mimetype="application/json",
        headers={"Content-Disposition": "attachment; filename=selected_findings.json"},
    )


@findings_ui.route("/<int:finding_id>/upload", methods=["POST"])
=======

        json_data,

        mimetype="application/json",

        headers={

            "Content-Disposition":
            "attachment; filename=selected_findings.json"

        }

    )

@findings_ui.route(
    "/<int:finding_id>/upload",
    methods=["POST"]
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@login_required
def upload_evidence(finding_id):

    file = request.files.get("evidence")

<<<<<<< HEAD
    EvidenceService.upload(file, finding_id)

    flash("Evidence uploaded successfully.", "success")

    return redirect(url_for("findings_ui.view", finding_id=finding_id))


from flask import send_file


=======
    EvidenceService.upload(

        file,

        finding_id

    )

    flash(

        "Evidence uploaded successfully.",

        "success"

    )

    return redirect(

        url_for(

            "findings_ui.view",

            finding_id=finding_id

        )

    )

from flask import send_file

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@findings_ui.route("/evidence/<int:evidence_id>/download")
@login_required
def download_evidence(evidence_id):

    evidence = Evidence.query.get_or_404(evidence_id)

    return send_file(
<<<<<<< HEAD
        evidence.filepath, as_attachment=True, download_name=evidence.filename
    )


import os


@findings_ui.route("/evidence/<int:evidence_id>/delete", methods=["POST"])
=======

        evidence.filepath,

        as_attachment=True,

        download_name=evidence.filename

    )
import os

@findings_ui.route(
    "/evidence/<int:evidence_id>/delete",
    methods=["POST"]
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@login_required
def delete_evidence(evidence_id):

    evidence = Evidence.query.get_or_404(evidence_id)

    if os.path.exists(evidence.filepath):

        os.remove(evidence.filepath)

    finding_id = evidence.finding_id

    db.session.delete(evidence)

    db.session.commit()

<<<<<<< HEAD
    flash("Evidence deleted successfully.", "success")

    return redirect(url_for("findings_ui.view", finding_id=finding_id))
=======
    flash(

        "Evidence deleted successfully.",

        "success"

    )

    return redirect(

        url_for(

            "findings_ui.view",

            finding_id=finding_id

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
