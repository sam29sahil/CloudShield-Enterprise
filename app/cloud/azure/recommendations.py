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
<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        "Virtual Machine has a Public IP": {
            "priority": "High",
            "recommendation": (
                "Remove unnecessary public IP addresses. "
                "Use Azure Bastion, VPN Gateway, or a Load Balancer "
                "instead of exposing virtual machines directly."
<<<<<<< HEAD
            ),
        },
=======
            )
        },

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        "Public Blob Access Enabled": {
            "priority": "Critical",
            "recommendation": (
                "Disable public blob access. "
                "Enable Private Endpoints and restrict access "
                "using Azure RBAC."
<<<<<<< HEAD
            ),
        },
=======
            )
        },

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        "HTTPS Only Disabled": {
            "priority": "High",
            "recommendation": (
                "Enable HTTPS-only traffic to encrypt all "
                "communication with the storage account."
<<<<<<< HEAD
            ),
        },
=======
            )
        },

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        "Allow Any/Any Rule Detected": {
            "priority": "Critical",
            "recommendation": (
                "Restrict inbound rules to trusted IP addresses. "
                "Avoid using Any/Any rules."
<<<<<<< HEAD
            ),
        },
=======
            )
        },

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        "Soft Delete Disabled": {
            "priority": "Medium",
            "recommendation": (
                "Enable Soft Delete and Purge Protection "
                "to prevent accidental deletion of secrets."
<<<<<<< HEAD
            ),
        },
=======
            )
        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    }

    def get(self, title):

        return self.RECOMMENDATIONS.get(
            title,
            {
                "priority": "Low",
<<<<<<< HEAD
                "recommendation": "Review this resource according to Azure Security Best Practices.",
            },
=======
                "recommendation":
                    "Review this resource according to Azure Security Best Practices."
            }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
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

<<<<<<< HEAD
        return enriched
=======
        return enriched
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
