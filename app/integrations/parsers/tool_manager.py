"""
CloudShield Enterprise
Professional Tool Manager
"""

import shutil

from app.integrations.nmap_scanner import NmapScanner
from app.integrations.nikto_scanner import NiktoScanner
from app.integrations.whatweb_scanner import WhatWebScanner
from app.integrations.nuclei_scanner import NucleiScanner
from app.integrations.wafw00f_scanner import WAFScanner


class ToolManager:

    def __init__(self):

        self.available = {
            "nmap": shutil.which("nmap"),
            "nikto": shutil.which("nikto"),
            "whatweb": shutil.which("whatweb"),
            "nuclei": shutil.which("nuclei"),
            "wafw00f": shutil.which("wafw00f"),
        }

        self.nmap = NmapScanner()

        self.nikto = NiktoScanner()

        self.whatweb = WhatWebScanner()

        self.nuclei = NucleiScanner()

        self.waf = WAFScanner()

    def installed_tools(self):

        return {tool: bool(path) for tool, path in self.available.items()}

    def scan_all(self, target):

        results = {}

        if self.available["nmap"]:

            results["nmap"] = self.nmap.service_scan(target)

        if self.available["whatweb"]:

            results["whatweb"] = self.whatweb.scan(target)

        if self.available["nikto"]:

            results["nikto"] = self.nikto.scan(target)

        if self.available["nuclei"]:

            results["nuclei"] = self.nuclei.scan(target)

        if self.available["wafw00f"]:

            results["waf"] = self.waf.scan(target)

        return results
