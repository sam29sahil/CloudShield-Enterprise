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

<<<<<<< HEAD
                findings.append(
                    {
                        "severity": "High",
                        "resource": node["name"],
                        "title": "Node Not Ready",
                        "description": "Cluster node is not in Ready state.",
                    }
                )
=======
                findings.append({

                    "severity": "High",

                    "resource": node["name"],

                    "title": "Node Not Ready",

                    "description": "Cluster node is not in Ready state."

                })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # ----------------------------------
        # Pods
        # ----------------------------------

        for pod in data.get("pods", []):

            if pod["status"] != "Running":

<<<<<<< HEAD
                findings.append(
                    {
                        "severity": "Medium",
                        "resource": pod["name"],
                        "title": "Pod Not Running",
                        "description": "Pod is not currently running.",
                    }
                )
=======
                findings.append({

                    "severity": "Medium",

                    "resource": pod["name"],

                    "title": "Pod Not Running",

                    "description": "Pod is not currently running."

                })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # ----------------------------------
        # Services
        # ----------------------------------

        for service in data.get("services", []):

            if service["type"] == "LoadBalancer":

<<<<<<< HEAD
                findings.append(
                    {
                        "severity": "Info",
                        "resource": service["name"],
                        "title": "Public Service",
                        "description": "Service exposed through LoadBalancer.",
                    }
                )

        return findings
=======
                findings.append({

                    "severity": "Info",

                    "resource": service["name"],

                    "title": "Public Service",

                    "description": "Service exposed through LoadBalancer."

                })

        return findings
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
