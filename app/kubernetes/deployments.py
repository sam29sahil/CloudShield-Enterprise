"""
CloudShield Enterprise
Kubernetes Deployments
"""

from kubernetes.client import AppsV1Api
from kubernetes.client.rest import ApiException


class KubernetesDeployments:

    def __init__(self, client):

        self.client = client

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            api = AppsV1Api()

            deployments = api.list_deployment_for_all_namespaces().items

            data = []

            for deployment in deployments:

<<<<<<< HEAD
                data.append(
                    {
                        "name": deployment.metadata.name,
                        "namespace": deployment.metadata.namespace,
                        "replicas": deployment.spec.replicas,
                        "available": deployment.status.available_replicas or 0,
                        "updated": deployment.status.updated_replicas or 0,
                    }
                )
=======
                data.append({

                    "name": deployment.metadata.name,

                    "namespace": deployment.metadata.namespace,

                    "replicas": deployment.spec.replicas,

                    "available": deployment.status.available_replicas or 0,

                    "updated": deployment.status.updated_replicas or 0

                })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            return data

        except ApiException:

            return []

        except Exception:

<<<<<<< HEAD
            return []
=======
            return []
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
