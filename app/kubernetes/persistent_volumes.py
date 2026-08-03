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

                data.append({

                    "name": volume.metadata.name,

                    "capacity": volume.spec.capacity.get("storage"),

                    "access_modes": volume.spec.access_modes,

                    "status": volume.status.phase,

                    "storage_class": volume.spec.storage_class_name

                })

            return data

        except ApiException:

            return []

        except Exception:

            return []