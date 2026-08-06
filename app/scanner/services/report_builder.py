"""
CloudShield Enterprise
Enterprise Report Builder
"""

import json


class ReportBuilder:

    def __init__(self, scan):

        self.scan = scan

        try:

            self.data = json.loads(scan.parsed_output) if scan.parsed_output else {}

        except Exception:

            self.data = {}

    # ----------------------------------------------------

    def build(self):

        return {
            "summary": self.summary(),
            "website": self.website(),
            "headers": self.headers(),
            "ssl": self.ssl(),
            "dns": self.dns(),
            "whois": self.whois(),
            "technology": self.technology(),
            "ports": self.ports(),
            "findings": self.findings(),
            "recommendations": self.recommendations(),
            "raw": self.raw(),
        }

    # ----------------------------------------------------

    def summary(self):

        return {
            "target": self.scan.target,
            "tool": self.scan.tool,
            "category": self.scan.category,
            "status": self.scan.status,
            "score": self.scan.score,
            "risk": self.scan.risk,
            "duration": self.scan.duration,
            "started": self.scan.started_at,
            "completed": self.scan.completed_at,
        }

    # ----------------------------------------------------

    def website(self):

        return self.data.get("website", {})

    # ----------------------------------------------------

    def headers(self):

        headers = self.data.get("headers", {})

        if isinstance(headers, dict):

            return headers.get("analysis", [])

        return headers

    # ----------------------------------------------------

    def ssl(self):

        return self.data.get("ssl", {})

    # ----------------------------------------------------

    def dns(self):

        return self.data.get("dns", {})

    # ----------------------------------------------------

    def whois(self):

        return self.data.get("whois", {})

    # ----------------------------------------------------

    def technology(self):

        tech = self.data.get("technology", {})

        if isinstance(tech, dict):

            return tech.get("technologies", [])

        return tech

    # ----------------------------------------------------

    def ports(self):

        ports = self.data.get("ports", [])

        if ports is None:

            return []

        return ports

    # ----------------------------------------------------

    def findings(self):

        items = []

        if not hasattr(self.scan, "findings"):

            return items

        for finding in self.scan.findings:

            items.append(
                {
                    "id": getattr(finding, "id", None),
                    "title": getattr(finding, "title", ""),
                    "severity": getattr(finding, "severity", ""),
                    "description": getattr(finding, "description", ""),
                    "recommendation": getattr(finding, "recommendation", ""),
                    "evidence": getattr(finding, "evidence", ""),
                    "cvss": getattr(finding, "cvss", ""),
                    "cwe": getattr(finding, "cwe", ""),
                    "owasp": getattr(finding, "owasp", ""),
                    "reference": getattr(finding, "reference", ""),
                    "status": getattr(finding, "status", ""),
                    "asset_id": getattr(finding, "asset", ""),
                    "scan_id": getattr(finding, "scan", ""),
                }
            )

        return items

    # ----------------------------------------------------

    def recommendations(self):

        items = []

        if not hasattr(self.scan, "findings"):

            return items

        for finding in self.scan.findings:

            items.append(
                {
                    "title": getattr(finding, "title", ""),
                    "severity": getattr(finding, "severity", ""),
                    "recommendation": getattr(finding, "recommendation", ""),
                    "evidence": getattr(finding, "evidence", ""),
                    "reference": getattr(finding, "reference", ""),
                }
            )

        return items

    # ----------------------------------------------------

    def raw(self):

        return self.data
