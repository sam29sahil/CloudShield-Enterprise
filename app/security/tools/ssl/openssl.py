"""
CloudShield Enterprise
OpenSSL Tool
"""

from app.security.tools.common.base import BaseTool

from app.security.tools.ssl.constants import OPENSSL_DEFAULT


class OpenSSLTool(BaseTool):
    """
    OpenSSL Scanner
    """

    name = "openssl"

    default_arguments = OPENSSL_DEFAULT
    timeout = 300

    def certificate(self, target):

        return self.scan(target, ["s_client", "-connect"])

    def show_certificate(self, target):

        return self.scan(target, ["s_client", "-showcerts", "-connect"])

    def cipher(self, target):

        return self.scan(target, ["ciphers"])

    def version(self):

        return self.runner.version("openssl")

    def info(self):

        return {
            "name": self.name,
            "category": "SSL",
            "description": "OpenSSL Security Toolkit",
        }
