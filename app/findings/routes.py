"""
CloudShield Enterprise
Findings Routes
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

from flask_login import login_required

from app.findings import (
    FindingService,
    FindingStatistics,
    FindingFilters,
    FindingExporter,
)

bp = Blueprint("findings", __name__, url_prefix="/findings")

service = FindingService()

statistics = FindingStatistics()

filters = FindingFilters()

exporter = FindingExporter()


# =====================================================
# DASHBOARD
# =====================================================


@bp.route("/")
@login_required
def dashboard():

    data = statistics.dashboard()

    recent = service.latest(10)

    return render_template("findings/dashboard.html", dashboard=data, recent=recent)


# =====================================================
# FINDINGS LIST
# =====================================================


@bp.route("/list")
@login_required
def findings():

    page = request.args.get("page", 1, type=int)

    query = filters.apply(request.args)

    pagination = query.paginate(page=page, per_page=20)

    return render_template(
        "findings/list.html", pagination=pagination, findings=pagination.items
    )


# =====================================================
# DETAILS
# =====================================================


@bp.route("/<int:finding_id>")
@login_required
def details(finding_id):

    finding = service.get(finding_id)

    return render_template("findings/details.html", finding=finding)


# =====================================================
# CREATE
# =====================================================


@bp.route("/create", methods=["POST"])
@login_required
def create():

    finding = service.create(
        title=request.form.get("title"),
        description=request.form.get("description"),
        severity=request.form.get("severity"),
        category=request.form.get("category"),
        recommendation=request.form.get("recommendation"),
        evidence=request.form.get("evidence"),
        cvss=float(request.form.get("cvss", 0)),
        project_id=request.form.get("project_id", type=int),
        asset_id=request.form.get("asset_id", type=int),
        scan_id=request.form.get("scan_id", type=int),
        status="Open",
    )

    flash("Finding created successfully.", "success")

    return redirect(url_for("findings.details", finding_id=finding.id))


# =====================================================
# UPDATE
# =====================================================


@bp.route("/<int:finding_id>/update", methods=["POST"])
@login_required
def update(finding_id):

    service.update(
        finding_id,
        title=request.form.get("title"),
        description=request.form.get("description"),
        severity=request.form.get("severity"),
        category=request.form.get("category"),
        recommendation=request.form.get("recommendation"),
        evidence=request.form.get("evidence"),
        cvss=float(request.form.get("cvss", 0)),
    )

    flash("Finding updated successfully.", "success")

    return redirect(url_for("findings.details", finding_id=finding_id))


# =====================================================
# DELETE
# =====================================================


@bp.route("/<int:finding_id>/delete", methods=["POST"])
@login_required
def delete(finding_id):

    service.delete(finding_id)

    flash("Finding deleted successfully.", "success")

    return redirect(url_for("findings.findings"))


# =====================================================
# RESOLVE
# =====================================================


@bp.route("/<int:finding_id>/resolve", methods=["POST"])
@login_required
def resolve(finding_id):

    service.resolve(finding_id)

    flash("Finding resolved.", "success")

    return redirect(url_for("findings.details", finding_id=finding_id))


# =====================================================
# REOPEN
# =====================================================


@bp.route("/<int:finding_id>/reopen", methods=["POST"])
@login_required
def reopen(finding_id):

    service.reopen(finding_id)

    flash("Finding reopened.", "warning")

    return redirect(url_for("findings.details", finding_id=finding_id))


# =====================================================
# FALSE POSITIVE
# =====================================================


@bp.route("/<int:finding_id>/false-positive", methods=["POST"])
@login_required
def false_positive(finding_id):

    service.mark_false_positive(finding_id)

    flash("Marked as false positive.", "info")

    return redirect(url_for("findings.details", finding_id=finding_id))


# =====================================================
# BULK RESOLVE
# =====================================================


@bp.route("/bulk/resolve", methods=["POST"])
@login_required
def bulk_resolve():

    ids = request.form.getlist("ids", type=int)

    count = service.bulk_resolve(ids)

    flash(f"{count} findings resolved.", "success")

    return redirect(url_for("findings.findings"))


# =====================================================
# BULK DELETE
# =====================================================


@bp.route("/bulk/delete", methods=["POST"])
@login_required
def bulk_delete():

    ids = request.form.getlist("ids", type=int)

    count = service.bulk_delete(ids)

    flash(f"{count} findings deleted.", "success")

    return redirect(url_for("findings.findings"))


# =====================================================
# BULK FALSE POSITIVE
# =====================================================


@bp.route("/bulk/false-positive", methods=["POST"])
@login_required
def bulk_false_positive():

    ids = request.form.getlist("ids", type=int)

    count = service.bulk_false_positive(ids)

    flash(f"{count} findings marked as false positive.", "info")

    return redirect(url_for("findings.findings"))


# =====================================================
# BULK SEVERITY
# =====================================================


@bp.route("/bulk/severity", methods=["POST"])
@login_required
def bulk_severity():

    ids = request.form.getlist("ids", type=int)

    severity = request.form.get("severity")

    count = service.bulk_change_severity(ids, severity)

    flash(f"{count} findings updated.", "success")

    return redirect(url_for("findings.findings"))


# =====================================================
# SEARCH
# =====================================================


@bp.route("/search")
@login_required
def search():

    keyword = request.args.get("q", "")

    findings = service.search(keyword)

    return render_template("findings/list.html", findings=findings, keyword=keyword)


# =====================================================
# FILTERS
# =====================================================


@bp.route("/filter")
@login_required
def filter_findings():

    query = filters.apply(request.args)

    findings = query.all()

    return render_template(
        "findings/list.html", findings=findings, filters=request.args
    )


# =====================================================
# FILTER API
# =====================================================


@bp.route("/api/filter")
@login_required
def api_filter():

    query = filters.apply(request.args)

    findings = query.all()

    return jsonify(exporter.serialize_many(findings))


# =====================================================
# DASHBOARD API
# =====================================================


@bp.route("/api/dashboard")
@login_required
def api_dashboard():

    return jsonify(statistics.dashboard())


# =====================================================
# SUMMARY API
# =====================================================


@bp.route("/api/summary")
@login_required
def api_summary():

    return jsonify(statistics.summary())


# =====================================================
# SEVERITY API
# =====================================================


@bp.route("/api/severity")
@login_required
def api_severity():

    return jsonify(statistics.severity())


# =====================================================
# STATUS API
# =====================================================


@bp.route("/api/status")
@login_required
def api_status():

    return jsonify(statistics.status())


# =====================================================
# CATEGORY API
# =====================================================


@bp.route("/api/categories")
@login_required
def api_categories():

    return jsonify(statistics.categories())


# =====================================================
# RISK SCORE API
# =====================================================


@bp.route("/api/risk-score")
@login_required
def api_risk_score():

    return jsonify({"risk_score": statistics.risk_score()})


# =====================================================
# CVSS API
# =====================================================


@bp.route("/api/cvss")
@login_required
def api_cvss():

    return jsonify(
        {"average": statistics.average_cvss(), "maximum": statistics.max_cvss()}
    )


# =====================================================
# TOP ASSETS API
# =====================================================


@bp.route("/api/top-assets")
@login_required
def api_top_assets():

    return jsonify(statistics.top_assets())


# =====================================================
# TOP PROJECTS API
# =====================================================


@bp.route("/api/top-projects")
@login_required
def api_top_projects():

    return jsonify(statistics.top_projects())


# =====================================================
# TIMELINE API
# =====================================================


@bp.route("/api/timeline")
@login_required
def api_timeline():

    return jsonify(statistics.by_date())


# =====================================================
# MONTHLY API
# =====================================================


@bp.route("/api/monthly")
@login_required
def api_monthly():

    return jsonify(statistics.monthly())


# =====================================================
# MTTR API
# =====================================================


@bp.route("/api/mttr")
@login_required
def api_mttr():

    return jsonify({"mttr": statistics.mttr()})


# =====================================================
# EXECUTIVE SUMMARY API
# =====================================================


@bp.route("/api/executive")
@login_required
def api_executive():

    return jsonify(statistics.executive_summary())


from flask import Response

# =====================================================
# EXPORT CSV
# =====================================================


@bp.route("/export/csv")
@login_required
def export_csv():

    findings = filters.apply(request.args).all()

    csv_data = exporter.export_csv(findings)

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=findings.csv"},
    )


# =====================================================
# EXPORT JSON
# =====================================================


@bp.route("/export/json")
@login_required
def export_json():

    findings = filters.apply(request.args).all()

    return Response(
        exporter.export_json(findings),
        mimetype="application/json",
        headers={"Content-Disposition": "attachment; filename=findings.json"},
    )


# =====================================================
# EXECUTIVE REPORT
# =====================================================


@bp.route("/report/executive")
@login_required
def executive_report():

    findings = filters.apply(request.args).all()

    return jsonify(exporter.executive_report(findings))


# =====================================================
# TECHNICAL REPORT
# =====================================================


@bp.route("/report/technical")
@login_required
def technical_report():

    findings = filters.apply(request.args).all()

    return jsonify(exporter.technical_report(findings))


# =====================================================
# PROJECT REPORT
# =====================================================


@bp.route("/project/<int:project_id>/report")
@login_required
def project_report(project_id):

    findings = service.by_project(project_id)

    return jsonify(exporter.project_report(project_id, findings))


# =====================================================
# ASSET REPORT
# =====================================================


@bp.route("/asset/<int:asset_id>/report")
@login_required
def asset_report(asset_id):

    findings = service.by_asset(asset_id)

    return jsonify(exporter.asset_report(asset_id, findings))


# =====================================================
# SCAN REPORT
# =====================================================


@bp.route("/scan/<int:scan_id>/report")
@login_required
def scan_report(scan_id):

    findings = service.by_scan(scan_id)

    return jsonify(exporter.scan_report(scan_id, findings))


# =====================================================
# PDF REPORT
# =====================================================


@bp.route("/report/pdf")
@login_required
def pdf_report():

    findings = filters.apply(request.args).all()

    data = exporter.executive_report(findings)

    # Replace this with your existing
    # ReportLab PDF generator

    return jsonify({"message": "Connect ReportLab generator here.", "report": data})
