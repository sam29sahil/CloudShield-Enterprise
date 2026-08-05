"""
CloudShield Enterprise
Core Scanner Engine
"""

from app.scanner.website_service import scan_website


class ScannerEngine:

    def __init__(self):

        pass

    def start_scan(self, url):

        return scan_website(url)
