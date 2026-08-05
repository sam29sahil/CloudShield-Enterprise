"""
CloudShield Enterprise
Nikto Scanner
"""

import subprocess


class NiktoScanner:

    def scan(self, target):

        try:

<<<<<<< HEAD
            command = ["nikto", "-h", target]

            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, text=True
            )

            return {"success": True, "tool": "Nikto", "output": output}

        except Exception as e:

            return {"success": False, "tool": "Nikto", "error": str(e)}
=======
            command = [

                "nikto",

                "-h",

                target

            ]

            output = subprocess.check_output(

                command,

                stderr=subprocess.STDOUT,

                text=True

            )

            return {

                "success": True,

                "tool": "Nikto",

                "output": output

            }

        except Exception as e:

            return {

                "success": False,

                "tool": "Nikto",

                "error": str(e)

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
