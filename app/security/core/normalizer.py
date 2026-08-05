"""
CloudShield Enterprise
Enterprise Result Parser
"""

import json


class ResultParser:
    """
    Standardize scanner output for the
    entire CloudShield platform.
    """

    def parse(self, tool, target, result, execution_time=0):

        if result is None:

            result = {}

        summary = self.summary(result, execution_time)

        return {
            "success": result.get("success", False),
            "tool": tool,
            "target": target,
            "summary": summary,
            # -----------------------------
            # Website
            # -----------------------------
            "website": result.get("website", {}),
            # -----------------------------
            # Security Headers
            # -----------------------------
            "headers": result.get("headers", []),
            # -----------------------------
            # SSL
            # -----------------------------
            "ssl": result.get("ssl", {}),
            # -----------------------------
            # DNS
            # -----------------------------
            "dns": result.get("dns", {}),
            # -----------------------------
            # WHOIS
            # -----------------------------
            "whois": result.get("whois", {}),
            # -----------------------------
            # Technology Detection
            # -----------------------------
            "technology": result.get("technology", []),
            # -----------------------------
            # Open Ports
            # -----------------------------
            "ports": result.get("ports", []),
            # -----------------------------
            # Findings
            # -----------------------------
            "findings": self.findings(result),
            # -----------------------------
            # Raw Output
            # -----------------------------
            "raw_output": result,
            # -----------------------------
            # Metadata
            # -----------------------------
            "command": result.get("command", ""),
            "return_code": result.get("return_code", 0),
            "execution_time": execution_time,
            "error": result.get("stderr", result.get("error", "")),
        }

    def summary(self, result, execution_time):

        return {
            "status": "Completed" if result.get("success") else "Failed",
            "message": (
                "Scan completed successfully."
                if result.get("success")
                else result.get("error", result.get("stderr", "Unknown error"))
            ),
            "score": result.get("score", 0),
            "risk": result.get("risk", "Unknown"),
            "execution_time": execution_time,
            "return_code": result.get("return_code", 0),
        }

    def findings(self, result):

        if isinstance(result.get("findings"), list):

            return result["findings"]

        findings = []

        output = str(result.get("stdout", ""))

        for line in output.splitlines():

            line = line.strip()

            if line:

                findings.append(line)

        return findings

    def json(self, value):

        try:

            return json.loads(value)

        except Exception:

            return {}
