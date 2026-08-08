"""
CloudShield Enterprise
Basic Security Tools
"""

from .website import WebsiteScanner
from .headers import HeaderScanner
from .ssl_scanner import SSLScanner
from .dns import DNSScanner
from .whois import WhoisScanner
from .ports import PortScanner
from .technology import TechnologyScanner


def get_all_tools():

    return {

        "website": WebsiteScanner(),

        "headers": HeaderScanner(),

        "ssl": SSLScanner(),

        "dns": DNSScanner(),

        "whois": WhoisScanner(),

        "ports": PortScanner(),

        "technology": TechnologyScanner()

    }