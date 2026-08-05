"""
CloudShield Enterprise
Tool Runner
"""

import subprocess
import time


class ToolRunner:
    """
    Executes external security tools.
    """

    DEFAULT_TIMEOUT = 300

    # ==========================================================
    # Execute Tool
    # ==========================================================

<<<<<<< HEAD
    def execute(self, tool, target=None, arguments=None, timeout=None):
=======
    def execute(
        self,
        tool,
        target=None,
        arguments=None,
        timeout=None
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        """
        Execute a security tool.
        """

        command = [tool]

        if arguments:

            if isinstance(arguments, list):

                command.extend(arguments)

            elif isinstance(arguments, str):

                command.extend(arguments.split())

        # Always append target if provided
        if target:

            command.append(target)

        timeout = timeout or self.DEFAULT_TIMEOUT

        start = time.perf_counter()

        try:

            result = subprocess.run(
<<<<<<< HEAD
                command, capture_output=True, text=True, timeout=timeout
            )

            elapsed = round(time.perf_counter() - start, 2)

            return {
                "success": result.returncode == 0,
                "tool": tool,
                "command": " ".join(command),
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip(),
                "return_code": result.returncode,
                "execution_time": elapsed,
=======

                command,

                capture_output=True,

                text=True,

                timeout=timeout

            )

            elapsed = round(

                time.perf_counter() - start,

                2

            )

            return {

                "success": result.returncode == 0,

                "tool": tool,

                "command": " ".join(command),

                "stdout": result.stdout.strip(),

                "stderr": result.stderr.strip(),

                "return_code": result.returncode,

                "execution_time": elapsed

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except FileNotFoundError:

            return {
<<<<<<< HEAD
                "success": False,
                "tool": tool,
                "error": f"{tool} is not installed.",
=======

                "success": False,

                "tool": tool,

                "error": f"{tool} is not installed."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except subprocess.TimeoutExpired:

            return {
<<<<<<< HEAD
                "success": False,
                "tool": tool,
                "error": f"{tool} timed out after {timeout} seconds.",
=======

                "success": False,

                "tool": tool,

                "error": f"{tool} timed out after {timeout} seconds."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        except Exception as e:

<<<<<<< HEAD
            return {"success": False, "tool": tool, "error": str(e)}
=======
            return {

                "success": False,

                "tool": tool,

                "error": str(e)

            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # ==========================================================
    # Installation Check
    # ==========================================================

    def is_installed(self, tool):
        """
        Check whether the tool exists.
        """

        try:

            subprocess.run(
<<<<<<< HEAD
                [tool, "--version"], capture_output=True, text=True, timeout=10
=======

                [tool, "--version"],

                capture_output=True,

                text=True,

                timeout=10

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )

            return True

        except Exception:

            return False

    # ==========================================================
    # Version
    # ==========================================================

    def version(self, tool):
        """
        Return tool version.
        """

        try:

            result = subprocess.run(
<<<<<<< HEAD
                [tool, "--version"], capture_output=True, text=True, timeout=10
=======

                [tool, "--version"],

                capture_output=True,

                text=True,

                timeout=10

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )

            output = result.stdout.strip()

            if not output:

                output = result.stderr.strip()

            return output or "Unknown"

        except Exception:

<<<<<<< HEAD
            return "Unknown"
=======
            return "Unknown"
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
