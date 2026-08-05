"""
CloudShield Enterprise
Kubernetes Namespaces
"""

from kubernetes.client.rest import ApiException


class KubernetesNamespaces:

    def __init__(self, client):

        self.client = client

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            api = self.client.core()

            namespaces = api.list_namespace().items

            data = []

            for namespace in namespaces:

<<<<<<< HEAD
                data.append(
                    {
                        "name": namespace.metadata.name,
                        "status": namespace.status.phase,
                        "created": namespace.metadata.creation_timestamp,
                    }
                )
=======
                data.append({

                    "name": namespace.metadata.name,

                    "status": namespace.status.phase,

                    "created": namespace.metadata.creation_timestamp

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
