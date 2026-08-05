"""
CloudShield Enterprise
Security Manager
"""

from time import perf_counter

from app.security.core.normalizer import ResultParser
from app.security.core.registry import load_registry, get_categories


class SecurityManager:
    """
    Central Security Manager.

    Responsibilities:
    - Load registered security tools
    - Execute security tools
    - Normalize results
    - Provide tool metadata
    """

    def __init__(self):

        self.parser = ResultParser()
        self.registry = {}

        self.reload_tools()

    # ==========================================================
    # Registry
    # ==========================================================

    def reload_tools(self):
        """
        Reload all registered security tools.
        """

        self.registry = load_registry()

    def tools(self):
        """
        Return all registered tools.
        """

        return sorted(self.registry.keys())

    def categories(self):
        """
        Return available tool categories.
        """

        return get_categories()

    # ==========================================================
    # Tool Lookup
    # ==========================================================

    def get(self, tool):
        """
        Return tool instance.
        """

        if not tool:
            return None

        return self.registry.get(tool.lower())

    def is_registered(self, tool):
        """
        Check whether a tool exists in the registry.
        """

        if not tool:
            return False

        return tool.lower() in self.registry

    def installed(self, tool):
        """
        Check whether the tool is installed.
        """

        scanner = self.get(tool)

        if scanner is None:
            return False

        if hasattr(scanner, "installed"):
            return scanner.installed()

        return True

    # ==========================================================
    # Tool Execution
    # ==========================================================

    def run_tool(self, tool, target, arguments=None):
        """
        Execute a registered tool.
        """

        scanner = self.get(tool)

        if scanner is None:

            return {
                "success": False,
                "tool": tool,
                "error": f"'{tool}' is not registered.",
            }

        start = perf_counter()

        try:

            raw = scanner.scan(target=target, arguments=arguments)

        except Exception as e:

            raw = {"success": False, "tool": tool, "target": target, "error": str(e)}

        elapsed = round(perf_counter() - start, 2)

        print("\n" + "=" * 60)
        print(f"TOOL EXECUTED : {tool}")
        print(f"TARGET        : {target}")
        print(f"TIME          : {elapsed}s")
        print("=" * 60)
        print(raw)
        print("=" * 60 + "\n")

        parsed = self.parser.parse(
            tool=tool, target=target, result=raw, execution_time=elapsed
        )

        return parsed

    # ==========================================================
    # Future Extensions
    # ==========================================================

    def run_category(self, category, target, arguments=None):
        """
        Placeholder for future category execution.

        Example:
            run_category("web", "example.com")

        This will execute every registered web tool.
        """

        raise NotImplementedError("Category execution is not implemented yet.")
