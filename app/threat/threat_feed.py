"""
CloudShield Enterprise
Threat Feed Service
"""


class ThreatFeedService:
    """
    Threat Intelligence Feed Service
    """

    def __init__(self):

        self.feeds = []

    # -------------------------------------

    def all(self):

        return self.feeds

    # -------------------------------------

    def count(self):

        return len(self.feeds)

    # -------------------------------------

    def connected(self):

        return len(self.feeds) > 0

    # -------------------------------------

    def latest(self, limit=10):

        return self.feeds[:limit]
