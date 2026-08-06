"""
CloudShield Enterprise
Base Result Adapter
"""


class BaseAdapter:
    """
    Base class for all adapters.
    """

    def adapt(self, tool, target, result, execution_time=0):
        raise NotImplementedError(
            "Adapter must implement adapt()."
        )