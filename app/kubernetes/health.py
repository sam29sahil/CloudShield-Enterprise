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
<<<<<<< HEAD
            "connected": summary["connected"],
            "nodes": summary["nodes"],
            "pods": summary["pods"],
            "deployments": summary["deployments"],
            "services": summary["services"],
            "namespaces": summary["namespaces"],
            "ingress": summary["ingress"],
            "healthy": (summary["connected"] and summary["nodes"] > 0),
        }
=======

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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
