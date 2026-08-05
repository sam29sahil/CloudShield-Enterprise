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

<<<<<<< HEAD
        return self.feeds[:limit]
=======
        return self.feeds[:limit]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
