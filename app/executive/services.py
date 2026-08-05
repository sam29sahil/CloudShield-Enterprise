"""
CloudShield Enterprise
Executive Dashboard Services
"""

<<<<<<< HEAD
from app.models import Asset, Finding, SecurityScan
=======
from app.models import (

    Asset,

    Finding,

    SecurityScan

)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


class ExecutiveService:

    def summary(self):

        scans = SecurityScan.query.count()

        findings = Finding.query.count()

        assets = Asset.query.count()

        score = 100

        if findings:

<<<<<<< HEAD
            score = max(0, 100 - findings * 5)

        return {"assets": assets, "scans": scans, "findings": findings, "score": score}

    def top_risks(self):

        return Finding.query.order_by(Finding.severity.desc()).limit(5).all()
=======
            score = max(

                0,

                100 - findings * 5

            )

        return {

            "assets": assets,

            "scans": scans,

            "findings": findings,

            "score": score

        }

    def top_risks(self):

        return (

            Finding.query

            .order_by(

                Finding.severity.desc()

            )

            .limit(5)

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def recommendations(self):

        return [
<<<<<<< HEAD
            "Enable Multi-Factor Authentication",
            "Patch Critical Vulnerabilities",
            "Close Unused Ports",
            "Enable Security Headers",
            "Review Firewall Rules",
=======

            "Enable Multi-Factor Authentication",

            "Patch Critical Vulnerabilities",

            "Close Unused Ports",

            "Enable Security Headers",

            "Review Firewall Rules"

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        ]

    def compliance(self):

<<<<<<< HEAD
        return {"OWASP": 82, "CIS": 79, "NIST": 75}
=======
        return {

            "OWASP": 82,

            "CIS": 79,

            "NIST": 75

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
