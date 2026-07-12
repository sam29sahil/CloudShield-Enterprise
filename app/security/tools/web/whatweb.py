"""
CloudShield Enterprise
WhatWeb Tool
"""

from app.security.tools.common.base import BaseTool


class WhatWebTool(BaseTool):
    """
    WhatWeb Wrapper
    """

    name = "whatweb"

    default_arguments = [

        "--color=never",

        "--log-json=-"

    ]

    timeout = 300


def get_tool():
    """
    Return WhatWeb tool instance.
    """
    return WhatWebTool()