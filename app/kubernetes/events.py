"""
CloudShield Enterprise
Kubernetes Events
"""

from kubernetes.client.rest import ApiException


class KubernetesEvents:

    def __init__(self, client):

        self.client = client

    def list(self, limit=100):

        if not self.client.is_connected():

            return []

        try:

            api = self.client.core()

<<<<<<< HEAD
            events = api.list_event_for_all_namespaces(limit=limit).items
=======
            events = api.list_event_for_all_namespaces(

                limit=limit

            ).items
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            data = []

            for event in events:

<<<<<<< HEAD
                data.append(
                    {
                        "namespace": event.metadata.namespace,
                        "resource": event.involved_object.kind,
                        "name": event.involved_object.name,
                        "reason": event.reason,
                        "type": event.type,
                        "message": event.message,
                        "time": event.last_timestamp,
                    }
                )
=======
                data.append({

                    "namespace": event.metadata.namespace,

                    "resource": event.involved_object.kind,

                    "name": event.involved_object.name,

                    "reason": event.reason,

                    "type": event.type,

                    "message": event.message,

                    "time": event.last_timestamp

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
