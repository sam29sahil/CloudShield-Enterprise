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

<<<<<<< HEAD
                data.append(
                    {
                        "name": service.metadata.name,
                        "namespace": service.metadata.namespace,
                        "type": service.spec.type,
                        "cluster_ip": service.spec.cluster_ip,
                        "ports": len(service.spec.ports),
                    }
                )
=======
                data.append({

                    "name": service.metadata.name,

                    "namespace": service.metadata.namespace,

                    "type": service.spec.type,

                    "cluster_ip": service.spec.cluster_ip,

                    "ports": len(service.spec.ports)

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
