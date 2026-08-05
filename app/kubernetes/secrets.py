"""
CloudShield Enterprise
Kubernetes Secrets
"""

from kubernetes.client.rest import ApiException


class KubernetesSecrets:

    def __init__(self, client):

        self.client = client

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            api = self.client.core()

            secrets = api.list_secret_for_all_namespaces().items

            data = []

            for secret in secrets:

<<<<<<< HEAD
                data.append(
                    {
                        "name": secret.metadata.name,
                        "namespace": secret.metadata.namespace,
                        "type": secret.type,
                        "created": secret.metadata.creation_timestamp,
                    }
                )
=======
                data.append({

                    "name": secret.metadata.name,

                    "namespace": secret.metadata.namespace,

                    "type": secret.type,

                    "created": secret.metadata.creation_timestamp

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
