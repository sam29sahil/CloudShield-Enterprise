"""
CloudShield Enterprise
Security Findings Aggregator
"""

from app.models.finding import Finding

class FindingAggregator:

    def aggregate(self, scan_result):

        findings = []

        # -------------------------------
        # Missing Security Headers
        # -------------------------------

        if "headers" in scan_result:

            for item in scan_result["headers"]["analysis"]:

                if item["status"] == "Missing":

                    findings.append(

                        Finding(

                            title=item["header"],

                            severity=item["severity"],

                            category="HTTP Headers",

                            source="Header Scanner",

                            description=item["description"],

                            recommendation=item["recommendation"],

                            target=scan_result["website"]["url"]

                        )

                    )

        # -------------------------------
        # SSL
        # -------------------------------

        ssl = scan_result.get("ssl")

        if ssl:

            if not ssl.get("valid", True):

                findings.append(

                    Finding(

                        title="Expired SSL Certificate",

                        severity="High",

                        category="SSL",

                        source="SSL Scanner",

                        description="SSL certificate is expired.",

                        recommendation="Renew the SSL certificate.",

                        target=scan_result["website"]["url"]

                    )

                )

        return findings