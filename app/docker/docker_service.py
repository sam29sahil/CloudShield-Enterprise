"""
CloudShield Enterprise
Docker Service
"""

import docker
from app.docker.scanner import DockerScanner


class DockerService:

    def __init__(self):

        try:

            self.client = docker.from_env()

            self.client.ping()

            self.connected = True

        except Exception as e:

            print("Docker connection failed:", e)

            self.client = None

            self.connected = False

    # ----------------------------------
    # Security Findings
    # ----------------------------------

    def security_findings(self):

        if not self.connected:

            return []

        findings = []

        for container in self.containers():

            if container.attrs["HostConfig"].get("Privileged"):

                findings.append({

                    "severity": "Critical",

                    "container": container.name,

                    "title": "Privileged Container",

                    "description": "Container runs with privileged mode.",

                    "recommendation": "Disable privileged mode."

                })

            if container.attrs["Config"].get("User") in ("", "root"):

                findings.append({

                    "severity": "High",

                    "container": container.name,

                    "title": "Running as Root",

                    "description": "Container executes as root user.",

                    "recommendation": "Use a non-root user."

                })

        return findings       

    # ----------------------------------
    # Connection Status
    # ----------------------------------

    def is_running(self):

        return self.connected

    # ----------------------------------
    # Docker Version
    # ----------------------------------

    def version(self):

        if not self.connected:

            return {}

        return self.client.version()

    # ----------------------------------
    # Docker Information
    # ----------------------------------

    def info(self):

        if not self.connected:

            return {}

        return self.client.info()

    # ----------------------------------
    # Containers
    # ----------------------------------

    def containers(self):

        if not self.connected:
            return []

        try:

            return self.client.containers.list(all=True)

        except Exception:

            return []

    # ----------------------------------
    # Running Containers
    # ----------------------------------

    def running_containers(self):

        if not self.connected:

            return []

        return self.client.containers.list()

    # ----------------------------------
    # Images
    # ----------------------------------

    def images(self):

        if not self.connected:
            return []

        try:

            return self.client.images.list()

        except Exception:

            return []

    # ----------------------------------
    # Networks
    # ----------------------------------

    def networks(self):

        if not self.connected:
            return []

        try:

            return self.client.networks.list()

        except Exception:

            return []

    # ----------------------------------
    # Volumes
    # ----------------------------------

    def volumes(self):

        if not self.connected:
            return []

        try:

            return self.client.volumes.list()

        except Exception:

            return []

    # ----------------------------------
    # Container By ID
    # ----------------------------------

    def container_details(self, container_id):

        container = self.client.containers.get(container_id)

        return {

            "container": container,

            "stats": container.stats(stream=False),

            "logs": container.logs(
                tail=200
            ).decode(
                "utf-8",
                errors="ignore"
            )

        }

    # ----------------------------------
    # Start Container
    # ----------------------------------

    def start(self, container_id):

        container = self.container(container_id)

        if container:

            container.start()

            return True

        return False

    # ----------------------------------
    # Stop Container
    # ----------------------------------

    def stop(self, container_id):

        container = self.container(container_id)

        if container:

            container.stop()

            return True

        return False

    # ----------------------------------
    # Restart Container
    # ----------------------------------

    def restart(self, container_id):

        container = self.container(container_id)

        if container:

            container.restart()

            return True

        return False

    # ----------------------------------
    # Remove Container
    # ----------------------------------

    def remove(self, container_id):

        container = self.container(container_id)

        if container:

            container.remove(force=True)

            return True

        return False

    # ----------------------------------
    # Container Logs
    # ----------------------------------

    def logs(self, container_id, tail=200):

        container = self.container(container_id)

        if not container:

            return ""

        try:

            return container.logs(

                tail=tail

            ).decode(

                errors="ignore"

            )

        except Exception:

            return ""

    # ----------------------------------
    # Container Stats
    # ----------------------------------

    def stats(self, container_id):

        container = self.container(container_id)

        if not container:

            return {}

        try:

            return container.stats(

                stream=False

            )

        except Exception:

            return {}