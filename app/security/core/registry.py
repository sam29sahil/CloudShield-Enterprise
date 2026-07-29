"""
CloudShield Enterprise
Tool Registry
"""

from app.security.tools.network import get_all_tools as network_tools
from app.security.tools.web import get_all_tools as web_tools
from app.security.tools.ssl import get_all_tools as ssl_tools
from app.security.tools.dns import get_all_tools as dns_tools
from app.security.tools.cloud import get_all_tools as cloud_tools
from app.security.tools.wireless import get_all_tools as wireless_tools


def load_registry():
    registry = {}

    registry.update(network_tools())
    registry.update(web_tools())
    registry.update(ssl_tools())
    registry.update(dns_tools())
    registry.update(cloud_tools())
    registry.update(wireless_tools())

    return registry