"""
CloudShield Enterprise
Nmap Adapter
"""

from app.security.adapters.base import BaseAdapter


class NmapAdapter(BaseAdapter):

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

        findings = []

        for port in result.get("ports", []):

<<<<<<< HEAD
            findings.append(
                {
                    "severity": "Info",
                    "title": f"Port {port['port']} ({port['protocol']})",
                    "description": f"{port['service']} " f"{port['state']}",
                }
            )

        return {
            "success": result.get("success", False),
            "tool": tool,
            "target": target,
            "summary": {
                "status": ("Completed" if result.get("success") else "Failed"),
                "hostname": result.get("hostname", ""),
            },
            "findings": findings,
            "raw_output": str(result),
            "error": result.get("error", ""),
            "execution_time": execution_time,
        }
=======
            findings.append({

                "severity": "Info",

                "title": f"Port {port['port']} ({port['protocol']})",

                "description":

                    f"{port['service']} "

                    f"{port['state']}"

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

                ),

                "hostname": result.get(

                    "hostname",

                    ""

                )

            },

            "findings": findings,

            "raw_output": str(result),

            "error": result.get(

                "error",

                ""

            ),

            "execution_time": execution_time

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
