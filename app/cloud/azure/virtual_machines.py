"""
CloudShield Enterprise
Azure Virtual Machines
"""

<<<<<<< HEAD
from __future__ import annotations

import logging
from time import perf_counter

from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient

logger = logging.getLogger(__name__)


class AzureVirtualMachines:
    """
    Azure Virtual Machine Inventory Service
    """
=======
from azure.mgmt.compute import ComputeManagementClient


class AzureVirtualMachines:
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def __init__(self, client):

        self.client = client

<<<<<<< HEAD
        self.compute = ComputeManagementClient(
            credential=self.client.get_credential(),
            subscription_id=self.client.subscription(),
        )

        self.network = NetworkManagementClient(
            credential=self.client.get_credential(),
            subscription_id=self.client.subscription(),
        )

    # -------------------------------------------------------
    # Helpers
    # -------------------------------------------------------

    @staticmethod
    def resource_group(resource_id: str) -> str:

        try:

            return resource_id.split("/")[4]

        except Exception:

            return "-"

    @staticmethod
    def power_state(instance_view):

        try:

            for status in instance_view.statuses:

                if status.code.startswith("PowerState/"):

                    return status.display_status

        except Exception:

            pass

        return "Unknown"

    @staticmethod
    def provisioning_state(instance_view):

        try:

            for status in instance_view.statuses:

                if status.code.startswith("ProvisioningState/"):

                    return status.display_status

        except Exception:

            pass

        return "Unknown"

    # -------------------------------------------------------
    # Inventory
    # -------------------------------------------------------
=======
    # -------------------------------------
    # List Virtual Machines
    # -------------------------------------
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def list(self):

        if not self.client.is_connected():

<<<<<<< HEAD
            return {
                "success": False,
                "count": 0,
                "data": [],
                "execution_time": 0,
                "error": "Azure client is not connected.",
            }

        started = perf_counter()

        inventory = []

        try:

            logger.info("Collecting Azure Virtual Machines...")

            for vm in self.compute.virtual_machines.list_all():

                resource_group = self.resource_group(vm.id)

                try:

                    instance = self.compute.virtual_machines.instance_view(
                        resource_group, vm.name
                    )

                except Exception:

                    instance = None

                inventory.append(
                    {
                        "id": vm.id,
                        "name": vm.name,
                        "resource_group": resource_group,
                        "location": vm.location,
                        "type": vm.type,
                        "vm_size": (
                            vm.hardware_profile.vm_size if vm.hardware_profile else "-"
                        ),
                        "power_state": self.power_state(instance),
                        "provisioning_state": self.provisioning_state(instance),
                        "zones": vm.zones or [],
                        "tags": vm.tags or {},
                        "network_interfaces": (
                            vm.network_profile.network_interfaces
                            if vm.network_profile
                            else []
                        ),
                        "identity": vm.identity,
                        "diagnostics": vm.diagnostics_profile,
                        "storage_profile": vm.storage_profile,
                    }
                )
                # ------------------------------------------
                # Network Interfaces
                # ------------------------------------------

                private_ip = None
                public_ip = None
                subnet = None
                mac_address = None
                nic_name = None

                try:

                    if vm.network_profile and vm.network_profile.network_interfaces:

                        nic_reference = vm.network_profile.network_interfaces[0]

                        nic_name = nic_reference.id.split("/")[-1]

                        nic = self.network.network_interfaces.get(
                            resource_group, nic_name
                        )

                        mac_address = nic.mac_address

                        if nic.ip_configurations:

                            config = nic.ip_configurations[0]

                            private_ip = config.private_ip_address

                            if config.subnet:

                                subnet = config.subnet.id.split("/")[-1]

                            if config.public_ip_address:

                                public_ip = config.public_ip_address.id

                except Exception as error:

                    logger.debug(
                        "Unable to collect NIC information for %s : %s", vm.name, error
                    )

                # ------------------------------------------
                # Managed Identity
                # ------------------------------------------

                managed_identity = False

                identity_type = "-"

                if vm.identity:

                    managed_identity = True

                    identity_type = vm.identity.type

                # ------------------------------------------
                # Boot Diagnostics
                # ------------------------------------------

                boot_diagnostics = False

                try:

                    if (
                        vm.diagnostics_profile
                        and vm.diagnostics_profile.boot_diagnostics
                    ):

                        boot_diagnostics = bool(
                            vm.diagnostics_profile.boot_diagnostics.enabled
                        )

                except Exception:

                    pass

                # ------------------------------------------
                # Storage
                # ------------------------------------------

                os_disk = {}

                data_disks = []

                try:

                    if vm.storage_profile:

                        if vm.storage_profile.os_disk:

                            disk = vm.storage_profile.os_disk

                            os_disk = {
                                "name": disk.name,
                                "os_type": str(disk.os_type),
                                "caching": str(disk.caching),
                                "managed": disk.managed_disk is not None,
                            }

                        if vm.storage_profile.data_disks:

                            for disk in vm.storage_profile.data_disks:

                                data_disks.append(
                                    {
                                        "name": disk.name,
                                        "lun": disk.lun,
                                        "size_gb": disk.disk_size_gb,
                                        "managed": disk.managed_disk is not None,
                                    }
                                )

                except Exception:

                    pass

                # ------------------------------------------
                # Final Inventory Record
                # ------------------------------------------

                inventory.append(
                    {
                        "id": vm.id,
                        "name": vm.name,
                        "resource_group": resource_group,
                        "location": vm.location,
                        "type": vm.type,
                        "vm_size": (
                            vm.hardware_profile.vm_size if vm.hardware_profile else "-"
                        ),
                        "power_state": self.power_state(instance),
                        "provisioning_state": self.provisioning_state(instance),
                        "zones": vm.zones or [],
                        "tags": vm.tags or {},
                        "private_ip": private_ip,
                        "public_ip": public_ip,
                        "subnet": subnet,
                        "nic": nic_name,
                        "mac_address": mac_address,
                        "managed_identity": managed_identity,
                        "identity_type": identity_type,
                        "boot_diagnostics": boot_diagnostics,
                        "os_disk": os_disk,
                        "data_disks": data_disks,
                    }
                )

            logger.info("Collected %s Azure Virtual Machines.", len(inventory))

            return {
                "success": True,
                "count": len(inventory),
                "data": inventory,
                "execution_time": round(perf_counter() - started, 3),
                "error": "",
            }

        except Exception as error:

            logger.exception("Azure VM inventory failed: %s", error)

            return {
                "success": False,
                "count": 0,
                "data": [],
                "execution_time": round(perf_counter() - started, 3),
                "error": str(error),
            }
=======
            return []

        try:

            compute = ComputeManagementClient(

                credential=self.client.get_credential(),

                subscription_id=self.client.subscription()

            )

            virtual_machines = []

            for vm in compute.virtual_machines.list_all():

                virtual_machines.append(

                    {

                        "name": vm.name,

                        "location": vm.location,

                        "type": vm.type,

                        "id": vm.id

                    }

                )

            return virtual_machines

        except Exception:

            return []
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
