
"""
CloudShield Enterprise
CVE Service
"""

from datetime import datetime


class CVEService:
    """
    CVE Intelligence Service
    """

    def __init__(self):

        self.cves = [

            {
                "id": "CVE-2025-10001",
                "title": "Remote Code Execution in Apache HTTP Server",
                "vendor": "Apache",
                "product": "HTTP Server",
                "severity": "Critical",
                "cvss": 9.8,
                "published": "2025-01-15",
                "description": "Remote attacker can execute arbitrary code.",
                "recommendation": "Upgrade Apache to the latest patched version."
            },

            {
                "id": "CVE-2025-10002",
                "title": "SQL Injection in Web Application",
                "vendor": "Generic",
                "product": "Web Application",
                "severity": "High",
                "cvss": 8.6,
                "published": "2025-02-10",
                "description": "SQL Injection vulnerability detected.",
                "recommendation": "Use parameterized queries."
            },

            {
                "id": "CVE-2025-10003",
                "title": "Cross Site Scripting",
                "vendor": "Generic",
                "product": "CMS",
                "severity": "Medium",
                "cvss": 6.3,
                "published": "2025-03-01",
                "description": "Reflected XSS vulnerability.",
                "recommendation": "Sanitize user input."
            }

        ]

    # ----------------------------------------
    # Dashboard Summary
    # ----------------------------------------

    def summary(self):

        critical = len(
            [c for c in self.cves if c["severity"] == "Critical"]
        )

        high = len(
            [c for c in self.cves if c["severity"] == "High"]
        )

        medium = len(
            [c for c in self.cves if c["severity"] == "Medium"]
        )

        low = len(
            [c for c in self.cves if c["severity"] == "Low"]
        )

        return {

            "critical": critical,

            "high": high,

            "medium": medium,

            "low": low,

            "total": len(self.cves)

        }

    # ----------------------------------------
    # Get All CVEs
    # ----------------------------------------

    def all(self):

        return self.cves

    # ----------------------------------------
    # Search
    # ----------------------------------------

    def search(self, keyword):

        keyword = keyword.lower()

        results = []

        for cve in self.cves:

            if (

                keyword in cve["id"].lower()

                or keyword in cve["vendor"].lower()

                or keyword in cve["product"].lower()

                or keyword in cve["title"].lower()

            ):

                results.append(cve)

        return results

    # ----------------------------------------
    # Severity Filter
    # ----------------------------------------

    def by_severity(self, severity):

        return [

            cve

            for cve in self.cves

            if cve["severity"].lower() == severity.lower()

        ]

    # ----------------------------------------
    # Latest CVEs
    # ----------------------------------------

    def latest(self, limit=10):

        return sorted(

            self.cves,

            key=lambda x: datetime.strptime(

                x["published"],

                "%Y-%m-%d"

            ),

            reverse=True

        )[:limit]