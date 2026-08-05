"""
CloudShield Enterprise
Kubernetes Cluster
"""

from kubernetes.client import VersionApi


class KubernetesCluster:

    def __init__(self, client):

        self.client = client

    def info(self):

        if not self.client.is_connected():

            return {}

        try:

            version = VersionApi().get_code()

            return {
                "platform": "Kubernetes",
                "git_version": version.git_version,
                "major": version.major,
                "minor": version.minor,
                "compiler": version.compiler,
                "build_date": version.build_date,
                "go_version": version.go_version,
                "os": version.platform,
            }

        except Exception:

            return {}
