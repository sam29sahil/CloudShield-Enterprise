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

            events = api.list_event_for_all_namespaces(

                limit=limit

            ).items

            data = []

            for event in events:

                data.append({

                    "namespace": event.metadata.namespace,

                    "resource": event.involved_object.kind,

                    "name": event.involved_object.name,

                    "reason": event.reason,

                    "type": event.type,

                    "message": event.message,

                    "time": event.last_timestamp

                })

            return data

        except ApiException:

            return []

        except Exception:

            return []