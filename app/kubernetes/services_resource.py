"""
CloudShield Enterprise
Kubernetes Services
"""

from kubernetes.client.rest import ApiException


class KubernetesServices:

    def __init__(self, client):

        self.client = client

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            api = self.client.core()

            services = api.list_service_for_all_namespaces().items

            data = []

            for service in services:

                data.append(
                    {
                        "name": service.metadata.name,
                        "namespace": service.metadata.namespace,
                        "type": service.spec.type,
                        "cluster_ip": service.spec.cluster_ip,
                        "ports": len(service.spec.ports),
                    }
                )

            return data

        except ApiException:

            return []

        except Exception:

            return []
