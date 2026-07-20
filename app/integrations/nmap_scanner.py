"""
CloudShield Enterprise
Nmap Scanner
"""

import subprocess


class NmapScanner:

    def quick_scan(self, target):

        try:

            command = [

                "nmap",

                "-F",

                target

            ]

            output = subprocess.check_output(

                command,

                text=True,

                stderr=subprocess.STDOUT

            )

            return {

                "success": True,

                "type": "Quick Scan",

                "output": output

            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }

    def service_scan(self, target):

        try:

            command = [

                "nmap",

                "-sV",

                target

            ]

            output = subprocess.check_output(

                command,

                text=True,

                stderr=subprocess.STDOUT

            )

            return {

                "success": True,

                "type": "Service Detection",

                "output": output

            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }

    def os_scan(self, target):

        try:

            command = [

                "nmap",

                "-O",

                target

            ]

            output = subprocess.check_output(

                command,

                text=True,

                stderr=subprocess.STDOUT

            )

            return {

                "success": True,

                "type": "OS Detection",

                "output": output

            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }

    def full_scan(self, target):

        try:

            command = [

                "nmap",

                "-A",

                target

            ]

            output = subprocess.check_output(

                command,

                text=True,

                stderr=subprocess.STDOUT

            )

            return {

                "success": True,

                "type": "Aggressive Scan",

                "output": output

            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }