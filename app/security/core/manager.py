"""
CloudShield Enterprise
Security Manager
"""

from time import perf_counter

from app.security.core.normalizer import ResultParser
from app.security.core.registry import load_registry, get_categories


class SecurityManager:
    """
    Central Security Manager

    Responsible for:
    - Loading tool registry
    - Executing tools
    - Returning categories/tools
    - Normalizing results
    """

    def __init__(self):

        self.parser = ResultParser()
        self.registry = {}

        self.reload_tools()

    # =====================================================
    # Registry
    # =====================================================

    def reload_tools(self):

        self.registry = load_registry()

    def get_categories(self):

        return get_categories()

    def get_tools(
        self,
        category=None,
        mode="universal"
    ):

        tools = []

        for name, tool in self.registry.items():

            if category is None:

                tools.append(name)

                continue

            tool_category = getattr(
                tool,
                "category",
                None
            )

            if tool_category == category:

                tools.append(name)

        return sorted(tools)

    def tools(self):

        return sorted(self.registry.keys())

    def get(self, tool):

        if not tool:

            return None

        return self.registry.get(tool.lower())

    def is_registered(self, tool):

        return tool.lower() in self.registry

    def installed(self, tool):

        scanner = self.get(tool)

        if scanner is None:

            return False

        if hasattr(scanner, "installed"):

            return scanner.installed()

        return True

    # =====================================================
    # Main Entry
    # =====================================================

    def execute(
        self,
        user_id,
        asset_id,
        mode,
        category,
        tool,
        target,
        arguments=None
    ):
        """
        Main execution entry used by SecurityService.
        """

        if arguments is None:

            arguments = []

        if mode == "basic":

            tool = "quick_scan"

        return self.run_tool(

            tool=tool,

            target=target,

            arguments=arguments

        )

    # =====================================================
    # Tool Execution
    # =====================================================

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

                "tool": tool,

                "error": f"{tool} is not registered."

            }

        start = perf_counter()

        try:

            result = scanner.scan(

                target=target,

                arguments=arguments

            )

        except Exception as e:

            result = {

                "success": False,

                "tool": tool,

                "target": target,

                "error": str(e)

            }

        elapsed = round(

            perf_counter() - start,

            2

        )

        parsed = self.parser.parse(

            tool=tool,

            target=target,

            result=result,

            execution_time=elapsed

        )

        return parsed

    # =====================================================
    # Future
    # =====================================================

    def run_category(
        self,
        category,
        target,
        arguments=None
    ):

        raise NotImplementedError(
            "Category execution is not implemented yet."
        )