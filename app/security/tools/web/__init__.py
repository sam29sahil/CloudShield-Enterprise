"""
CloudShield Enterprise
Web Security Tools
"""

import logging

from app.security.tools.web.whatweb import WhatWebTool
from app.security.tools.web.nikto import NiktoTool
from app.security.tools.web.nuclei import NucleiTool
from app.security.tools.web.gobuster import GobusterTool
from app.security.tools.web.ffuf import FFUFTool
from app.security.tools.web.dirsearch import DirsearchTool
from app.security.tools.web.sqlmap import SQLMapTool
from app.security.tools.web.zap import ZAPTool
from app.security.tools.web.dalfox import DalfoxTool
from app.security.tools.web.xsstrike import XSStrikeTool
from app.security.tools.web.wafw00f import WAFW00FTool
from app.security.tools.web.corsy import CorsyTool

logger = logging.getLogger(__name__)


def _safe_create(tool_class):
    """
    Safely create a tool instance.
    """

    try:
        return tool_class()

    except Exception as e:

        logger.exception(
            "Failed to initialize %s: %s",
            tool_class.__name__,
            e
        )

        return None


WEB_TOOLS = {
    "whatweb": _safe_create(WhatWebTool),
    "nikto": _safe_create(NiktoTool),
    "nuclei": _safe_create(NucleiTool),
    "gobuster": _safe_create(GobusterTool),
    "ffuf": _safe_create(FFUFTool),
    "dirsearch": _safe_create(DirsearchTool),
    "sqlmap": _safe_create(SQLMapTool),
    "zap": _safe_create(ZAPTool),
    "dalfox": _safe_create(DalfoxTool),
    "xsstrike": _safe_create(XSStrikeTool),
    "wafw00f": _safe_create(WAFW00FTool),
    "corsy": _safe_create(CorsyTool),
}


def get_tool(name):
    """
    Return a web tool instance.
    """

    if not name:
        return None

    return WEB_TOOLS.get(name.lower())


def tool_exists(name):
    """
    Check whether a web tool exists.
    """

    return get_tool(name) is not None


def get_all_tools():
    """
    Return all successfully initialized tools.
    """

    return {
        name: tool
        for name, tool in WEB_TOOLS.items()
        if tool is not None
    }


def tool_names():
    """
    Return all available web tool names.
    """

    return sorted(get_all_tools().keys())


__all__ = [
    "WhatWebTool",
    "NiktoTool",
    "NucleiTool",
    "GobusterTool",
    "FFUFTool",
    "DirsearchTool",
    "SQLMapTool",
    "ZAPTool",
    "DalfoxTool",
    "XSStrikeTool",
    "WAFW00FTool",
    "CorsyTool",
    "WEB_TOOLS",
    "get_tool",
    "get_all_tools",
    "tool_exists",
    "tool_names",
]