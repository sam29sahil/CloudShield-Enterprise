"""
CloudShield Enterprise
WAF Detection
"""

import subprocess


class WAFScanner:

    def scan(self, target):

        try:

            command = ["wafw00f", target]

            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, text=True
            )

            return {"success": True, "tool": "WAFW00F", "output": output}

        except Exception as e:

            return {"success": False, "tool": "WAFW00F", "error": str(e)}
