"""
CloudShield Enterprise
Kubernetes Persistent Volumes
"""

from kubernetes.client.rest import ApiException


class KubernetesPersistentVolumes:

    def __init__(self, client):

        self.client = client

    def list(self):

        if not self.client.is_connected():

            return []

        try:

            api = self.client.core()

            volumes = api.list_persistent_volume().items

            data = []

            for volume in volumes:

<<<<<<< HEAD
                data.append(
                    {
                        "name": volume.metadata.name,
                        "capacity": volume.spec.capacity.get("storage"),
                        "access_modes": volume.spec.access_modes,
                        "status": volume.status.phase,
                        "storage_class": volume.spec.storage_class_name,
                    }
                )
=======
                data.append({

                    "name": volume.metadata.name,

                    "capacity": volume.spec.capacity.get("storage"),

                    "access_modes": volume.spec.access_modes,

                    "status": volume.status.phase,

                    "storage_class": volume.spec.storage_class_name

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
