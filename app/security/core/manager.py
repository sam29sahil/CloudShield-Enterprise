"""
CloudShield Enterprise
Security Manager
"""

from time import perf_counter

from app.security.core.normalizer import ResultParser

from app.security.core.registry import load_registry


class SecurityManager:
    """
    Central Security Manager
    """

    def __init__(self):

        self.registry = {}
        self.parser = ResultParser()
        self.registry = load_registry()

        self.load_tools()

    def load_tools(self):
        self.registry = load_registry()

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