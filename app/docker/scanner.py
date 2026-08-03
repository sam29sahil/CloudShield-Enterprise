"""
CloudShield Enterprise
Docker Security Scanner
"""

import docker


class DockerScanner:
    """
    Docker Security Scanner
    """

    def __init__(self):

        try:

            self.client = docker.from_env()

            self.client.ping()

            self.connected = True

        except Exception:

            self.client = None

            self.connected = False

    # ----------------------------------
    # Connection
    # ----------------------------------

    def is_connected(self):

        return self.connected

    # ----------------------------------
    # Scan Docker Environment
    # ----------------------------------

    def scan(self):

        if not self.connected:

            return []

        findings = []

        try:

            containers = self.client.containers.list(all=True)

            for container in containers:

                # Privileged Container
                if container.attrs["HostConfig"].get("Privileged"):

                    findings.append({

                        "title": "Privileged Container",

                        "severity": "Critical",

                        "container": container.name,

                        "description": (
                            "Container is running in privileged mode."
                        )

                    })

                # Host Network
                if container.attrs["HostConfig"].get("NetworkMode") == "host":

                    findings.append({

                        "title": "Host Network Mode",

                        "severity": "High",

                        "container": container.name,

                        "description": (
                            "Container shares host network."
                        )

                    })

                # Running as Root
                user = container.attrs["Config"].get("User", "")

                if user in ("", "0", "root"):

                    findings.append({

                        "title": "Running as Root",

                        "severity": "Medium",

                        "container": container.name,

                        "description": (
                            "Container appears to run as root."
                        )

                    })

        except Exception:

            return []

        return findings

    # ----------------------------------
    # Security Score
    # ----------------------------------

    def score(self):

        findings = self.scan()

        critical = sum(

            1 for finding in findings

            if finding["severity"] == "Critical"

        )

        high = sum(

            1 for finding in findings

            if finding["severity"] == "High"

        )

        score = max(

            100 - (critical * 20) - (high * 10),

            0

        )

        return {

            "score": score,

            "risk_level": (

                "Critical"

                if critical

                else "High"

                if high

                else "Low"

            ),

            "findings": findings

        }