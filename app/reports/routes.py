"""
CloudShield Enterprise
Reports Routes
"""

from flask import (
    render_template,
    send_file,
    redirect,
    url_for,
    flash
)

from flask_login import login_required

from app.reports import reports
from app.models import SecurityScan
from app.reports.pdf import PDFReport
from app.reports.csv_export import CSVReport
from app.reports.json_export import JSONReport
from app.extensions import db

import tempfile
import os


@reports.route("/")
@login_required
def index():
    """
    Reports Home
    """

    scans = (
        SecurityScan.query
        .order_by(SecurityScan.started_at.desc())
        .all()
    )

    return render_template(
        "reports/index.html",
        scans=scans
    )


@reports.route("/pdf/<int:scan_id>")
@login_required
def pdf(scan_id):

    scan = SecurityScan.query.get_or_404(scan_id)
    
    pdf_buffer = PDFReport().generate(scan)

    
    return send_file(

            pdf_buffer,

            mimetype="application/pdf",

            as_attachment=True,

            download_name=f"CloudShield_Report_{scan.id}.pdf"

    )
    
@reports.route("/csv/<int:scan_id>")
@login_required
def csv(scan_id):

    scan = SecurityScan.query.get_or_404(scan_id)

    tmp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".csv"
    )

    tmp.close()

    CSVReport().generate(scan, tmp.name)

    return send_file(
        tmp.name,
        as_attachment=True,
        download_name=f"CloudShield_Report_{scan.id}.csv",
        mimetype="text/csv"
    )

@reports.route("/json/<int:scan_id>")
@login_required
def json_report(scan_id):

    scan = SecurityScan.query.get_or_404(scan_id)

    tmp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".json"
    )

    tmp.close()

    JSONReport().generate(scan, tmp.name)

    return send_file(
        tmp.name,
        as_attachment=True,
        download_name=f"CloudShield_Report_{scan.id}.json",
        mimetype="application/json"
    )

@reports.route("/<int:scan_id>")
@login_required
def view(scan_id):
    """
    View Report
    """

    scan = SecurityScan.query.get_or_404(scan_id)

    return render_template(
        "reports/report.html",
        scan=scan
    )

@reports.route("/delete/<int:scan_id>")
@login_required
def delete(scan_id):

    from app.models import SecurityScan
    from app.models.finding import Finding
    from app.models.report import Report

    scan = SecurityScan.query.get_or_404(scan_id)

    Finding.query.filter_by(
        scan_id=scan.id
    ).delete()

    Report.query.filter_by(
        scan_id=scan.id
    ).delete()

    db.session.delete(scan)

    db.session.commit()

    flash(
        "Report deleted successfully.",
        "success"
    )

    return redirect(
        url_for("reports.index")
    )

@reports.route("/download/<int:scan_id>")
@login_required
def download(scan_id):
    return redirect(
        url_for(
            "reports.pdf",
            scan_id=scan_id
        )
    )
   