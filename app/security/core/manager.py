"""
CloudShield Enterprise
Enterprise Security Manager
"""

from time import perf_counter
import logging

from app.security.core.normalizer import ResultParser

from app.security.core.registry import (
    load_registry,
    get_categories,
    get_tools,
    get_tool,
    tool_exists,
)

logger = logging.getLogger(__name__)


class SecurityManager:
    """
    Enterprise Security Manager

    Responsibilities

    • Load registry
    • Execute tools
    • Execute categories
    • Normalize results
    • Handle failures
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

    def categories(self):

        return get_categories()

    def tools(self):

        return sorted(self.registry.keys())

    def get(self, tool):

        if not tool:

            return None

        return self.registry.get(tool.lower())

    def exists(self, tool):

        if not tool:

            return False

        return tool_exists(tool)

    def installed(self, tool):

        scanner = self.get(tool)

        if scanner is None:

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
        # New API
        #

        if hasattr(scanner, "run"):

            return scanner.run(

                target,

                arguments

            )

        #
        # Existing APIs
        #

        if hasattr(scanner, "scan"):

            return scanner.scan(

                target=target,

                arguments=arguments

            )

        if hasattr(scanner, "execute"):

            return scanner.execute(

                target,

                arguments

            )

        if hasattr(scanner, "check"):

            return scanner.check(

                target,

                arguments

            )

        if hasattr(scanner, "analyze"):

            return scanner.analyze(

                target,

                arguments

            )

        raise RuntimeError(

            f"{scanner.__class__.__name__} "

            "does not expose "

            "run(), scan(), execute(), "

            "check() or analyze()."

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

        scanner = self.get(tool)

        if scanner is None:

            return {

                "success": False,

                "tool": tool,

                "target": target,

                "error": "Tool not registered."

            }

        start = perf_counter()

        try:

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