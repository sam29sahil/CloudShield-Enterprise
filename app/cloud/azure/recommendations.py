"""
CloudShield Enterprise
Azure Security Recommendations
"""


class AzureRecommendations:
    """
    Generates remediation guidance
    for Azure security findings.
    """

    RECOMMENDATIONS = {

        "Virtual Machine has a Public IP": {
            "priority": "High",
            "recommendation": (
                "Remove unnecessary public IP addresses. "
                "Use Azure Bastion, VPN Gateway, or a Load Balancer "
                "instead of exposing virtual machines directly."
            )
        },

        "Public Blob Access Enabled": {
            "priority": "Critical",
            "recommendation": (
                "Disable public blob access. "
                "Enable Private Endpoints and restrict access "
                "using Azure RBAC."
            )
        },

        "HTTPS Only Disabled": {
            "priority": "High",
            "recommendation": (
                "Enable HTTPS-only traffic to encrypt all "
                "communication with the storage account."
            )
        },

        "Allow Any/Any Rule Detected": {
            "priority": "Critical",
            "recommendation": (
                "Restrict inbound rules to trusted IP addresses. "
                "Avoid using Any/Any rules."
            )
        },

        "Soft Delete Disabled": {
            "priority": "Medium",
            "recommendation": (
                "Enable Soft Delete and Purge Protection "
                "to prevent accidental deletion of secrets."
            )
        }
    }

    def get(self, title):

        return self.RECOMMENDATIONS.get(
            title,
            {
                "priority": "Low",
                "recommendation":
                    "Review this resource according to Azure Security Best Practices."
            }
        )

    def enrich(self, findings):
        """
        Adds recommendation and priority
        to every finding.
        """

        enriched = []

        for finding in findings:

            info = self.get(finding["title"])

            item = finding.copy()

            item["priority"] = info["priority"]
            item["recommendation"] = info["recommendation"]

            enriched.append(item)

        return enriched