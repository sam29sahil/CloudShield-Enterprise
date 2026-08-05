"""
CloudShield Enterprise
Enterprise Nmap Tool
"""

import time
import nmap


class NmapTool:
    """
    Enterprise Nmap Scanner

    Features
    --------
    • Host Discovery
    • Service Detection
    • OS Detection
    • Version Detection
    • Enterprise Metadata
    """

    name = "nmap"

    display_name = "Nmap"

    version_required = "7.0"

    default_arguments = "-sV -T4"

    timeout = 300

    def __init__(self):

        self.scanner = None

        self.last_command = ""

        try:

            self.scanner = nmap.PortScanner()

        except Exception:

            self.scanner = None

    # ==========================================================
    # Installation
    # ==========================================================

    @staticmethod
    def installed():
        """
        Check whether Nmap is available.
        """

        try:

            nmap.PortScanner()

            return True

        except Exception:

            return False

    # ==========================================================
    # Execute Scan
    # ==========================================================

<<<<<<< HEAD
    def scan(self, target, arguments=None):
=======
    def scan(
        self,
        target,
        arguments=None
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        """
        Execute Nmap scan.
        """

        if self.scanner is None:

            return {
<<<<<<< HEAD
                "success": False,
                "tool": self.name,
                "target": target,
                "error": "Nmap is not installed.",
=======

                "success": False,

                "tool": self.name,

                "target": target,

                "error": "Nmap is not installed."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        if arguments is None:

            arguments = self.default_arguments

        elif isinstance(arguments, list):

            arguments = " ".join(arguments)

        start = time.perf_counter()

        try:

<<<<<<< HEAD
            self.scanner.scan(hosts=target, arguments=arguments)

            self.last_command = self.command()

            execution_time = round(time.perf_counter() - start, 2)

            return self.parse(target, execution_time)
=======
            self.scanner.scan(

                hosts=target,

                arguments=arguments

            )

            self.last_command = self.command()

            execution_time = round(

                time.perf_counter() - start,

                2

            )

            return self.parse(

                target,

                execution_time

            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        except Exception as e:

            return {
<<<<<<< HEAD
                "success": False,
                "tool": self.name,
                "target": target,
                "error": str(e),
            }
        # ==========================================================

    # Parse Results
    # ==========================================================

    def parse(self, target, execution_time):
=======

                "success": False,

                "tool": self.name,

                "target": target,

                "error": str(e)

            }
        # ==========================================================
    # Parse Results
    # ==========================================================

    def parse(
        self,
        target,
        execution_time
    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        """
        Parse Nmap results into the CloudShield
        Enterprise standard format.
        """

        if self.scanner is None:

            return {
<<<<<<< HEAD
                "success": False,
                "tool": self.name,
                "target": target,
                "error": "Nmap is unavailable.",
=======

                "success": False,

                "tool": self.name,

                "target": target,

                "error": "Nmap is unavailable."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        if target not in self.scanner.all_hosts():

            return {
<<<<<<< HEAD
                "success": False,
                "tool": self.name,
                "target": target,
                "error": "Host not found.",
=======

                "success": False,

                "tool": self.name,

                "target": target,

                "error": "Host not found."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        host = self.scanner[target]

        raw = {
<<<<<<< HEAD
            "hostname": host.hostname(),
            "state": host.state(),
            "ipv4": host["addresses"].get("ipv4"),
            "ipv6": host["addresses"].get("ipv6"),
            "mac": host["addresses"].get("mac"),
            "vendor": host.get("vendor", {}),
            "os": [],
            "ports": [],
=======

            "hostname": host.hostname(),

            "state": host.state(),

            "ipv4": host["addresses"].get("ipv4"),

            "ipv6": host["addresses"].get("ipv6"),

            "mac": host["addresses"].get("mac"),

            "vendor": host.get("vendor", {}),

            "os": [],

            "ports": []

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }

        # ------------------------------------------------------
        # Operating Systems
        # ------------------------------------------------------

        if "osmatch" in host:

            for operating_system in host["osmatch"]:

<<<<<<< HEAD
                raw["os"].append(
                    {
                        "name": operating_system.get("name"),
                        "accuracy": operating_system.get("accuracy"),
                    }
                )
=======
                raw["os"].append({

                    "name": operating_system.get("name"),

                    "accuracy": operating_system.get("accuracy")

                })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # ------------------------------------------------------
        # Ports
        # ------------------------------------------------------

        open_ports = 0

        for protocol in host.all_protocols():

            for port in sorted(host[protocol].keys()):

                service = host[protocol][port]

                state = service.get("state")

                if state == "open":

                    open_ports += 1

<<<<<<< HEAD
                raw["ports"].append(
                    {
                        "protocol": protocol,
                        "port": port,
                        "state": state,
                        "service": service.get("name"),
                        "product": service.get("product"),
                        "version": service.get("version"),
                        "reason": service.get("reason"),
                        "extra_info": service.get("extrainfo"),
                    }
                )
=======
                raw["ports"].append({

                    "protocol": protocol,

                    "port": port,

                    "state": state,

                    "service": service.get("name"),

                    "product": service.get("product"),

                    "version": service.get("version"),

                    "reason": service.get("reason"),

                    "extra_info": service.get("extrainfo")

                })
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        # ------------------------------------------------------
        # Security Score
        # ------------------------------------------------------

<<<<<<< HEAD
        score = max(0, 100 - (open_ports * 3))
=======
        score = max(

            0,

            100 - (open_ports * 3)

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        if open_ports == 0:

            risk = "Info"

        elif open_ports <= 5:

            risk = "Low"

        elif open_ports <= 15:

            risk = "Medium"

        else:

            risk = "High"

        # ------------------------------------------------------
        # Enterprise Result
        # ------------------------------------------------------

        return {
<<<<<<< HEAD
            "success": True,
            "tool": self.name,
            "target": target,
            "execution_time": execution_time,
            "scanner_version": self.version(),
            "command": self.last_command,
            "raw_output": raw,
            "summary": {
                "status": "Completed",
                "score": score,
                "risk": risk,
                "open_ports": open_ports,
                "hosts": 1,
            },
        }

        # ==========================================================

=======

            "success": True,

            "tool": self.name,

            "target": target,

            "execution_time": execution_time,

            "scanner_version": self.version(),

            "command": self.last_command,

            "raw_output": raw,

            "summary": {

                "status": "Completed",

                "score": score,

                "risk": risk,

                "open_ports": open_ports,

                "hosts": 1

            }

        }

        # ==========================================================
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    # Helpers
    # ==========================================================

    def hosts(self):
        """
        Return discovered hosts.
        """

        if self.scanner is None:
            return []

        try:
            return self.scanner.all_hosts()

        except Exception:
            return []

    def version(self):
        """
        Return installed Nmap version.
        """

        if self.scanner is None:
            return "Not Installed"

        try:

            version = self.scanner.nmap_version()

<<<<<<< HEAD
            return ".".join(map(str, version))
=======
            return ".".join(
                map(str, version)
            )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        except Exception:

            return "Unknown"

    def command(self):
        """
        Return executed command line.
        """

        if self.scanner is None:
            return ""

        try:
            return self.scanner.command_line()

        except Exception:
            return ""

    # ==========================================================
    # Metadata
    # ==========================================================

    def info(self):
        """
        Tool information.
        """

        return {
<<<<<<< HEAD
            "name": self.name,
            "display_name": self.display_name,
            "installed": self.installed(),
            "version": self.version(),
            "timeout": self.timeout,
            "default_arguments": self.default_arguments,
=======

            "name": self.name,

            "display_name": self.display_name,

            "installed": self.installed(),

            "version": self.version(),

            "timeout": self.timeout,

            "default_arguments": self.default_arguments

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        }


def get_tool():
    """
    Return Nmap Tool instance.
    """

<<<<<<< HEAD
    return NmapTool()
=======
    return NmapTool()    

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
