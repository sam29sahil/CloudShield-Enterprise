"""
CloudShield Enterprise
Nuclei Scanner
"""

import subprocess


class NucleiScanner:

    def scan(self, target):

        try:

<<<<<<< HEAD
            command = ["nuclei", "-u", target, "-silent"]

            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, text=True
            )

            return {"success": True, "tool": "Nuclei", "output": output}

        except Exception as e:

            return {"success": False, "tool": "Nuclei", "error": str(e)}
=======
            command = [

                "nuclei",

                "-u",

                target,

                "-silent"

            ]

            output = subprocess.check_output(

                command,

                stderr=subprocess.STDOUT,

                text=True

            )

            return {

                "success": True,

                "tool": "Nuclei",

                "output": output

            }

        except Exception as e:

            return {

                "success": False,

                "tool": "Nuclei",

                "error": str(e)

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
