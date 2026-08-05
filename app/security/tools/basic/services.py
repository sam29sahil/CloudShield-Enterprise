"""
CloudShield Enterprise
Quick Scan Service
"""
<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
import traceback
from datetime import datetime
import json

from app.extensions import db
from app.models import SecurityScan, Report
from app.assets.services import AssetManager
from app.notifications.services import NotificationService

from app.security.tools.basic.website import website_scan
from app.security.tools.basic.headers import scan_headers
from app.security.tools.basic.ssl_scanner import get_ssl_info
from app.security.tools.basic.dns import dns_scan
from app.security.tools.basic.whois import whois_scan
from app.security.tools.basic.ports import port_scan
from app.security.tools.basic.technology import detect_technology
from app.security.tools.basic.risk import calculate_risk

<<<<<<< HEAD

class BasicSecurityService:

    def execute(self, user_id, asset_id, category, tool, target, arguments=None):
=======
class BasicSecurityService:

    def execute(
        self,
        user_id,
        asset_id,
        category,
        tool,
        target,
        arguments=None
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        print("\n========== BasicSecurityService Started ==========\n")

        started = datetime.utcnow()

<<<<<<< HEAD
        host = target.replace("https://", "").replace("http://", "").split("/")[0]
=======
        host = (
            target.replace("https://", "")
                  .replace("http://", "")
                  .split("/")[0]
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        report = {}

        # -------------------------------------------------
        # Website
        # -------------------------------------------------

        print("Running Website Scan...")

        website = website_scan(target)

        if not website.get("success"):

            print("Website Scan Failed")
            print(website)

<<<<<<< HEAD
            return {"scan": None, "result": website}
=======
            return {

                "scan": None,

                "result": website

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        report["website"] = website

        # -------------------------------------------------
        # Headers
        # -------------------------------------------------

        print("Running Header Analysis...")

        report["headers"] = scan_headers(target)

        # -------------------------------------------------
        # Technology
        # -------------------------------------------------

        print("Running Technology Detection...")

<<<<<<< HEAD
        report["technology"] = detect_technology(website["headers"], website["html"])
=======
        report["technology"] = detect_technology(

            website["headers"],

            website["html"]

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # -------------------------------------------------
        # DNS
        # -------------------------------------------------

        print("Running DNS Scan...")

        report["dns"] = dns_scan(host)

        # -------------------------------------------------
        # WHOIS
        # -------------------------------------------------

        print("Running WHOIS Scan...")

        report["whois"] = whois_scan(host)

        # -------------------------------------------------
        # SSL
        # -------------------------------------------------

        print("Running SSL Scan...")

        report["ssl"] = get_ssl_info(host)

        # -------------------------------------------------
        # Port Scan
        # -------------------------------------------------

        print("Running Port Scan...")

        report["ports"] = port_scan(host)

        # --------------------------
        # Risk Calculation
<<<<<<< HEAD
        # --------------------------
=======
         # --------------------------
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        risk = calculate_risk(report)

        report["score"] = risk["score"]
        report["risk"] = risk["risk"]
        report["findings"] = "\n".join(risk["findings"])

        completed = datetime.utcnow()

<<<<<<< HEAD
        duration = (completed - started).total_seconds()

        scan = SecurityScan(
            user_id=user_id,
            asset_id=asset_id,
            category=category,
            tool="quick_scan",
            target=target,
            arguments=" ".join(arguments) if arguments else "",
            status="Completed",
            score=report["score"],
            risk=report["risk"],
            raw_output=json.dumps(report, indent=4, default=str),
            parsed_output=json.dumps(report, indent=4, default=str),
            started_at=started,
            completed_at=completed,
            duration=duration,
=======
        duration = (

            completed - started

        ).total_seconds()

        scan = SecurityScan(

            user_id=user_id,
            
            asset_id=asset_id,

            category=category,

            tool="quick_scan",

            target=target,

            arguments=" ".join(arguments) if arguments else "",

            status="Completed",

            score=report["score"],

            risk=report["risk"],

            raw_output=json.dumps(report, indent=4, default=str),

            parsed_output=json.dumps(report, indent=4, default=str),

            started_at=started,

            completed_at=completed,

            duration=duration

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        db.session.add(scan)

        db.session.commit()

        # --------------------------
        # Generate Finding
        # --------------------------

        from app.findings.generator import FindingGenerator

        try:

<<<<<<< HEAD
            findings = FindingGenerator.generate(scan, report)
=======
            findings = FindingGenerator.generate(

                scan,

                report
            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            print("=" * 60)
            print("FINDINGS CREATED:", findings)
            print("=" * 60)
<<<<<<< HEAD

=======
          
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        except Exception as e:

            print("=" * 60)
            print("FINDING GENERATOR ERROR")
            traceback.print_exc()
            print("=" * 60)

        # --------------------------
        # Update Asset
        # --------------------------
        if asset_id:

            from app.models.finding import Finding

<<<<<<< HEAD
            count = Finding.query.filter_by(asset_id=asset_id).count()

            AssetManager().update_scan(
                asset_id=asset_id,
                score=report["score"],
                risk=report["risk"],
                findings=count,
=======
            count = Finding.query.filter_by(
                asset_id=asset_id
            ).count()

            AssetManager().update_scan(

                asset_id=asset_id,

                score=report["score"],

                risk=report["risk"],

                findings=count

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )

        # --------------------------
        # Create Notification
        # --------------------------

        notification_service = NotificationService()

        if report["risk"] == "Critical":

            title = "🚨 Critical Risk Detected"

            severity = "Critical"

        elif report["risk"] == "High":

            title = "⚠ High Risk Detected"

            severity = "High"

        else:

            title = " Scan Completed"

            severity = "Info"

        notification_service.create(
<<<<<<< HEAD
            user_id=user_id,
            title=title,
            message=(
                f"Target: {target}\n"
                f"Risk: {report['risk']}\n"
                f"Security Score: {report['score']}"
            ),
            severity=severity,
=======

            user_id=user_id,

            title=title,

            message=(

                f"Target: {target}\n"

                f"Risk: {report['risk']}\n"

                f"Security Score: {report['score']}"

            ),

            severity=severity

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        print("\n========== Scan Completed ==========\n")

<<<<<<< HEAD
        return {"scan": scan, "result": report}
=======
        return {

            "scan": scan,

            "result": report

        }

  
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
