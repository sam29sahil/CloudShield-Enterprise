"""
CloudShield Enterprise
Findings Routes
"""

<<<<<<< HEAD
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
=======
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

from flask_login import login_required

from app.findings import (
    FindingService,
    FindingStatistics,
    FindingFilters,
<<<<<<< HEAD
    FindingExporter,
)

bp = Blueprint("findings", __name__, url_prefix="/findings")
=======
    FindingExporter
)

bp = Blueprint(

    "findings",

    __name__,

    url_prefix="/findings"

)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

service = FindingService()

statistics = FindingStatistics()

filters = FindingFilters()

exporter = FindingExporter()


# =====================================================
# DASHBOARD
# =====================================================

<<<<<<< HEAD

@bp.route("/")
=======
@bp.route("/")

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@login_required
def dashboard():

    data = statistics.dashboard()

    recent = service.latest(10)

<<<<<<< HEAD
    return render_template("findings/dashboard.html", dashboard=data, recent=recent)
=======
    return render_template(

        "findings/dashboard.html",

        dashboard=data,

        recent=recent

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# FINDINGS LIST
# =====================================================

<<<<<<< HEAD

@bp.route("/list")
@login_required
def findings():

    page = request.args.get("page", 1, type=int)

    query = filters.apply(request.args)

    pagination = query.paginate(page=page, per_page=20)

    return render_template(
        "findings/list.html", pagination=pagination, findings=pagination.items
=======
@bp.route("/list")

@login_required
def findings():

    page = request.args.get(

        "page",

        1,

        type=int

    )

    query = filters.apply(request.args)

    pagination = query.paginate(

        page=page,

        per_page=20

    )

    return render_template(

        "findings/list.html",

        pagination=pagination,

        findings=pagination.items

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# =====================================================
# DETAILS
# =====================================================

<<<<<<< HEAD

@bp.route("/<int:finding_id>")
@login_required
def details(finding_id):

    finding = service.get(finding_id)

    return render_template("findings/details.html", finding=finding)


=======
@bp.route("/<int:finding_id>")

@login_required
def details(finding_id):

    finding = service.get(

        finding_id

    )

    return render_template(

        "findings/details.html",

        finding=finding

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# =====================================================
# CREATE
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/create", methods=["POST"])
@login_required
def create():

    finding = service.create(
<<<<<<< HEAD
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
=======

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

        status="Open"

    )

    flash(

        "Finding created successfully.",

        "success"

    )

    return redirect(

        url_for(

            "findings.details",

            finding_id=finding.id

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# UPDATE
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/<int:finding_id>/update", methods=["POST"])
@login_required
def update(finding_id):

    service.update(
<<<<<<< HEAD
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
=======

        finding_id,

        title=request.form.get("title"),

        description=request.form.get("description"),

        severity=request.form.get("severity"),

        category=request.form.get("category"),

        recommendation=request.form.get("recommendation"),

        evidence=request.form.get("evidence"),

        cvss=float(request.form.get("cvss", 0))

    )

    flash(

        "Finding updated successfully.",

        "success"

    )

    return redirect(

        url_for(

            "findings.details",

            finding_id=finding_id

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# DELETE
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/<int:finding_id>/delete", methods=["POST"])
@login_required
def delete(finding_id):

<<<<<<< HEAD
    service.delete(finding_id)

    flash("Finding deleted successfully.", "success")

    return redirect(url_for("findings.findings"))
=======
    service.delete(

        finding_id

    )

    flash(

        "Finding deleted successfully.",

        "success"

    )

    return redirect(

        url_for(

            "findings.findings"

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# RESOLVE
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/<int:finding_id>/resolve", methods=["POST"])
@login_required
def resolve(finding_id):

<<<<<<< HEAD
    service.resolve(finding_id)

    flash("Finding resolved.", "success")

    return redirect(url_for("findings.details", finding_id=finding_id))
=======
    service.resolve(

        finding_id

    )

    flash(

        "Finding resolved.",

        "success"

    )

    return redirect(

        url_for(

            "findings.details",

            finding_id=finding_id

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# REOPEN
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/<int:finding_id>/reopen", methods=["POST"])
@login_required
def reopen(finding_id):

<<<<<<< HEAD
    service.reopen(finding_id)

    flash("Finding reopened.", "warning")

    return redirect(url_for("findings.details", finding_id=finding_id))
=======
    service.reopen(

        finding_id

    )

    flash(

        "Finding reopened.",

        "warning"

    )

    return redirect(

        url_for(

            "findings.details",

            finding_id=finding_id

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# FALSE POSITIVE
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/<int:finding_id>/false-positive", methods=["POST"])
@login_required
def false_positive(finding_id):

<<<<<<< HEAD
    service.mark_false_positive(finding_id)

    flash("Marked as false positive.", "info")

    return redirect(url_for("findings.details", finding_id=finding_id))


=======
    service.mark_false_positive(

        finding_id

    )

    flash(

        "Marked as false positive.",

        "info"

    )

    return redirect(

        url_for(

            "findings.details",

            finding_id=finding_id

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# =====================================================
# BULK RESOLVE
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/bulk/resolve", methods=["POST"])
@login_required
def bulk_resolve():

    ids = request.form.getlist("ids", type=int)

    count = service.bulk_resolve(ids)

<<<<<<< HEAD
    flash(f"{count} findings resolved.", "success")

    return redirect(url_for("findings.findings"))
=======
    flash(

        f"{count} findings resolved.",

        "success"

    )

    return redirect(

        url_for("findings.findings")

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# BULK DELETE
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/bulk/delete", methods=["POST"])
@login_required
def bulk_delete():

    ids = request.form.getlist("ids", type=int)

    count = service.bulk_delete(ids)

<<<<<<< HEAD
    flash(f"{count} findings deleted.", "success")

    return redirect(url_for("findings.findings"))
=======
    flash(

        f"{count} findings deleted.",

        "success"

    )

    return redirect(

        url_for("findings.findings")

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# BULK FALSE POSITIVE
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/bulk/false-positive", methods=["POST"])
@login_required
def bulk_false_positive():

    ids = request.form.getlist("ids", type=int)

    count = service.bulk_false_positive(ids)

<<<<<<< HEAD
    flash(f"{count} findings marked as false positive.", "info")

    return redirect(url_for("findings.findings"))
=======
    flash(

        f"{count} findings marked as false positive.",

        "info"

    )

    return redirect(

        url_for("findings.findings")

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# BULK SEVERITY
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/bulk/severity", methods=["POST"])
@login_required
def bulk_severity():

    ids = request.form.getlist("ids", type=int)

    severity = request.form.get("severity")

<<<<<<< HEAD
    count = service.bulk_change_severity(ids, severity)

    flash(f"{count} findings updated.", "success")

    return redirect(url_for("findings.findings"))
=======
    count = service.bulk_change_severity(

        ids,

        severity

    )

    flash(

        f"{count} findings updated.",

        "success"

    )

    return redirect(

        url_for("findings.findings")

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# SEARCH
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/search")
@login_required
def search():

<<<<<<< HEAD
    keyword = request.args.get("q", "")

    findings = service.search(keyword)

    return render_template("findings/list.html", findings=findings, keyword=keyword)
=======
    keyword = request.args.get(

        "q",

        ""

    )

    findings = service.search(

        keyword

    )

    return render_template(

        "findings/list.html",

        findings=findings,

        keyword=keyword

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# FILTERS
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/filter")
@login_required
def filter_findings():

<<<<<<< HEAD
    query = filters.apply(request.args)
=======
    query = filters.apply(

        request.args

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    findings = query.all()

    return render_template(
<<<<<<< HEAD
        "findings/list.html", findings=findings, filters=request.args
=======

        "findings/list.html",

        findings=findings,

        filters=request.args

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# =====================================================
# FILTER API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/filter")
@login_required
def api_filter():

<<<<<<< HEAD
    query = filters.apply(request.args)

    findings = query.all()

    return jsonify(exporter.serialize_many(findings))


=======
    query = filters.apply(

        request.args

    )

    findings = query.all()

    return jsonify(

        exporter.serialize_many(

            findings

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
# =====================================================
# DASHBOARD API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/dashboard")
@login_required
def api_dashboard():

<<<<<<< HEAD
    return jsonify(statistics.dashboard())
=======
    return jsonify(

        statistics.dashboard()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# SUMMARY API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/summary")
@login_required
def api_summary():

<<<<<<< HEAD
    return jsonify(statistics.summary())
=======
    return jsonify(

        statistics.summary()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# SEVERITY API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/severity")
@login_required
def api_severity():

<<<<<<< HEAD
    return jsonify(statistics.severity())
=======
    return jsonify(

        statistics.severity()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# STATUS API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/status")
@login_required
def api_status():

<<<<<<< HEAD
    return jsonify(statistics.status())
=======
    return jsonify(

        statistics.status()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# CATEGORY API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/categories")
@login_required
def api_categories():

<<<<<<< HEAD
    return jsonify(statistics.categories())
=======
    return jsonify(

        statistics.categories()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# RISK SCORE API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/risk-score")
@login_required
def api_risk_score():

<<<<<<< HEAD
    return jsonify({"risk_score": statistics.risk_score()})
=======
    return jsonify({

        "risk_score":

        statistics.risk_score()

    })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# CVSS API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/cvss")
@login_required
def api_cvss():

<<<<<<< HEAD
    return jsonify(
        {"average": statistics.average_cvss(), "maximum": statistics.max_cvss()}
    )
=======
    return jsonify({

        "average":

        statistics.average_cvss(),

        "maximum":

        statistics.max_cvss()

    })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# TOP ASSETS API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/top-assets")
@login_required
def api_top_assets():

<<<<<<< HEAD
    return jsonify(statistics.top_assets())
=======
    return jsonify(

        statistics.top_assets()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# TOP PROJECTS API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/top-projects")
@login_required
def api_top_projects():

<<<<<<< HEAD
    return jsonify(statistics.top_projects())
=======
    return jsonify(

        statistics.top_projects()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# TIMELINE API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/timeline")
@login_required
def api_timeline():

<<<<<<< HEAD
    return jsonify(statistics.by_date())
=======
    return jsonify(

        statistics.by_date()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# MONTHLY API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/monthly")
@login_required
def api_monthly():

<<<<<<< HEAD
    return jsonify(statistics.monthly())
=======
    return jsonify(

        statistics.monthly()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# MTTR API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/mttr")
@login_required
def api_mttr():

<<<<<<< HEAD
    return jsonify({"mttr": statistics.mttr()})
=======
    return jsonify({

        "mttr":

        statistics.mttr()

    })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# EXECUTIVE SUMMARY API
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/api/executive")
@login_required
def api_executive():

<<<<<<< HEAD
    return jsonify(statistics.executive_summary())

=======
    return jsonify(

        statistics.executive_summary()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

from flask import Response

# =====================================================
# EXPORT CSV
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/export/csv")
@login_required
def export_csv():

    findings = filters.apply(request.args).all()

    csv_data = exporter.export_csv(findings)

    return Response(
<<<<<<< HEAD
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=findings.csv"},
=======

        csv_data,

        mimetype="text/csv",

        headers={

            "Content-Disposition":
            "attachment; filename=findings.csv"

        }

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# =====================================================
# EXPORT JSON
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/export/json")
@login_required
def export_json():

    findings = filters.apply(request.args).all()

    return Response(
<<<<<<< HEAD
        exporter.export_json(findings),
        mimetype="application/json",
        headers={"Content-Disposition": "attachment; filename=findings.json"},
=======

        exporter.export_json(findings),

        mimetype="application/json",

        headers={

            "Content-Disposition":
            "attachment; filename=findings.json"

        }

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )


# =====================================================
# EXECUTIVE REPORT
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/report/executive")
@login_required
def executive_report():

    findings = filters.apply(request.args).all()

<<<<<<< HEAD
    return jsonify(exporter.executive_report(findings))
=======
    return jsonify(

        exporter.executive_report(

            findings

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# TECHNICAL REPORT
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/report/technical")
@login_required
def technical_report():

    findings = filters.apply(request.args).all()

<<<<<<< HEAD
    return jsonify(exporter.technical_report(findings))
=======
    return jsonify(

        exporter.technical_report(

            findings

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# PROJECT REPORT
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/project/<int:project_id>/report")
@login_required
def project_report(project_id):

<<<<<<< HEAD
    findings = service.by_project(project_id)

    return jsonify(exporter.project_report(project_id, findings))
=======
    findings = service.by_project(

        project_id

    )

    return jsonify(

        exporter.project_report(

            project_id,

            findings

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# ASSET REPORT
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/asset/<int:asset_id>/report")
@login_required
def asset_report(asset_id):

<<<<<<< HEAD
    findings = service.by_asset(asset_id)

    return jsonify(exporter.asset_report(asset_id, findings))
=======
    findings = service.by_asset(

        asset_id

    )

    return jsonify(

        exporter.asset_report(

            asset_id,

            findings

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# SCAN REPORT
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/scan/<int:scan_id>/report")
@login_required
def scan_report(scan_id):

<<<<<<< HEAD
    findings = service.by_scan(scan_id)

    return jsonify(exporter.scan_report(scan_id, findings))
=======
    findings = service.by_scan(

        scan_id

    )

    return jsonify(

        exporter.scan_report(

            scan_id,

            findings

        )

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


# =====================================================
# PDF REPORT
# =====================================================

<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@bp.route("/report/pdf")
@login_required
def pdf_report():

<<<<<<< HEAD
    findings = filters.apply(request.args).all()

    data = exporter.executive_report(findings)
=======
    findings = filters.apply(

        request.args

    ).all()

    data = exporter.executive_report(

        findings

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # Replace this with your existing
    # ReportLab PDF generator

<<<<<<< HEAD
    return jsonify({"message": "Connect ReportLab generator here.", "report": data})
=======
    return jsonify({

        "message":

        "Connect ReportLab generator here.",

        "report":

        data

    })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
