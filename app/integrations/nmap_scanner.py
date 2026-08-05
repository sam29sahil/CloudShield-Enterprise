"""
CloudShield Enterprise
Nmap Scanner
"""

import subprocess


class NmapScanner:

    def quick_scan(self, target):

        try:

<<<<<<< HEAD
            command = ["nmap", "-F", target]

            output = subprocess.check_output(
                command, text=True, stderr=subprocess.STDOUT
            )

            return {"success": True, "type": "Quick Scan", "output": output}

        except Exception as e:

            return {"success": False, "error": str(e)}
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def service_scan(self, target):

        try:

<<<<<<< HEAD
            command = ["nmap", "-sV", target]

            output = subprocess.check_output(
                command, text=True, stderr=subprocess.STDOUT
            )

            return {"success": True, "type": "Service Detection", "output": output}

        except Exception as e:

            return {"success": False, "error": str(e)}
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def os_scan(self, target):

        try:

<<<<<<< HEAD
            command = ["nmap", "-O", target]

            output = subprocess.check_output(
                command, text=True, stderr=subprocess.STDOUT
            )

            return {"success": True, "type": "OS Detection", "output": output}

        except Exception as e:

            return {"success": False, "error": str(e)}
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def full_scan(self, target):

        try:

<<<<<<< HEAD
            command = ["nmap", "-A", target]

            output = subprocess.check_output(
                command, text=True, stderr=subprocess.STDOUT
            )

            return {"success": True, "type": "Aggressive Scan", "output": output}

        except Exception as e:

            return {"success": False, "error": str(e)}
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
