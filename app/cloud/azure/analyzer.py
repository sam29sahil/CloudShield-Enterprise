"""
CloudShield Enterprise
Azure Security Analyzer
"""

from typing import Dict, List


class AzureSecurityAnalyzer:
    """
    Analyze Azure resources and generate security findings.
    """

    def analyze_virtual_machines(self, virtual_machines: List[Dict]) -> List[Dict]:

        findings = []

        for vm in virtual_machines:

            # Public IP
            if vm.get("public_ip"):
                findings.append(
                    {
                        "resource": vm.get("name"),
                        "service": "Virtual Machine",
                        "severity": "High",
                        "title": "Virtual Machine has a Public IP",
                        "description": "This virtual machine is directly accessible from the Internet.",
                        "recommendation": "Use a private IP or restrict access using an NSG.",
                    }
                )

            # Power State
            if vm.get("power_state") == "running":
                findings.append(
                    {
                        "resource": vm.get("name"),
                        "service": "Virtual Machine",
                        "severity": "Info",
                        "title": "Virtual Machine Running",
                        "description": "The virtual machine is currently running.",
                        "recommendation": "Ensure the VM is required and patched regularly.",
                    }
                )

        return findings

    def analyze_storage(self, storage_accounts: List[Dict]) -> List[Dict]:

        findings = []

        for storage in storage_accounts:

            if storage.get("public_access"):

                findings.append(
                    {
                        "resource": storage.get("name"),
                        "service": "Storage Account",
                        "severity": "Critical",
                        "title": "Public Blob Access Enabled",
                        "description": "Public access is enabled for this storage account.",
                        "recommendation": "Disable public blob access and use Private Endpoints.",
                    }
                )

            if not storage.get("https_only", True):

                findings.append(
                    {
                        "resource": storage.get("name"),
                        "service": "Storage Account",
                        "severity": "High",
                        "title": "HTTPS Only Disabled",
                        "description": "The storage account allows insecure HTTP connections.",
                        "recommendation": "Enable HTTPS-only traffic.",
                    }
                )

        return findings

    def analyze_network_security_groups(self, groups: List[Dict]) -> List[Dict]:

        findings = []

        for group in groups:

            if group.get("allow_any_any"):

                findings.append(
                    {
                        "resource": group.get("name"),
                        "service": "Network Security Group",
                        "severity": "Critical",
                        "title": "Allow Any/Any Rule Detected",
                        "description": "A rule allows unrestricted inbound access.",
                        "recommendation": "Restrict inbound rules to trusted IP ranges.",
                    }
                )

        return findings

    def analyze_keyvault(self, vaults: List[Dict]) -> List[Dict]:

        findings = []

        for vault in vaults:

            if not vault.get("soft_delete", True):

                findings.append(
                    {
                        "resource": vault.get("name"),
                        "service": "Key Vault",
                        "severity": "Medium",
                        "title": "Soft Delete Disabled",
                        "description": "Soft Delete protection is disabled.",
                        "recommendation": "Enable Soft Delete to protect secrets from accidental deletion.",
                    }
                )

        return findings

    def analyze(self, azure_data: Dict) -> List[Dict]:
        """
        Run all Azure security checks.
        """

        findings = []

        findings.extend(
            self.analyze_virtual_machines(azure_data.get("virtual_machines", []))
        )

        findings.extend(self.analyze_storage(azure_data.get("storage_accounts", [])))

        findings.extend(
            self.analyze_network_security_groups(
                azure_data.get("network_security_groups", [])
            )
        )

        findings.extend(self.analyze_keyvault(azure_data.get("keyvaults", [])))

        return findings
