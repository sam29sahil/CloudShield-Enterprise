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
<<<<<<< HEAD
        "website": WebsiteScanner(),
        "headers": HeaderScanner(),
        "ssl": SSLScanner(),
        "dns": DNSScanner(),
        "whois": WhoisScanner(),
        "ports": PortScanner(),
        "technology": TechnologyScanner(),
    }
=======

        "website": WebsiteScanner(),

        "headers": HeaderScanner(),

        "ssl": SSLScanner(),

        "dns": DNSScanner(),

        "whois": WhoisScanner(),

        "ports": PortScanner(),

        "technology": TechnologyScanner()

    }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
