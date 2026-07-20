"""
CloudShield Enterprise
Universal Scan Service
"""

from app.scanner.website_service import scan_website

from app.security.integration.manager import IntegrationManager


class ScanService:

    def __init__(self):

        self.manager = IntegrationManager()

    def website(

        self,

        url

    ):

        return scan_website(url)

    def tool(

        self,

        tool,

        target,

        arguments=None

    ):

        return self.manager.execute(

            tool,

            target,

            arguments

        )