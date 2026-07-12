"""
CloudShield Enterprise
Nmap Tool
"""

import nmap


class NmapTool:
    """
    Enterprise Nmap Scanner
    """

    name = "nmap"

    default_arguments = "-sV -T4"

    timeout = 300

    def __init__(self):

        self.scanner = None

        try:

            self.scanner = nmap.PortScanner()

        except Exception:

            self.scanner = None

    def scan(
        self,
        target,
        arguments=None
    ):

        if self.scanner is None:

            return {

                "success": False,

                "error": "Nmap is not installed."

            }

        if arguments is None:

            arguments = self.default_arguments

        elif isinstance(arguments, list):

            arguments = " ".join(arguments)

        try:

            self.scanner.scan(

                hosts=target,

                arguments=arguments

            )

            return self.parse(target)

        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }

    def parse(
        self,
        target
    ):

        if self.scanner is None:

            return {

                "success": False,

                "error": "Nmap is not available."

            }

        if target not in self.scanner.all_hosts():

            return {

                "success": False,

                "error": "Host not found."

            }

        host = self.scanner[target]

        result = {

            "success": True,

            "tool": self.name,

            "target": target,

            "hostname": host.hostname(),

            "state": host.state(),

            "ipv4": host["addresses"].get("ipv4"),

            "ipv6": host["addresses"].get("ipv6"),

            "mac": host["addresses"].get("mac"),

            "vendor": host.get("vendor", {}),

            "os": [],

            "ports": []

        }

        if "osmatch" in host:

            for os in host["osmatch"]:

                result["os"].append({

                    "name": os.get("name"),

                    "accuracy": os.get("accuracy")

                })

        for protocol in host.all_protocols():

            for port in sorted(host[protocol].keys()):

                service = host[protocol][port]

                result["ports"].append({

                    "protocol": protocol,

                    "port": port,

                    "state": service.get("state"),

                    "service": service.get("name"),

                    "product": service.get("product"),

                    "version": service.get("version"),

                    "extrainfo": service.get("extrainfo"),

                    "reason": service.get("reason")

                })

        return result

    def hosts(self):

        if self.scanner is None:

            return []

        return self.scanner.all_hosts()

    def version(self):

        if self.scanner is None:

            return "Not Installed"

        try:

            version = self.scanner.nmap_version()

            return ".".join(map(str, version))

        except Exception:

            return "Unknown"

    def command(self):

        if self.scanner is None:

            return ""

        try:

            return self.scanner.command_line()

        except Exception:

            return ""

    def installed(self):

        return self.scanner is not None

    def info(self):

        return {

            "name": self.name,

            "installed": self.installed(),

            "version": self.version(),

            "timeout": self.timeout

        }


def get_tool():
    """
    Return Nmap tool instance.
    """

    return NmapTool()