"""
CloudShield Enterprise
Kubernetes Scanner
"""

from app.kubernetes.services import KubernetesService


class KubernetesScanner:

    def __init__(self):

        self.service = KubernetesService()

    def scan(self):

<<<<<<< HEAD
        return self.service.dashboard()
=======
        return self.service.dashboard()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
