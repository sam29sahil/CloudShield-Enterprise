"""
CloudShield Enterprise
SSL Security Tools
"""

from app.security.tools.ssl.sslyze import SSLyzeTool
from app.security.tools.ssl.testssl import TestSSLTool
from app.security.tools.ssl.openssl import OpenSSLTool

<<<<<<< HEAD
SSL_TOOLS = {"sslyze": SSLyzeTool(), "testssl": TestSSLTool(), "openssl": OpenSSLTool()}
=======

SSL_TOOLS = {

    "sslyze": SSLyzeTool(),

    "testssl": TestSSLTool(),

    "openssl": OpenSSLTool()

}
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


def get_tool(name):

    return SSL_TOOLS.get(name.lower())


def get_all_tools():

    return SSL_TOOLS


__all__ = [
<<<<<<< HEAD
    "SSLyzeTool",
    "TestSSLTool",
    "OpenSSLTool",
    "SSL_TOOLS",
    "get_tool",
    "get_all_tools",
]
=======

    "SSLyzeTool",

    "TestSSLTool",

    "OpenSSLTool",

    "SSL_TOOLS",

    "get_tool",

    "get_all_tools"

]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
