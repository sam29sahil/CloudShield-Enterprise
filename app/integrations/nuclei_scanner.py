"""
CloudShield Enterprise
Nuclei Scanner
"""

import subprocess


class NucleiScanner:

    def scan(self, target):

        try:

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