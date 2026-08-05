"""
CloudShield Enterprise
Kubernetes Network Policies
"""

from kubernetes.client import NetworkingV1Api


class KubernetesNetworkPolicies:

    def __init__(self, client):

        self.client = client

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            api = NetworkingV1Api()

            policies = api.list_network_policy_for_all_namespaces().items

            data = []

            for policy in policies:

<<<<<<< HEAD
                data.append(
                    {
                        "name": policy.metadata.name,
                        "namespace": policy.metadata.namespace,
                        "created": policy.metadata.creation_timestamp,
                    }
                )
=======
                data.append({

                    "name": policy.metadata.name,

                    "namespace": policy.metadata.namespace,

                    "created": policy.metadata.creation_timestamp

                })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            return data

        except Exception:

<<<<<<< HEAD
            return []
=======
            return []
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
