"""
CloudShield Enterprise
Kubernetes Service
"""

from app.kubernetes.client import KubernetesClient
from app.kubernetes.nodes import KubernetesNodes
from app.kubernetes.pods import KubernetesPods
from app.kubernetes.namespaces import KubernetesNamespaces
from app.kubernetes.deployments import KubernetesDeployments
from app.kubernetes.services_resource import KubernetesServices
from app.kubernetes.ingress import KubernetesIngress


class KubernetesService:

    def __init__(self):

        self.client = KubernetesClient()

        self.nodes = KubernetesNodes(self.client)
        self.pods = KubernetesPods(self.client)
        self.namespaces = KubernetesNamespaces(self.client)
        self.deployments = KubernetesDeployments(self.client)
        self.services = KubernetesServices(self.client)
        self.ingress = KubernetesIngress(self.client)

    # ------------------------------------
    # Connection
    # ------------------------------------

    def connected(self):

        return self.client.is_connected()

    # ------------------------------------
    # Dashboard Summary
    # ------------------------------------

    def summary(self):

        if not self.connected():

            return {

                "connected": False,
                "nodes": 0,
                "pods": 0,
                "deployments": 0,
                "services": 0,
                "namespaces": 0,
                "ingress": 0

            }

        return {

            "connected": True,

            "nodes": len(self.nodes.list()),

            "pods": len(self.pods.list()),

            "deployments": len(self.deployments.list()),

            "services": len(self.services.list()),

            "namespaces": len(self.namespaces.list()),

            "ingress": len(self.ingress.list())

        }

    # ------------------------------------
    # Complete Dashboard Data
    # ------------------------------------

    def dashboard(self):

        return {

            "summary": self.summary(),

            "nodes": self.nodes.list(),

            "pods": self.pods.list(),

            "deployments": self.deployments.list(),

            "services": self.services.list(),

            "namespaces": self.namespaces.list(),

            "ingress": self.ingress.list()

        }