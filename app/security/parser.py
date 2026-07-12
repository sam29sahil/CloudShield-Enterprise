"""
CloudShield Enterprise
Security Result Parser
"""

import json


class ResultParser:
    """
    Standardize tool output.
    """

    def parse(
        self,
        tool,
        target,
        result,
        execution_time=0
    ):

        return {
            "success": result.get("success", False),
            "tool": tool,
            "target": target,
            "summary": self.summary(result),
            "findings": self.findings(result),
            "raw_output": result.get("stdout", ""),
            "error": result.get(
                "stderr",
                result.get("error", "")
            ),
            "command": result.get("command", ""),
            "return_code": result.get("return_code", -1),
            "execution_time": execution_time
        }

    def summary(self, result):

        if result.get("success"):
            return {
                "status": "Completed",
                "message": "Scan completed successfully.",
                "return_code": result.get("return_code", 0)
            }

        return {
            "status": "Failed",
            "message": result.get(
                "error",
                result.get("stderr", "Unknown error")
            ),
            "return_code": result.get("return_code", -1)
        }

    def findings(self, result):

        findings = []

        output = result.get("stdout", "")

        for line in output.splitlines():
            line = line.strip()

            if line:
                findings.append(line)

        return findings

    def json(self, result):

        try:
            return json.loads(result)

        except Exception:
            return {}