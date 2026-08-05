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

<<<<<<< HEAD
            config.load_kube_config(config_file=KubernetesConfig.KUBECONFIG)
=======
            config.load_kube_config(

                config_file=KubernetesConfig.KUBECONFIG

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

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

<<<<<<< HEAD
        return self.client
=======
        return self.client
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
