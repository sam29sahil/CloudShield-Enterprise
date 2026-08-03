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

                data.append({

                    "name": policy.metadata.name,

                    "namespace": policy.metadata.namespace,

                    "created": policy.metadata.creation_timestamp

                })

            return data

        except Exception:

            return []