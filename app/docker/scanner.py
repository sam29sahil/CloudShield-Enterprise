"""
CloudShield Enterprise
Docker Security Scanner
"""

from app.docker.docker_service import DockerService


class DockerScanner:

    def __init__(self):

        self.docker = DockerService()

    def security_findings(self):

        findings = []

        if not self.docker.is_running():

            return findings

        containers = self.docker.containers()

        for container in containers:

            attrs = container.attrs

            host = attrs.get("HostConfig", {})

            config = attrs.get("Config", {})

            # Privileged Container
            if host.get("Privileged"):

                findings.append({

                    "container": container.name,

                    "severity": "Critical",

                    "title": "Privileged Container",

                    "description": "Container is running in privileged mode."

                })

            # Running as Root
            if config.get("User", "") in ("", "root"):

                findings.append({

                    "container": container.name,

                    "severity": "High",

                    "title": "Running as Root",

                    "description": "Container is running as root."

                })

            # Host Network
            if host.get("NetworkMode") == "host":

                findings.append({

                    "container": container.name,

                    "severity": "High",

                    "title": "Host Network",

                    "description": "Container shares the host network."

                })

            # Docker Socket Mounted
            mounts = attrs.get("Mounts", [])

            for mount in mounts:

                if mount.get("Source") == "/var/run/docker.sock":

                    findings.append({

                        "container": container.name,

                        "severity": "Critical",

                        "title": "Docker Socket Mounted",

                        "description": "Container can control Docker daemon."

                    })

        return findings