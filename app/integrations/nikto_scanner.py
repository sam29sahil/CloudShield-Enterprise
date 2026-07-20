"""
CloudShield Enterprise
Nikto Scanner
"""

import subprocess


class NiktoScanner:

    def scan(self, target):

        try:

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