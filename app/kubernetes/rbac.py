"""
CloudShield Enterprise
Kubernetes RBAC
"""

from kubernetes.client import RbacAuthorizationV1Api


class KubernetesRBAC:

    def __init__(self, client):

        self.client = client

    def roles(self):

        if not self.client.is_connected():

            return []

        try:

            api = RbacAuthorizationV1Api()

            roles = api.list_role_for_all_namespaces().items

            data = []

            for role in roles:

                data.append(
                    {"name": role.metadata.name, "namespace": role.metadata.namespace}
                )

            return data

        except Exception:

            return []

    def cluster_roles(self):

        if not self.client.is_connected():

            return []

        try:

            api = RbacAuthorizationV1Api()

            roles = api.list_cluster_role().items

            data = []

            for role in roles:

                data.append({"name": role.metadata.name})

            return data

        except Exception:

            return []
