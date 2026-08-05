"""
CloudShield Enterprise
Kubernetes Nodes
"""

from kubernetes.client.rest import ApiException


class KubernetesNodes:

    def __init__(self, client):

        self.client = client

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            api = self.client.core()

            nodes = api.list_node().items

            data = []

            for node in nodes:

<<<<<<< HEAD
                data.append(
                    {
                        "name": node.metadata.name,
                        "os": node.status.node_info.os_image,
                        "kernel": node.status.node_info.kernel_version,
                        "kubelet": node.status.node_info.kubelet_version,
                        "container_runtime": node.status.node_info.container_runtime_version,
                        "architecture": node.status.node_info.architecture,
                        "status": (
                            "Ready"
                            if any(
                                condition.type == "Ready" and condition.status == "True"
                                for condition in node.status.conditions
                            )
                            else "Not Ready"
                        ),
                    }
                )
=======
                data.append({

                    "name": node.metadata.name,

                    "os": node.status.node_info.os_image,

                    "kernel": node.status.node_info.kernel_version,

                    "kubelet": node.status.node_info.kubelet_version,

                    "container_runtime": node.status.node_info.container_runtime_version,

                    "architecture": node.status.node_info.architecture,

                    "status": "Ready"

                    if any(

                        condition.type == "Ready"

                        and condition.status == "True"

                        for condition in node.status.conditions

                    )

                    else "Not Ready"

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
