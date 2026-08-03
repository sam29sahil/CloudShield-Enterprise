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

                data.append({

                    "name": deployment.metadata.name,

                    "namespace": deployment.metadata.namespace,

                    "replicas": deployment.spec.replicas,

                    "available": deployment.status.available_replicas or 0,

                    "updated": deployment.status.updated_replicas or 0

                })

            return data

        except ApiException:

            return []

        except Exception:

            return []