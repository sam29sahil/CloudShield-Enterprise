"""
CloudShield Enterprise
Kubernetes Pods
"""

from kubernetes.client.rest import ApiException


class KubernetesPods:

    def __init__(self, client):

        self.client = client

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            api = self.client.core()

            pods = api.list_pod_for_all_namespaces().items

            data = []

            for pod in pods:

                data.append(
                    {
                        "name": pod.metadata.name,
                        "namespace": pod.metadata.namespace,
                        "node": pod.spec.node_name,
                        "status": pod.status.phase,
                        "ip": pod.status.pod_ip,
                    }
                )

            return data

        except ApiException:

            return []

        except Exception:

            return []
