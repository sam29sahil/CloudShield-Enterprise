"""
CloudShield Enterprise
<<<<<<< HEAD
Security Manager
"""

from time import perf_counter

from app.security.core.normalizer import ResultParser
from app.security.core.registry import load_registry, get_categories
=======
Enterprise Security Manager
"""

from time import perf_counter
import logging

from app.security.tools.common.base import BaseTool
from app.security.core.normalizer import ResultParser

from app.security.core.registry import (
    load_registry,
    get_categories,
    get_tools,
    get_tool,
    tool_exists,
)

logger = logging.getLogger(__name__)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


class SecurityManager:
    """
<<<<<<< HEAD
    Central Security Manager.

    Responsibilities:
    - Load registered security tools
    - Execute security tools
    - Normalize results
    - Provide tool metadata
=======
    Enterprise Security Manager

    Responsibilities

    • Load registry
    • Execute tools
    • Execute categories
    • Normalize results
    • Handle failures
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    """

    def __init__(self):

        self.parser = ResultParser()
<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        self.registry = {}

        self.reload_tools()

<<<<<<< HEAD
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
=======
    # =====================================================
    # Registry
    # =====================================================

    def reload_tools(self):

        self.registry = load_registry()

    def categories(self):

        return get_categories()

    def tools(self):

        return sorted(self.registry.keys())

    def get(self, tool):

        if not tool:

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            return None

        return self.registry.get(tool.lower())

<<<<<<< HEAD
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
=======
    def exists(self, tool):

        if not tool:

            return False

        return tool_exists(tool)

    def installed(self, tool):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        scanner = self.get(tool)

        if scanner is None:
<<<<<<< HEAD
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
=======

            return False

        if hasattr(scanner, "installed"):

            try:

                return scanner.installed()

            except Exception:

                return False

        return True

    # =====================================================
    # Categories
    # =====================================================

    def get_categories(self):

        return get_categories()

    def get_tools(self, category=None):

        if category is None:

            return self.tools()

        return sorted(

            get_tools(category).keys()

        )

    def get_basic_tools(self):

        return list(

            get_tools("basic").keys()

        )

    def get_category_tools(self, category):

        return list(

            get_tools(category).keys()

        )

    # =====================================================
    # Execution Adapter
    # =====================================================

    def _execute(self, scanner, target, arguments=None):

        if arguments is None:
            arguments = []

        #
        # Preferred API
        #

        if (
            hasattr(scanner, "scan")
            and callable(scanner.scan)
            and scanner.__class__.scan is not BaseTool.run
        ):
            return scanner.scan(
                target=target,
                arguments=arguments
            )

        #
        # Legacy execute()
        #

        if (
            hasattr(scanner, "execute")
            and callable(scanner.execute)
        ):
            return scanner.execute(
                target,
                arguments
            )

        #
        # Legacy check()
        #

        if (
            hasattr(scanner, "check")
            and callable(scanner.check)
        ):
            return scanner.check(
                target,
                arguments
            )

        #
        # Legacy analyze()
        #

        if (
            hasattr(scanner, "analyze")
            and callable(scanner.analyze)
        ):
            return scanner.analyze(
                target,
                arguments
            )

        #
        # Enterprise run()
        #

        if (
            hasattr(scanner, "run")
            and callable(scanner.run)
            and scanner.__class__.run is not BaseTool.run
        ):
            return scanner.run(
                target,
                arguments
            )

        raise RuntimeError(
            f"{scanner.__class__.__name__} exposes no execution method."
        )
    # =====================================================
    # Execute One Tool
    # =====================================================

    def run_tool(

        self,

        tool,

        target,

        arguments=None

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        scanner = self.get(tool)

        if scanner is None:

            return {
<<<<<<< HEAD
                "success": False,
                "tool": tool,
                "error": f"'{tool}' is not registered.",
=======

                "success": False,

                "tool": tool,

                "target": target,

                "error": "Tool not registered."

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
            }

        start = perf_counter()

        try:

<<<<<<< HEAD
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
=======
            result = self._execute(

                scanner,

                target,

                arguments

            )

        except Exception as e:

            logger.exception(e)

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

        return self.parser.parse(

            tool=tool,

            target=target,

            result=result,

            execution_time=elapsed

        )

        # =====================================================
    # Execute Multiple Tools
    # =====================================================

    def execute_tools(
        self,
        tools,
        target,
        arguments=None
    ):
        """
        Execute multiple tools and return results.
        """

        if arguments is None:
            arguments = []

        results = []

        for tool in tools:

            result = self.run_tool(
                tool=tool,
                target=target,
                arguments=arguments
            )

            results.append(result)

        return results

    # =====================================================
    # Execute Category
    # =====================================================

    def execute_category(
        self,
        category,
        target,
        arguments=None
    ):
        """
        Execute all tools belonging to a category.
        """

        if arguments is None:
            arguments = []

        tools = self.get_category_tools(category)

        return self.execute_tools(
            tools,
            target,
            arguments
        )

    # =====================================================
    # Execute Enterprise Scan
    # =====================================================

    def execute_scan(
        self,
        category,
        target,
        arguments=None
    ):
        """
        Execute one complete scan.

        Flow

            Basic Tools
                 +
          Category Tools
        """

        if arguments is None:
            arguments = []

        tools = []

        #
        # Always execute basic checks
        #

        basic = self.get_basic_tools()

        for tool in basic:

            if tool not in tools:

                tools.append(tool)

        #
        # Category tools
        #

        if category:

            category_tools = self.get_category_tools(category)

            for tool in category_tools:

                if tool not in tools:

                    tools.append(tool)

        return self.execute_tools(
            tools,
            target,
            arguments
        )

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
        Main entry used by SecurityService.

        Modes:

            quick
            standard
            deep
            enterprise
        """

        if arguments is None:
            arguments = []

        #
        # Single tool execution
        #

        if tool:

            return self.run_tool(
                tool=tool,
                target=target,
                arguments=arguments
            )

        #
        # Full category scan
        #

        return self.execute_scan(
            category=category,
            target=target,
            arguments=arguments
        )

    # =====================================================
    # Statistics
    # =====================================================

    def summary(self):

        return {

            "categories": len(self.get_categories()),

            "tools": len(self.tools()),

            "basic_tools": len(self.get_basic_tools())

        }

    # =====================================================
    # Debug
    # =====================================================

    def __repr__(self):

        return (

            "<SecurityManager "

            f"tools={len(self.registry)}>"

        )    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
