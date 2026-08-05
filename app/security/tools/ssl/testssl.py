"""
CloudShield Enterprise
TestSSL Tool
"""

from app.security.tools.common.base import BaseTool

from app.security.tools.ssl.constants import TESTSSL_DEFAULT


class TestSSLTool(BaseTool):
    """
    TestSSL Scanner
    """

    name = "testssl"

    default_arguments = TESTSSL_DEFAULT
    timeout = 300

    def protocols(self, target):

<<<<<<< HEAD
        return self.scan(target, ["--protocols"])

    def vulnerabilities(self, target):

        return self.scan(target, ["--vulnerable"])

    def certificate(self, target):

        return self.scan(target, ["--server-defaults"])

    def ciphers(self, target):

        return self.scan(target, ["--cipher-per-proto"])

    def hsts(self, target):

        return self.scan(target, ["--hsts"])

    def ocsp(self, target):

        return self.scan(target, ["--ocsp"])

    def scan_all(self, target):

        return self.scan(target, self.default_arguments)
=======
        return self.scan(

            target,

            [

                "--protocols"

            ]

        )

    def vulnerabilities(self, target):

        return self.scan(

            target,

            [

                "--vulnerable"

            ]

        )

    def certificate(self, target):

        return self.scan(

            target,

            [

                "--server-defaults"

            ]

        )

    def ciphers(self, target):

        return self.scan(

            target,

            [

                "--cipher-per-proto"

            ]

        )

    def hsts(self, target):

        return self.scan(

            target,

            [

                "--hsts"

            ]

        )

    def ocsp(self, target):

        return self.scan(

            target,

            [

                "--ocsp"

            ]

        )

    def scan_all(self, target):

        return self.scan(

            target,

            self.default_arguments

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "SSL",
            "description": "TestSSL TLS Security Scanner",
        }
=======

            "name": self.name,

            "category": "SSL",

            "description": "TestSSL TLS Security Scanner"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
