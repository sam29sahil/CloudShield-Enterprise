"""
CloudShield Enterprise
Security Manager
"""

from time import perf_counter

from app.security.parser import ResultParser

from app.security.tools.network import get_all_tools as network_tools
from app.security.tools.web import get_all_tools as web_tools
from app.security.tools.ssl import get_all_tools as ssl_tools
from app.security.tools.dns import get_all_tools as dns_tools
from app.security.tools.cloud import get_all_tools as cloud_tools
from app.security.tools.wireless import get_all_tools as wireless_tools


class SecurityManager:
    """
    Central Security Manager
    """

    def __init__(self):

        self.registry = {}
        self.parser = ResultParser()

        self.load_tools()

    def load_tools(self):

        self.registry.clear()

        self.registry.update(network_tools())
        self.registry.update(web_tools())
        self.registry.update(ssl_tools())
        self.registry.update(dns_tools())
        self.registry.update(cloud_tools())
        self.registry.update(wireless_tools())

    def tools(self):

        return sorted(self.registry.keys())

    def get(self, tool):

        if not tool:
            return None

        return self.registry.get(tool.lower())

    def installed(self, tool):

        scanner = self.get(tool)

        if scanner is None:
            return False

        if hasattr(scanner, "installed"):
            return scanner.installed()

        return True

    def run_tool(
        self,
        tool,
        target,
        arguments=None
    ):

        scanner = self.get(tool)

        if scanner is None:

            return {

                "success": False,

                "error": f"{tool} is not registered."

            }

        start = perf_counter()

        try:

            raw = scanner.scan(
                target,
                arguments
            )

        except Exception as e:

            raw = {

                "success": False,

                "error": str(e)

            }

        elapsed = perf_counter() - start

        print("\n========== RAW RESULT ==========")
        print(raw)
        print("================================\n")

        parsed = self.parser.parse(

            tool=tool,

            target=target,

            result=raw,

            execution_time=round(elapsed, 2)

        )

        return parsed

    def categories(self):

        return {

            "network": list(network_tools().keys()),

            "web": list(web_tools().keys()),

            "ssl": list(ssl_tools().keys()),

            "dns": list(dns_tools().keys()),

            "cloud": list(cloud_tools().keys()),

            "wireless": list(wireless_tools().keys())

        }