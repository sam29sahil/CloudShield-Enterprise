"""
CloudShield Enterprise
WhatWeb Scanner
"""

import subprocess


class WhatWebScanner:

    def scan(self, target):

        try:

<<<<<<< HEAD
            command = ["whatweb", "--color=never", target]

            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, text=True
            )

            return {"success": True, "tool": "WhatWeb", "output": output}

        except Exception as e:

            return {"success": False, "tool": "WhatWeb", "error": str(e)}
=======
            command = [

                "whatweb",

                "--color=never",

                target

            ]

            output = subprocess.check_output(

                command,

                stderr=subprocess.STDOUT,

                text=True

            )

            return {

                "success": True,

                "tool": "WhatWeb",

                "output": output

            }

        except Exception as e:

            return {

                "success": False,

                "tool": "WhatWeb",

                "error": str(e)

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
