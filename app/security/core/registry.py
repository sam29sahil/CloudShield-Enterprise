"""
CloudShield Enterprise
Tool Registry
"""

# ==========================================================
# Tool Categories
# ==========================================================

from app.security.tools.basic import get_all_tools as basic_tools
from app.security.tools.network import get_all_tools as network_tools
from app.security.tools.web import get_all_tools as web_tools
from app.security.tools.ssl import get_all_tools as ssl_tools
from app.security.tools.dns import get_all_tools as dns_tools
from app.security.tools.cloud import get_all_tools as cloud_tools
from app.security.tools.wireless import get_all_tools as wireless_tools


# ==========================================================
# Registry Loader
# ==========================================================

def load_registry():
    """
    Load every registered security tool.
    """

    registry = {}

    for loader in (

        basic_tools,

        network_tools,

        web_tools,

        ssl_tools,

        dns_tools,

        cloud_tools,

        wireless_tools,

    ):

        registry.update(loader())

    return registry


# ==========================================================
# Categories
# ==========================================================

CATEGORY_LOADERS = {

    "basic": basic_tools,

    "network": network_tools,

    "web": web_tools,

    "ssl": ssl_tools,

    "dns": dns_tools,

    "cloud": cloud_tools,

    "wireless": wireless_tools,

}


def get_categories():
    """
    Return available categories.
    """

    return sorted(CATEGORY_LOADERS.keys())


def get_tools(category):
    """
    Return tools for a category.
    """

    loader = CATEGORY_LOADERS.get(category.lower())

    if loader is None:

        return {}

    return loader()


def get_tool_names(category):
    """
    Return tool names for UI dropdowns.
    """

    return sorted(

        get_tools(category).keys()

    )


def tool_exists(tool):
    """
    Check if tool exists.
    """

    return tool.lower() in load_registry()


def get_tool(tool):
    """
    Return tool instance.
    """

    return load_registry().get(

        tool.lower()

    )


def registry_summary():
    """
    Enterprise dashboard summary.
    """

    registry = load_registry()

    summary = {

        "categories": {},

        "total_categories": len(CATEGORY_LOADERS),

        "total_tools": len(registry)

    }

    for category in CATEGORY_LOADERS:

        summary["categories"][category] = len(

            get_tools(category)

        )

    return summary