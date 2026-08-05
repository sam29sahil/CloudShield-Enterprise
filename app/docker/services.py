"""
CloudShield Enterprise
Docker Business Service
"""

from app.docker.docker_service import DockerService
from app.docker.images import DockerImages
from app.docker.benchmark import DockerBenchmark


class DockerDashboardService:

    def __init__(self):

        self.docker = DockerService()
        self.images_service = DockerImages()
        self.benchmark = DockerBenchmark()

    # ----------------------------------
    # Images Summary
    # ----------------------------------

    def image_summary(self):

        return self.images_service.summary()

    # ----------------------------------
    # Docker Benchmark
    # ----------------------------------

    def benchmark(self):

        findings = self.security_summary()

        return {
            "score": findings["score"],
            "risk": findings["risk"],
            "critical": sum(
                1
                for f in self.docker.security_findings()
                if f["severity"] == "Critical"
            ),
            "high": sum(
                1 for f in self.docker.security_findings() if f["severity"] == "High"
            ),
            "medium": sum(
                1 for f in self.docker.security_findings() if f["severity"] == "Medium"
            ),
            "low": sum(
                1 for f in self.docker.security_findings() if f["severity"] == "Low"
            ),
            "checks": self.docker.security_findings(),
        }

    # ----------------------------------
    # Security Findings
    # ----------------------------------

    def findings(self):

        return self.docker.security_findings()

    # ----------------------------------
    # Dashboard Summary
    # ----------------------------------

    def summary(self):

        if not self.docker.is_running():

            return {
                "connected": False,
                "running": 0,
                "stopped": 0,
                "images": 0,
                "networks": 0,
                "volumes": 0,
            }

        containers = self.docker.containers() or []

        running = self.docker.running_containers() or []

        images = self.docker.images() or []

        networks = self.docker.networks() or []

        volumes = self.docker.volumes() or []

        return {
            "connected": True,
            "running": len(running),
            "stopped": len(containers) - len(running),
            "images": len(images),
            "networks": len(networks),
            "volumes": len(volumes),
        }

    # ----------------------------------
    # Security Summary
    # ----------------------------------

    def security_summary(self):

        if not self.docker.is_running():

            return {"score": 0, "risk": "Unknown", "findings": 0}

        findings = self.docker.security_findings()

        critical = sum(1 for finding in findings if finding["severity"] == "Critical")

        high = sum(1 for finding in findings if finding["severity"] == "High")

        score = max(100 - critical * 20 - high * 10, 0)

        return {
            "score": score,
            "risk": ("Critical" if critical else "High" if high else "Low"),
            "findings": len(findings),
        }

    def container_details(self, container_id):

        return self.docker.container_details(container_id)

    # ----------------------------------
    # Docker Information
    # ----------------------------------

    def information(self):

        if not self.docker.is_running():

            return {}

        info = self.docker.info()

        version = self.docker.version()

        return {
            "engine": version.get("Version"),
            "api": version.get("ApiVersion"),
            "os": info.get("OperatingSystem"),
            "kernel": info.get("KernelVersion"),
            "architecture": info.get("Architecture"),
            "cpus": info.get("NCPU"),
            "memory": round(info.get("MemTotal", 0) / 1024 / 1024 / 1024, 2),
            "containers": info.get("Containers"),
            "running": info.get("ContainersRunning"),
            "paused": info.get("ContainersPaused"),
            "stopped": info.get("ContainersStopped"),
        }

    # ----------------------------------
    # Container List
    # ----------------------------------

    def containers(self):

        return self.docker.containers()

    # ----------------------------------
    # Image List
    # ----------------------------------

    def images(self):

        return self.docker.images()

    # ----------------------------------
    # Network List
    # ----------------------------------

    def networks(self):

        return self.docker.networks()

    # ----------------------------------
    # Volume List
    # ----------------------------------

    def volumes(self):

        return self.docker.volumes()

    # ----------------------------------
    # Container Details
    # ----------------------------------

    def details(self, container_id):

        container = self.docker.container(container_id)

        if not container:

            return None

        return {
            "container": container,
            "logs": self.docker.logs(container_id),
            "stats": self.docker.stats(container_id),
        }

    # ----------------------------------
    # Container Actions
    # ----------------------------------

    def start(self, container_id):

        return self.docker.start(container_id)

    def stop(self, container_id):

        return self.docker.stop(container_id)

    def restart(self, container_id):

        return self.docker.restart(container_id)

    def remove(self, container_id):

        return self.docker.remove(container_id)

    # ----------------------------------
    # Dashboard
    # ----------------------------------

    def dashboard(self):

        return {
            "summary": self.summary(),
            "information": self.information(),
            "security": self.security_summary(),
        }

    # ----------------------------------
    # Health
    # ----------------------------------

    def health(self):

        return {
            "docker_running": self.docker.is_running(),
            "containers": len(self.docker.running_containers() or []),
            "images": len(self.docker.images() or []),
        }
