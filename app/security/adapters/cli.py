"""
CloudShield Enterprise
CLI Tool Adapter
"""

from app.security.adapters.base import BaseAdapter


class CLIAdapter(BaseAdapter):

    def adapt(self, tool, target, result, execution_time=0):

        stdout = result.get("stdout", "")
        stderr = result.get("stderr", "")

        findings = []

        for line in stdout.splitlines():

            line = line.strip()

            if line:

                findings.append(
                    {"severity": "Info", "title": line, "description": line}
                )

        return {
            "success": result.get("success", False),
            "tool": tool,
            "target": target,
            "summary": {"status": ("Completed" if result.get("success") else "Failed")},
            "findings": findings,
            "raw_output": stdout,
            "error": stderr,
            "execution_time": execution_time,
        }
