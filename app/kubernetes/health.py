"""
CloudShield Enterprise
Kubernetes Health
"""

from app.kubernetes.services import KubernetesService


class KubernetesHealth:

    def __init__(self):

        self.service = KubernetesService()

    def status(self):

        summary = self.service.summary()

        return {

            "connected": summary["connected"],

            "nodes": summary["nodes"],

            "pods": summary["pods"],

            "deployments": summary["deployments"],

            "services": summary["services"],

            "namespaces": summary["namespaces"],

            "ingress": summary["ingress"],

            "healthy": (

                summary["connected"]

                and summary["nodes"] > 0

            )

        }