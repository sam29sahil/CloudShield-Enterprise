"""
CloudShield Enterprise
MITRE ATT&CK Service
"""


class MITREService:
    """
    MITRE ATT&CK Service
    """

    def __init__(self):

        self.techniques = [
            {
                "id": "TA0001",
                "name": "Initial Access",
                "description": "Techniques used to gain initial access.",
            },
            {"id": "TA0002", "name": "Execution", "description": "Run malicious code."},
            {
                "id": "TA0003",
                "name": "Persistence",
                "description": "Maintain access after reboot.",
            },
            {
                "id": "TA0004",
                "name": "Privilege Escalation",
                "description": "Gain higher privileges.",
            },
            {
                "id": "TA0005",
                "name": "Defense Evasion",
                "description": "Avoid security detection.",
            },
            {
                "id": "TA0006",
                "name": "Credential Access",
                "description": "Steal credentials.",
            },
            {
                "id": "TA0007",
                "name": "Discovery",
                "description": "Discover environment information.",
            },
            {
                "id": "TA0008",
                "name": "Lateral Movement",
                "description": "Move through the network.",
            },
            {
                "id": "TA0009",
                "name": "Collection",
                "description": "Collect sensitive data.",
            },
            {
                "id": "TA0010",
                "name": "Exfiltration",
                "description": "Transfer stolen data.",
            },
            {
                "id": "TA0011",
                "name": "Impact",
                "description": "Disrupt or destroy systems.",
            },
        ]

    # -------------------------------------

    def all(self):

        return self.techniques

    # -------------------------------------

    def count(self):

        return len(self.techniques)

    # -------------------------------------

    def search(self, keyword):

        keyword = keyword.lower()

        return [
            t
            for t in self.techniques
            if keyword in t["name"].lower() or keyword in t["id"].lower()
        ]
