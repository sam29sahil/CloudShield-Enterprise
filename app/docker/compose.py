"""
CloudShield Enterprise
Docker Compose
"""

import subprocess


class DockerCompose:

    # ----------------------------------
    # Version
    # ----------------------------------

    def version(self):

        try:

            result = subprocess.run(
                ["docker", "compose", "version"], capture_output=True, text=True
            )

            return result.stdout.strip()

        except Exception:

            return "Docker Compose Not Installed"

    # ----------------------------------
    # Services
    # ----------------------------------

    def services(self):

        try:

            result = subprocess.run(
                ["docker", "compose", "ps"], capture_output=True, text=True
            )

            return result.stdout

        except Exception:

            return ""

    # ----------------------------------
    # Projects
    # ----------------------------------

    def projects(self):

        try:

            result = subprocess.run(
                ["docker", "compose", "ls"], capture_output=True, text=True
            )

            return result.stdout

        except Exception:

            return ""
