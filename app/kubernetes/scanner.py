"""
CloudShield Enterprise
Kubernetes Scanner
"""

from app.kubernetes.services import KubernetesService


class KubernetesScanner:

    def __init__(self):

        self.service = KubernetesService()

    def scan(self):

        return self.service.dashboard()