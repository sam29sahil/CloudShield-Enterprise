"""
CloudShield Enterprise
SSL Security Tools
"""

from app.security.tools.ssl.sslyze import SSLyzeTool
from app.security.tools.ssl.testssl import TestSSLTool
from app.security.tools.ssl.openssl import OpenSSLTool


SSL_TOOLS = {

    "sslyze": SSLyzeTool(),

    "testssl": TestSSLTool(),

    "openssl": OpenSSLTool()

}


def get_tool(name):

    return SSL_TOOLS.get(name.lower())


def get_all_tools():

    return SSL_TOOLS


__all__ = [

    "SSLyzeTool",

    "TestSSLTool",

    "OpenSSLTool",

    "SSL_TOOLS",

    "get_tool",

    "get_all_tools"

]