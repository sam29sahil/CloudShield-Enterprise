"""
CloudShield Enterprise
Scan Dispatcher
"""

from app.security.integration.executor import ScanExecutor


class ScanDispatcher:
    """
    Dispatch scan requests.
    """

    def __init__(self):

        self.executor = ScanExecutor()

    def dispatch(

        self,

        tool,

        target,

        arguments=None

    ):

        return self.executor.execute(

            tool,

            target,

            arguments

        )

    def dispatch_all(

        self,

        tools,

        target

    ):

        return self.executor.execute_multiple(

            tools,

            target

        )

    def category(

        self,

        category,

        target

    ):

        groups = {

            "network": [

                "nmap",

                "rustscan",

                "masscan",

                "netdiscover"

            ],

            "web": [

                "whatweb",

                "nikto",

                "nuclei",

                "gobuster",

                "ffuf",

                "sqlmap",

                "zap",

                "dalfox",

                "xsstrike",

                "wafw00f",

                "corsy"

            ],

            "ssl": [

                "sslyze",

                "testssl",

                "openssl"

            ],

            "dns": [

                "amass",

                "subfinder",

                "assetfinder",

                "dnsrecon",

                "dnsenum",

                "fierce"

            ],

            "cloud": [

                "prowler",

                "scoutsuite",

                "cloudsplaining",

                "trivy"

            ],

            "wireless": [

                "aircrack-ng",

                "airodump-ng",

                "aireplay-ng",

                "wifite"

            ]

        }

        tools = groups.get(

            category.lower(),

            []

        )

        return self.dispatch_all(

            tools,

            target

        )