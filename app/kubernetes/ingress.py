"""
CloudShield Enterprise
Kubernetes Ingress
"""

from kubernetes.client import NetworkingV1Api
from kubernetes.client.rest import ApiException


class KubernetesIngress:

    def __init__(self, client):

        self.client = client

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            api = NetworkingV1Api()

            ingresses = api.list_ingress_for_all_namespaces().items

            data = []

            for ingress in ingresses:

                hosts = []

                if ingress.spec.rules:

                    for rule in ingress.spec.rules:

                        hosts.append(rule.host)

                data.append(
                    {
                        "name": ingress.metadata.name,
                        "namespace": ingress.metadata.namespace,
                        "hosts": hosts,
                        "class": ingress.spec.ingress_class_name,
                    }
                )

            return data

        except ApiException:

            return []

        except Exception:

            return []
