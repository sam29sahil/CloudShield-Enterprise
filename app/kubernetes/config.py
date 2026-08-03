"""
CloudShield Enterprise
Kubernetes Configuration
"""

import os


class KubernetesConfig:

    # ---------------------------------------
    # Kubernetes Config File
    # ---------------------------------------

    KUBECONFIG = os.getenv(

        "KUBECONFIG",

        os.path.expanduser("~/.kube/config")

    )

    # ---------------------------------------
    # Default Namespace
    # ---------------------------------------

    DEFAULT_NAMESPACE = os.getenv(

        "K8S_NAMESPACE",

        "default"

    )

    # ---------------------------------------
    # Verify Configuration
    # ---------------------------------------

    @classmethod
    def configured(cls):

        return os.path.exists(

            cls.KUBECONFIG

        )