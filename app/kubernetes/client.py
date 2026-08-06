"""
CloudShield Enterprise
Kubernetes Client
"""

from kubernetes import config
from kubernetes.client import CoreV1Api

from app.kubernetes.config import KubernetesConfig


class KubernetesClient:
    """
    Kubernetes API Client
    """

    def __init__(self):

        self.connected = False
        self.client = None

        if not KubernetesConfig.configured():
            return

        try:

            config.load_kube_config(config_file=KubernetesConfig.KUBECONFIG)

            self.client = CoreV1Api()

            self.connected = True

        except Exception:

            self.client = None

            self.connected = False

    # ---------------------------------------
    # Connection Status
    # ---------------------------------------

    def is_connected(self):

        return self.connected

    # ---------------------------------------
    # Core Client
    # ---------------------------------------

    def core(self):

        return self.client
