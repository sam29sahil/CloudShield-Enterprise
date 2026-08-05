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
<<<<<<< HEAD

=======
    
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    timeout = 300

    def certificate(self, target):

<<<<<<< HEAD
        return self.scan(target, ["--certinfo"])
=======
        return self.scan(

            target,

            [

                "--certinfo"

            ]

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def protocols(self, target):

        return self.scan(
<<<<<<< HEAD
            target,
            ["--sslv2", "--sslv3", "--tlsv1", "--tlsv1_1", "--tlsv1_2", "--tlsv1_3"],
=======

            target,

            [

                "--sslv2",

                "--sslv3",

                "--tlsv1",

                "--tlsv1_1",

                "--tlsv1_2",

                "--tlsv1_3"

            ]

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

    def ciphers(self, target):

<<<<<<< HEAD
        return self.scan(target, ["--cipher_suites"])

    def compression(self, target):

        return self.scan(target, ["--compression"])

    def renegotiation(self, target):

        return self.scan(target, ["--reneg"])

    def session_resumption(self, target):

        return self.scan(target, ["--resum"])

    def heartbleed(self, target):

        return self.scan(target, ["--heartbleed"])

    def robot(self, target):

        return self.scan(target, ["--robot"])

    def scan_all(self, target):

        return self.scan(target, self.default_arguments)
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "SSL",
            "description": "Enterprise SSL/TLS Security Scanner",
        }
=======

            "name": self.name,

            "category": "SSL",

            "description": "Enterprise SSL/TLS Security Scanner"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
