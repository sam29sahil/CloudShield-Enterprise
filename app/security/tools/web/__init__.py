"""
CloudShield Enterprise
Web Security Tools
"""

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


WEB_TOOLS = {

    "whatweb": WhatWebTool(),

    "nikto": NiktoTool(),

    "nuclei": NucleiTool(),

    "gobuster": GobusterTool(),

    "ffuf": FFUFTool(),

    "dirsearch": DirsearchTool(),

    "sqlmap": SQLMapTool(),

    "zap": ZAPTool(),

    "dalfox": DalfoxTool(),

    "xsstrike": XSStrikeTool(),

    "wafw00f": WAFW00FTool(),

    "corsy": CorsyTool()

}


def get_tool(name):

    return WEB_TOOLS.get(name.lower())


def get_all_tools():

    return WEB_TOOLS


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

    "get_all_tools"

]