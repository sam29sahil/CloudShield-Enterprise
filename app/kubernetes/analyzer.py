"""
CloudShield Enterprise
Kubernetes Security Analyzer
"""


class KubernetesAnalyzer:

    def analyze(self, data):

        findings = []

        # ----------------------------------
        # Nodes
        # ----------------------------------

        for node in data.get("nodes", []):

            if node["status"] != "Ready":

                findings.append({

                    "severity": "High",

                    "resource": node["name"],

                    "title": "Node Not Ready",

                    "description": "Cluster node is not in Ready state."

                })

        # ----------------------------------
        # Pods
        # ----------------------------------

        for pod in data.get("pods", []):

            if pod["status"] != "Running":

                findings.append({

                    "severity": "Medium",

                    "resource": pod["name"],

                    "title": "Pod Not Running",

                    "description": "Pod is not currently running."

                })

        # ----------------------------------
        # Services
        # ----------------------------------

        for service in data.get("services", []):

            if service["type"] == "LoadBalancer":

                findings.append({

                    "severity": "Info",

                    "resource": service["name"],

                    "title": "Public Service",

                    "description": "Service exposed through LoadBalancer."

                })

        return findings