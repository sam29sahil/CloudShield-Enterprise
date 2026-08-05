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

<<<<<<< HEAD
                data.append(
                    {"name": role.metadata.name, "namespace": role.metadata.namespace}
                )
=======
                data.append({

                    "name": role.metadata.name,

                    "namespace": role.metadata.namespace

                })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

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

<<<<<<< HEAD
                data.append({"name": role.metadata.name})
=======
                data.append({

                    "name": role.metadata.name

                })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            return data

        except Exception:

<<<<<<< HEAD
            return []
=======
            return []
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
