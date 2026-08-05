"""
CloudShield Enterprise
WhatWeb Scanner
"""

import subprocess


class WhatWebScanner:

    def scan(self, target):

        try:

            command = ["whatweb", "--color=never", target]

            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, text=True
            )

            return {"success": True, "tool": "WhatWeb", "output": output}

        except Exception as e:

            return {"success": False, "tool": "WhatWeb", "error": str(e)}
