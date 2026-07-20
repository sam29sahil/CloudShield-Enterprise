"""
CloudShield Enterprise
SSLyze Tool
"""

from app.security.tools.common.base import BaseTool

from app.security.tools.ssl.constants import SSLYZE_DEFAULT


class SSLyzeTool(BaseTool):
    """
    SSLyze Scanner
    """

    name = "sslyze"

    default_arguments = SSLYZE_DEFAULT
    
    timeout = 300

    def certificate(self, target):

        return self.scan(

            target,

            [

                "--certinfo"

            ]

        )

    def protocols(self, target):

        return self.scan(

            target,

            [

                "--sslv2",

                "--sslv3",

                "--tlsv1",

                "--tlsv1_1",

                "--tlsv1_2",

                "--tlsv1_3"

            ]

        )

    def ciphers(self, target):

        return self.scan(

            target,

            [

                "--cipher_suites"

            ]

        )

    def compression(self, target):

        return self.scan(

            target,

            [

                "--compression"

            ]

        )

    def renegotiation(self, target):

        return self.scan(

            target,

            [

                "--reneg"

            ]

        )

    def session_resumption(self, target):

        return self.scan(

            target,

            [

                "--resum"

            ]

        )

    def heartbleed(self, target):

        return self.scan(

            target,

            [

                "--heartbleed"

            ]

        )

    def robot(self, target):

        return self.scan(

            target,

            [

                "--robot"

            ]

        )

    def scan_all(self, target):

        return self.scan(

            target,

            self.default_arguments

        )

    def info(self):

        return {

            "name": self.name,

            "category": "SSL",

            "description": "Enterprise SSL/TLS Security Scanner"

        }