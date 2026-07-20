"""
CloudShield Enterprise
Findings Routes
"""

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash
)
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


service = FindingsService()


@findings_ui.route("/")
@login_required
def index():

    dashboard = FindingsService.dashboard()

    recent = FindingsService.latest(10)

    return render_template(

        "findings/index.html",

        dashboard=dashboard,

        recent=recent,

        findings=FindingsService.all()

    )

@findings_ui.route("/view/<int:finding_id>")
@login_required
def view(finding_id):

    finding = Finding.query.get_or_404(finding_id)

    return render_template(

        "findings/view.html",

        finding=finding

    )


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

        return redirect(url_for(
            "findings_ui.view",
            finding_id=finding.id
        ))

    return render_template(
        "findings/edit.html",
        finding=finding
    )

@findings_ui.route("/delete/<int:finding_id>", methods=["GET", "POST"])
@login_required
def delete(finding_id):

    finding = Finding.query.get_or_404(finding_id)

    if request.method == "POST":

        db.session.delete(finding)

        db.session.commit()

        # AJAX request
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":

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
            status=request.form.get("status")
        )

        db.session.add(finding)
        db.session.commit()

        flash("Finding created successfully.", "success")

        return redirect(url_for("findings_ui.index"))

    return render_template(
        "findings/create.html",
        projects=projects,
        assets=assets,
        scans=scans
    )

# =====================================================
# Resolve Finding
# =====================================================

@findings_ui.route("/resolve/<int:finding_id>", methods=["POST"])
@login_required
def resolve(finding_id):

    finding = Finding.query.get_or_404(finding_id)

    finding.status = "Resolved"

    db.session.commit()

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":

        return {
            "success": True,
            "message": "Finding resolved successfully."
        }

    flash("Finding resolved successfully.", "success")

    return redirect(url_for("findings_ui.list_findings"))

# =====================================================
# Reopen Finding
# =====================================================

@findings_ui.route("/reopen/<int:finding_id>", methods=["POST"])
@login_required
def reopen(finding_id):

    FindingsService.reopen(finding_id)

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


# =====================================================
# False Positive
# =====================================================

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


# =====================================================
# Remove False Positive
# =====================================================

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

# =====================================================
# Export CSV
# =====================================================

@findings_ui.route("/export/csv")
@login_required
def export_csv():

    csv_data = FindingsService.export_csv()

    return Response(

        csv_data,

        mimetype="text/csv",

        headers={

            "Content-Disposition":

            "attachment; filename=findings.csv"

        }

    )
# =====================================================
# Export JSON
# =====================================================

@findings_ui.route("/export/json")
@login_required
def export_json():

    json_data = FindingsService.export_json()

    return Response(

        json_data,

        mimetype="application/json",

        headers={

            "Content-Disposition":

            "attachment; filename=findings.json"

        }

    )
# =====================================================
# PDF Report
# =====================================================

@findings_ui.route("/report/pdf")
@login_required
def pdf_report():

    flash(

        "Enterprise PDF reporting will be integrated with the Reports module.",

        "info"

    )

    return redirect(

        url_for(

            "reports.index"

        )

    )
# =====================================================
# Dashboard API
# =====================================================

@findings_ui.route("/api/dashboard")
@login_required
def api_dashboard():

    return jsonify(

        FindingsService.dashboard()

    )

# =====================================================
# Severity Statistics
# =====================================================

@findings_ui.route("/api/severity")
@login_required
def api_severity():

    counts = FindingsService.counts()

    return jsonify({

        "Critical": counts["critical"],

        "High": counts["high"],

        "Medium": counts["medium"],

        "Low": counts["low"]

    })

# =====================================================
# Category Statistics
# =====================================================

@findings_ui.route("/api/categories")
@login_required
def api_categories():

    from sqlalchemy import func

    data = (

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
# =====================================================
# Monthly Trend
# =====================================================

@findings_ui.route("/api/monthly")
@login_required
def api_monthly():

    from sqlalchemy import func

    rows = (

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
@findings_ui.route("/list")
@login_required
def list_findings():

    search = request.args.get("search","").strip()

    sort_by = request.args.get("sort", "created_at")

    order = request.args.get("order", "desc")

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

    findings = pagination.items

    return render_template(

        "findings/list.html",

        findings=findings,
        pagination=pagination,
        search=search,
        sort_by=sort_by,
        order=order,
        severity=severity,
        status=status,
        category=category

    )

@findings_ui.route("/bulk-delete", methods=["POST"])
@login_required
def bulk_delete():

    print("===== BULK DELETE =====")

    print(request.form)

    ids = request.form.getlist("finding_ids")

    print(ids)

    FindingsService.bulk_delete(ids)

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":

        return {

            "success": True,

            "message": f"{len(ids)} finding(s) deleted."

        }

    flash(f"{len(ids)} finding(s) deleted.", "success")

    return redirect(url_for("findings_ui.list_findings"))
  
@findings_ui.route("/bulk-resolve", methods=["POST"])
@login_required
def bulk_resolve():

    ids = request.form.getlist("finding_ids")

    if not ids:

        flash("No findings selected.", "warning")

        return redirect(url_for("findings_ui.list_findings"))

    FindingsService.bulk_resolve(ids)

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":

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

@findings_ui.route("/export-selected/csv", methods=["POST"])
@login_required
def export_selected_csv():

    ids = request.form.getlist("finding_ids")

    print("EXPORT IDS:", ids)

    csv_data = FindingsService.export_selected_csv(ids)

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=selected_findings.csv"
        }
    )

@findings_ui.route("/export-selected/json", methods=["POST"])
@login_required
def export_selected_json():

    ids = request.form.getlist("finding_ids")

    json_data = FindingsService.export_selected_json(ids)

    return Response(

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
@login_required
def upload_evidence(finding_id):

    file = request.files.get("evidence")

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

@findings_ui.route("/evidence/<int:evidence_id>/download")
@login_required
def download_evidence(evidence_id):

    evidence = Evidence.query.get_or_404(evidence_id)

    return send_file(

        evidence.filepath,

        as_attachment=True,

        download_name=evidence.filename

    )
import os

@findings_ui.route(
    "/evidence/<int:evidence_id>/delete",
    methods=["POST"]
)
@login_required
def delete_evidence(evidence_id):

    evidence = Evidence.query.get_or_404(evidence_id)

    if os.path.exists(evidence.filepath):

        os.remove(evidence.filepath)

    finding_id = evidence.finding_id

    db.session.delete(evidence)

    db.session.commit()

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