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
<<<<<<< HEAD
                ["docker", "compose", "version"], capture_output=True, text=True
=======

                ["docker", "compose", "version"],

                capture_output=True,

                text=True

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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
<<<<<<< HEAD
                ["docker", "compose", "ps"], capture_output=True, text=True
=======

                ["docker", "compose", "ps"],

                capture_output=True,

                text=True

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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
<<<<<<< HEAD
                ["docker", "compose", "ls"], capture_output=True, text=True
=======

                ["docker", "compose", "ls"],

                capture_output=True,

                text=True

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            )

            return result.stdout

        except Exception:

<<<<<<< HEAD
            return ""
=======
            return ""
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
