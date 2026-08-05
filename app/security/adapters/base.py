"""
CloudShield Enterprise
Base Result Adapter
"""


class BaseAdapter:
    """
    Base class for all adapters.
    """

    def adapt(self, tool, target, result, execution_time=0):
<<<<<<< HEAD
        raise NotImplementedError("Adapter must implement adapt().")
=======
        raise NotImplementedError(
            "Adapter must implement adapt()."
        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
