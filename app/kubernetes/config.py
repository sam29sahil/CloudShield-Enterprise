"""
CloudShield Enterprise
Kubernetes Configuration
"""

import os


class KubernetesConfig:

    # ---------------------------------------
    # Kubernetes Config File
    # ---------------------------------------

<<<<<<< HEAD
    KUBECONFIG = os.getenv("KUBECONFIG", os.path.expanduser("~/.kube/config"))
=======
    KUBECONFIG = os.getenv(

        "KUBECONFIG",

        os.path.expanduser("~/.kube/config")

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # ---------------------------------------
    # Default Namespace
    # ---------------------------------------

<<<<<<< HEAD
    DEFAULT_NAMESPACE = os.getenv("K8S_NAMESPACE", "default")
=======
    DEFAULT_NAMESPACE = os.getenv(

        "K8S_NAMESPACE",

        "default"

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    # ---------------------------------------
    # Verify Configuration
    # ---------------------------------------

    @classmethod
    def configured(cls):

<<<<<<< HEAD
        return os.path.exists(cls.KUBECONFIG)
=======
        return os.path.exists(

            cls.KUBECONFIG

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
