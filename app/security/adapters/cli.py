"""
CloudShield Enterprise
CLI Tool Adapter
"""

from app.security.adapters.base import BaseAdapter


class CLIAdapter(BaseAdapter):

<<<<<<< HEAD
    def adapt(self, tool, target, result, execution_time=0):
=======
    def adapt(
        self,
        tool,
        target,
        result,
        execution_time=0
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        stdout = result.get("stdout", "")
        stderr = result.get("stderr", "")

        findings = []

        for line in stdout.splitlines():

            line = line.strip()

            if line:

<<<<<<< HEAD
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
=======
                findings.append({

                    "severity": "Info",

                    "title": line,

                    "description": line

                })

        return {

            "success": result.get("success", False),

            "tool": tool,

            "target": target,

            "summary": {

                "status": (

                    "Completed"

                    if result.get("success")

                    else "Failed"

                )

            },

            "findings": findings,

            "raw_output": stdout,

            "error": stderr,

            "execution_time": execution_time

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
