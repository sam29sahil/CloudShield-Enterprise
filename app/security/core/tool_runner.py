"""
CloudShield Enterprise
Tool Runner
"""

import subprocess


class ToolRunner:
    """
    Executes security tools.
    """

    def execute(
        self,
        tool,
        target,
        arguments=None
    ):

        command = [tool]

        if arguments:

            if isinstance(arguments, list):

                command.extend(arguments)

            else:

                command.append(arguments)
            if target:    

                command.append(target)

        try:

            result = subprocess.run(

                command,

                capture_output=True,

                text=True,

                timeout=300

            )

            return {

                "success": result.returncode == 0,

                "command": " ".join(command),

                "stdout": result.stdout,

                "stderr": result.stderr,

                "return_code": result.returncode

            }

        except FileNotFoundError:

            return {

                "success": False,

                "error": f"{tool} is not installed."

            }

        except subprocess.TimeoutExpired:

            return {

                "success": False,

                "error": "Scan timed out."

            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }

    def is_installed(self, tool):
        """
        Check tool availability.
        """

        try:

            subprocess.run(

                [tool, "--version"],

                capture_output=True,

                text=True

            )

            return True

        except Exception:

            return False

    def version(self, tool):
        """
        Return tool version.
        """

        try:

            result = subprocess.run(

                [tool, "--version"],

                capture_output=True,

                text=True

            )

            return result.stdout.strip()

        except Exception:

            return "Unknown"