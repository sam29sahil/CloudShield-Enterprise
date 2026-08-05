"""
CloudShield Enterprise
Reports Routes
"""

<<<<<<< HEAD
from flask import render_template, send_file, redirect, url_for, flash
=======
from flask import (
    render_template,
    send_file,
    redirect,
    url_for,
    flash
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

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

<<<<<<< HEAD
    scans = SecurityScan.query.order_by(SecurityScan.started_at.desc()).all()

    return render_template("reports/index.html", scans=scans)
=======
    scans = (
        SecurityScan.query
        .order_by(SecurityScan.started_at.desc())
        .all()
    )

    return render_template(
        "reports/index.html",
        scans=scans
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@reports.route("/pdf/<int:scan_id>")
@login_required
def pdf(scan_id):

    scan = SecurityScan.query.get_or_404(scan_id)
<<<<<<< HEAD

    pdf_buffer = PDFReport().generate(scan)

    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name=f"CloudShield_Report_{scan.id}.pdf",
    )


=======
    
    pdf_buffer = PDFReport().generate(scan)

    
    return send_file(

            pdf_buffer,

            mimetype="application/pdf",

            as_attachment=True,

            download_name=f"CloudShield_Report_{scan.id}.pdf"

    )
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@reports.route("/csv/<int:scan_id>")
@login_required
def csv(scan_id):

    scan = SecurityScan.query.get_or_404(scan_id)

<<<<<<< HEAD
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
=======
    tmp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".csv"
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    tmp.close()

    CSVReport().generate(scan, tmp.name)

    return send_file(
        tmp.name,
        as_attachment=True,
        download_name=f"CloudShield_Report_{scan.id}.csv",
<<<<<<< HEAD
        mimetype="text/csv",
    )


=======
        mimetype="text/csv"
    )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@reports.route("/json/<int:scan_id>")
@login_required
def json_report(scan_id):

    scan = SecurityScan.query.get_or_404(scan_id)

<<<<<<< HEAD
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
=======
    tmp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".json"
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    tmp.close()

    JSONReport().generate(scan, tmp.name)

    return send_file(
        tmp.name,
        as_attachment=True,
        download_name=f"CloudShield_Report_{scan.id}.json",
<<<<<<< HEAD
        mimetype="application/json",
    )


=======
        mimetype="application/json"
    )

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
@reports.route("/<int:scan_id>")
@login_required
def view(scan_id):
    """
    View Report
    """

    scan = SecurityScan.query.get_or_404(scan_id)

<<<<<<< HEAD
    return render_template("reports/report.html", scan=scan)

=======
    return render_template(
        "reports/report.html",
        scan=scan
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@reports.route("/delete/<int:scan_id>")
@login_required
def delete(scan_id):

    from app.models import SecurityScan
    from app.models.finding import Finding
    from app.models.report import Report

    scan = SecurityScan.query.get_or_404(scan_id)

<<<<<<< HEAD
    Finding.query.filter_by(scan_id=scan.id).delete()

    Report.query.filter_by(scan_id=scan.id).delete()
=======
    Finding.query.filter_by(
        scan_id=scan.id
    ).delete()

    Report.query.filter_by(
        scan_id=scan.id
    ).delete()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    db.session.delete(scan)

    db.session.commit()

<<<<<<< HEAD
    flash("Report deleted successfully.", "success")

    return redirect(url_for("reports.index"))

=======
    flash(
        "Report deleted successfully.",
        "success"
    )

    return redirect(
        url_for("reports.index")
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@reports.route("/download/<int:scan_id>")
@login_required
def download(scan_id):
<<<<<<< HEAD
    return redirect(url_for("reports.pdf", scan_id=scan_id))
=======
    return redirect(
        url_for(
            "reports.pdf",
            scan_id=scan_id
        )
    )
   
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
