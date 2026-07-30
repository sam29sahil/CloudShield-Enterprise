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

    registry.update(basic_tools())
    registry.update(network_tools())
    registry.update(web_tools())
    registry.update(ssl_tools())
    registry.update(dns_tools())
    registry.update(cloud_tools())
    registry.update(wireless_tools())

    return registry


# ==========================================================
# Categories
# ==========================================================

CATEGORIES = {
    "basic": list(basic_tools().keys()),
    "network": list(network_tools().keys()),
    "web": list(web_tools().keys()),
    "ssl": list(ssl_tools().keys()),
    "dns": list(dns_tools().keys()),
    "cloud": list(cloud_tools().keys()),
    "wireless": list(wireless_tools().keys()),
}


def get_categories():
    """
    Return all registered categories.
    """

    return CATEGORIES


# ==========================================================
# Helper Functions
# ==========================================================

def get_tools(category):
    """
    Return all tools for a category.
    """

    return CATEGORIES.get(category.lower(), [])


def tool_exists(tool):
    """
    Check if a tool is registered.
    """

    return tool.lower() in load_registry()