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

    def execute(
        self,
        tool,
        target=None,
        arguments=None,
        timeout=None
    ):
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

            }

        except FileNotFoundError:

            return {

                "success": False,

                "tool": tool,

                "error": f"{tool} is not installed."

            }

        except subprocess.TimeoutExpired:

            return {

                "success": False,

                "tool": tool,

                "error": f"{tool} timed out after {timeout} seconds."

            }

        except Exception as e:

            return {

                "success": False,

                "tool": tool,

                "error": str(e)

            }

    # ==========================================================
    # Installation Check
    # ==========================================================

    def is_installed(self, tool):
        """
        Check whether the tool exists.
        """

        try:

            subprocess.run(

                [tool, "--version"],

                capture_output=True,

                text=True,

                timeout=10

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

                [tool, "--version"],

                capture_output=True,

                text=True,

                timeout=10

            )

            output = result.stdout.strip()

            if not output:

                output = result.stderr.strip()

            return output or "Unknown"

        except Exception:

            return "Unknown"