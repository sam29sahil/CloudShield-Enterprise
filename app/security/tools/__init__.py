"""
CloudShield Enterprise
Security Tools Package
"""

from .network import get_all_tools as network_tools
from .web import get_all_tools as web_tools
from .ssl import get_all_tools as ssl_tools
from .dns import get_all_tools as dns_tools
from .cloud import get_all_tools as cloud_tools
from .wireless import get_all_tools as wireless_tools


def get_all_categories():
    """
    Return all available tool categories.
    """
    return {
        "network": network_tools,
        "web": web_tools,
        "ssl": ssl_tools,
        "dns": dns_tools,
        "cloud": cloud_tools,
        "wireless": wireless_tools,
    }