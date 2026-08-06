"""
CloudShield Enterprise
IOC Service
"""


class IOCService:
    """
    Indicator of Compromise Service
    """

    def __init__(self):

        self.iocs = [
            {
                "value": "192.168.1.100",
                "type": "IP Address",
                "severity": "Medium",
                "source": "Demo Feed",
                "status": "Active",
            },
            {
                "value": "malicious-example.com",
                "type": "Domain",
                "severity": "High",
                "source": "Demo Feed",
                "status": "Active",
            },
            {
                "value": "44d88612fea8a8f36de82e1278abb02f",
                "type": "MD5",
                "severity": "Critical",
                "source": "Demo Feed",
                "status": "Active",
            },
        ]

    # ----------------------------------------

    def all(self):

        return self.iocs

    # ----------------------------------------

    def count(self):

        return len(self.iocs)

    # ----------------------------------------

    def search(self, keyword):

        keyword = keyword.lower()

        return [
            ioc
            for ioc in self.iocs
            if keyword in ioc["value"].lower()
            or keyword in ioc["type"].lower()
            or keyword in ioc["severity"].lower()
        ]

    # ----------------------------------------

    def by_severity(self, severity):

        return [ioc for ioc in self.iocs if ioc["severity"].lower() == severity.lower()]
