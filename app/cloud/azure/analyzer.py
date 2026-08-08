"""
CloudShield Enterprise
Azure Security Analyzer
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


class AzureAnalyzer:
    """
    Azure Security Analysis Engine

    This class analyzes Azure inventory collected by the
    CloudShield Azure inventory modules and generates
    standardized security findings.

    It does NOT communicate with Azure.
    """

    def __init__(self):

        self.findings = []

    # --------------------------------------------------
    # Public Entry Point
    # --------------------------------------------------

    def analyze(self, inventory: dict):
        """
        Analyze Azure inventory.
        """

        self.findings = []
        
        print("VM DATA TYPE:", type(inventory.get("virtual_machines")))
        print("VM DATA:", inventory.get("virtual_machines"))

        self.analyze_virtual_machines(inventory.get("virtual_machines", []))

        self.analyze_network(inventory.get("network", {}))

        self.analyze_keyvault(inventory.get("keyvault", []))

        self.analyze_defender(inventory.get("defender", {}))

        logger.info("Generated %s findings.", len(self.findings))

        return self.findings
        # --------------------------------------------------

    # Finding Helper
    # --------------------------------------------------

    def add_finding(
        self,
        rule_id,
        severity,
        category,
        resource,
        title,
        description,
        recommendation,
        reference="Microsoft Azure Security Benchmark",
    ):

        self.findings.append(
            {
                "id": rule_id,
                "severity": severity,
                "category": category,
                "resource": resource,
                "title": title,
                "description": description,
                "recommendation": recommendation,
                "reference": reference,
            }
        )

        # --------------------------------------------------

    # Virtual Machines
    # --------------------------------------------------

    # --------------------------------------------------
    # Virtual Machines
    # --------------------------------------------------

    def analyze_virtual_machines(self, virtual_machines):

        logger.info("Analyzing %s virtual machines...", len(virtual_machines))
        print(type(virtual_machines))
        for vm in virtual_machines:

            resource = vm.get("name", "Unknown Virtual Machine")

            # ------------------------------------------
            # Public IP
            # ------------------------------------------

            if vm.get("public_ip"):

                self.add_finding(
                    rule_id="AZ-VM-001",
                    severity="High",
                    category="Virtual Machine",
                    resource=resource,
                    title="Virtual Machine has Public IP",
                    description=(
                        "The virtual machine is directly "
                        "reachable from the Internet."
                    ),
                    recommendation=(
                        "Remove the Public IP or restrict "
                        "access using a Network Security Group."
                    ),
                )

            # ------------------------------------------
            # Managed Identity
            # ------------------------------------------

            if not vm.get("managed_identity", False):

                self.add_finding(
                    rule_id="AZ-VM-002",
                    severity="Medium",
                    category="Virtual Machine",
                    resource=resource,
                    title="Managed Identity Disabled",
                    description=(
                        "The virtual machine does not use " "Azure Managed Identity."
                    ),
                    recommendation=(
                        "Enable a System Assigned or User " "Assigned Managed Identity."
                    ),
                )

            # ------------------------------------------
            # Boot Diagnostics
            # ------------------------------------------

            if not vm.get("boot_diagnostics", False):

                self.add_finding(
                    rule_id="AZ-VM-003",
                    severity="Low",
                    category="Virtual Machine",
                    resource=resource,
                    title="Boot Diagnostics Disabled",
                    description=("Boot diagnostics are disabled."),
                    recommendation=(
                        "Enable Azure Boot Diagnostics " "for troubleshooting."
                    ),
                )

            # ------------------------------------------
            # Power State
            # ------------------------------------------

            power = str(vm.get("power_state", "")).lower()

            if "stopped" in power:

                self.add_finding(
                    rule_id="AZ-VM-004",
                    severity="Info",
                    category="Virtual Machine",
                    resource=resource,
                    title="Virtual Machine Stopped",
                    description=("The virtual machine is currently stopped."),
                    recommendation=(
                        "Review whether the VM is still required "
                        "or can be deallocated."
                    ),
                )

            # ------------------------------------------
            # OS Disk
            # ------------------------------------------

            disk = vm.get("os_disk", {})

            if disk:

                if not disk.get("managed", True):

                    self.add_finding(
                        rule_id="AZ-VM-005",
                        severity="Medium",
                        category="Virtual Machine",
                        resource=resource,
                        title="Unmanaged OS Disk",
                        description=(
                            "The virtual machine uses an " "unmanaged OS disk."
                        ),
                        recommendation=("Migrate to Azure Managed Disks."),
                    )

    # --------------------------------------------------
    # Network
    # --------------------------------------------------

    # --------------------------------------------------
    # Network Security
    # --------------------------------------------------

    def analyze_network(self, network):

        logger.info("Analyzing Azure Network...")

        # Network data may be passed as a dictionary with sections
        if isinstance(network, dict):

            network_security_groups = network.get("network_security_groups", [])

            network_interfaces = network.get("network_interfaces", [])

        else:

            network_security_groups = []

            network_interfaces = []

        # ------------------------------------------
        # NSG Rules
        # ------------------------------------------

        for nsg in network_security_groups:

            nsg_name = nsg.get("name", "Unknown NSG")

            for rule in nsg.get("rules", []):

                source = str(rule.get("source", "")).lower()

                port = str(rule.get("destination_port", ""))

                access = str(rule.get("access", "")).lower()

                direction = str(rule.get("direction", "")).lower()

                protocol = str(rule.get("protocol", "")).lower()

                if access != "allow":

                    continue

                if direction != "inbound":

                    continue

                # ----------------------------------
                # SSH
                # ----------------------------------

                if port == "22":

                    self.add_finding(
                        rule_id="AZ-NET-001",
                        severity="High",
                        category="Network",
                        resource=nsg_name,
                        title="SSH Port Open",
                        description=(
                            "SSH (22) is allowed by a " "Network Security Group."
                        ),
                        recommendation=(
                            "Restrict SSH access to " "trusted IP addresses."
                        ),
                    )

                # ----------------------------------
                # RDP
                # ----------------------------------

                if port == "3389":

                    self.add_finding(
                        rule_id="AZ-NET-002",
                        severity="High",
                        category="Network",
                        resource=nsg_name,
                        title="RDP Port Open",
                        description=("Remote Desktop (3389) " "is exposed."),
                        recommendation=("Restrict RDP access or " "use Azure Bastion."),
                    )

                # ----------------------------------
                # Any / Any Rule
                # ----------------------------------

                if source in ("*", "internet", "0.0.0.0/0") and port == "*":

                    self.add_finding(
                        rule_id="AZ-NET-003",
                        severity="Critical",
                        category="Network",
                        resource=nsg_name,
                        title="Overly Permissive NSG Rule",
                        description=("Inbound traffic from " "any source is allowed."),
                        recommendation=("Restrict the source " "addresses and ports."),
                    )

        # ------------------------------------------
        # Network Interfaces
        # ------------------------------------------

        for nic in network_interfaces:

            if nic.get("public_ip"):

                self.add_finding(
                    rule_id="AZ-NET-004",
                    severity="High",
                    category="Network",
                    resource=nic.get("name", "NIC"),
                    title="Public Network Interface",
                    description=("The network interface has " "a public IP address."),
                    recommendation=("Remove unnecessary public IP " "addresses."),
                )

    # --------------------------------------------------
    # Key Vault
    # --------------------------------------------------

    # --------------------------------------------------
    # Key Vault
    # --------------------------------------------------

    def analyze_keyvault(self, vaults):

        logger.info("Analyzing %s Key Vault(s)...", len(vaults))

        for vault in vaults:

            resource = vault.get("name", "Unknown Key Vault")

            # ------------------------------------------
            # Soft Delete
            # ------------------------------------------

            if not vault.get("soft_delete", False):

                self.add_finding(
                    rule_id="AZ-KV-001",
                    severity="Critical",
                    category="Key Vault",
                    resource=resource,
                    title="Soft Delete Disabled",
                    description=("Azure Key Vault Soft Delete " "is disabled."),
                    recommendation=(
                        "Enable Soft Delete to "
                        "protect secrets from "
                        "accidental deletion."
                    ),
                )

            # ------------------------------------------
            # Purge Protection
            # ------------------------------------------

            if not vault.get("purge_protection", False):

                self.add_finding(
                    rule_id="AZ-KV-002",
                    severity="High",
                    category="Key Vault",
                    resource=resource,
                    title="Purge Protection Disabled",
                    description=("Purge Protection is disabled."),
                    recommendation=(
                        "Enable Purge Protection " "to prevent permanent deletion."
                    ),
                )

            # ------------------------------------------
            # Public Network Access
            # ------------------------------------------

            if str(vault.get("public_network_access", "")).lower() == "enabled":

                self.add_finding(
                    rule_id="AZ-KV-003",
                    severity="High",
                    category="Key Vault",
                    resource=resource,
                    title="Public Network Access Enabled",
                    description=("Key Vault can be reached " "from public networks."),
                    recommendation=(
                        "Disable public network "
                        "access or restrict it "
                        "using firewall rules."
                    ),
                )

            # ------------------------------------------
            # Private Endpoints
            # ------------------------------------------

            if vault.get("private_endpoints", 0) == 0:

                self.add_finding(
                    rule_id="AZ-KV-004",
                    severity="Medium",
                    category="Key Vault",
                    resource=resource,
                    title="No Private Endpoint",
                    description=("No Azure Private Endpoint " "is configured."),
                    recommendation=(
                        "Configure a Private Endpoint " "for secure access."
                    ),
                )

            # ------------------------------------------
            # RBAC
            # ------------------------------------------

            if not vault.get("rbac_authorization", False):

                self.add_finding(
                    rule_id="AZ-KV-005",
                    severity="Medium",
                    category="Key Vault",
                    resource=resource,
                    title="RBAC Authorization Disabled",
                    description=("Azure RBAC is not used " "for Key Vault access."),
                    recommendation=(
                        "Use Azure RBAC instead "
                        "of legacy access policies "
                        "where appropriate."
                    ),
                )

    # --------------------------------------------------
    # Defender
    # --------------------------------------------------

    # --------------------------------------------------
    # Microsoft Defender for Cloud
    # --------------------------------------------------

    def analyze_defender(self, defender):

        logger.info("Analyzing Microsoft Defender...")

        if not isinstance(defender, dict) or not defender:

            return

        # ------------------------------------------
        # Secure Score
        # ------------------------------------------

        score = defender.get("secure_score", {})

        if isinstance(score, dict):
            percentage = score.get("percentage", 0)
        else:
            percentage = score if isinstance(score, (int, float)) else 0

        try:
            percentage = float(percentage)
        except (TypeError, ValueError):
            percentage = 0

        if percentage < 50:

            self.add_finding(
                rule_id="AZ-DEF-001",
                severity="High",
                category="Microsoft Defender",
                resource="Subscription",
                title="Low Secure Score",
                description=(f"Azure Secure Score is only {percentage}%."),
                recommendation=(
                    "Implement Microsoft Defender "
                    "recommendations to improve "
                    "your security posture."
                ),
            )

        # ------------------------------------------
        # Active Alerts
        # ------------------------------------------

        alerts = defender.get("alerts", {})

        if isinstance(alerts, dict):
            alert_list = alerts.get("data", [])
        elif isinstance(alerts, list):
            alert_list = alerts
        else:
            alert_list = []

        if not isinstance(alert_list, list):
            alert_list = []

        for alert in alert_list:

            if not isinstance(alert, dict):
                continue

            self.add_finding(
                rule_id="AZ-DEF-002",
                severity=alert.get("severity", "High"),
                category="Microsoft Defender",
                resource=alert.get("resource", "Unknown Resource"),
                title=alert.get("name", "Active Security Alert"),
                description=(
                    "Microsoft Defender reported " "an active security alert."
                ),
                recommendation=("Investigate and remediate " "the security alert."),
            )

        # ------------------------------------------
        # Security Recommendations
        # ------------------------------------------

        recommendations = defender.get(
            "recommendations",
            [],
        )

        if isinstance(recommendations, dict):
            recommendation_list = recommendations.get(
                "data",
                [],
            )
        elif isinstance(recommendations, list):
            recommendation_list = recommendations
        else:
            # Azure Defender may return a numeric count
            # instead of the actual recommendation list.
            recommendation_list = []

        if not isinstance(recommendation_list, list):
            recommendation_list = []

        if len(recommendation_list) > 20:

            self.add_finding(
                rule_id="AZ-DEF-003",
                severity="Medium",
                category="Microsoft Defender",
                resource="Subscription",
                title="Large Number of Recommendations",
                description=(
                    f"There are {len(recommendation_list)} "
                    "security recommendations."
                ),
                recommendation=(
                    "Review and implement Microsoft Defender "
                    "recommendations."
                ),
            )
