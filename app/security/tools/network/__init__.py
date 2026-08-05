"""
CloudShield Enterprise
Network Security Tools
"""

import logging

from app.security.tools.network.nmap import NmapTool
from app.security.tools.network.rustscan import RustScanTool
from app.security.tools.network.masscan import MasscanTool
from app.security.tools.network.netdiscover import NetdiscoverTool

logger = logging.getLogger(__name__)


def _safe_create(tool_class):
    """
    Safely create a tool instance.
    """

    try:
        return tool_class()

    except Exception as e:

<<<<<<< HEAD
        logger.exception("Failed to initialize %s: %s", tool_class.__name__, e)
=======
        logger.exception(
            "Failed to initialize %s: %s",
            tool_class.__name__,
            e
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        return None


NETWORK_TOOLS = {
    "nmap": _safe_create(NmapTool),
    "rustscan": _safe_create(RustScanTool),
    "masscan": _safe_create(MasscanTool),
    "netdiscover": _safe_create(NetdiscoverTool),
}


def get_tool(name):
    """
    Return a network tool instance.
    """

    if not name:
        return None

    return NETWORK_TOOLS.get(name.lower())


def tool_exists(name):
    """
    Check whether a network tool exists.
    """

    return get_tool(name) is not None


def get_all_tools():
    """
    Return all successfully initialized tools.
    """

<<<<<<< HEAD
    return {name: tool for name, tool in NETWORK_TOOLS.items() if tool is not None}
=======
    return {
        name: tool
        for name, tool in NETWORK_TOOLS.items()
        if tool is not None
    }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


def tool_names():
    """
    Return all available network tool names.
    """

    return sorted(get_all_tools().keys())


__all__ = [
    "NmapTool",
    "RustScanTool",
    "MasscanTool",
    "NetdiscoverTool",
    "NETWORK_TOOLS",
    "get_tool",
    "get_all_tools",
    "tool_exists",
    "tool_names",
<<<<<<< HEAD
]
=======
]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
