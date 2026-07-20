"""
CloudShield Enterprise
Executive Dashboard Services
"""

from app.models import (

    Asset,

    Finding,

    SecurityScan

)


class ExecutiveService:

    def summary(self):

        scans = SecurityScan.query.count()

        findings = Finding.query.count()

        assets = Asset.query.count()

        score = 100

        if findings:

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

    def recommendations(self):

        return [

            "Enable Multi-Factor Authentication",

            "Patch Critical Vulnerabilities",

            "Close Unused Ports",

            "Enable Security Headers",

            "Review Firewall Rules"

        ]

    def compliance(self):

        return {

            "OWASP": 82,

            "CIS": 79,

            "NIST": 75

        }