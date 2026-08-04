"""
CloudShield Enterprise
Target Validator
"""

from app.security.core.target import Target


class TargetValidator:
    """
    Validates scan targets.
    """

    @staticmethod
    def validate(target: str):
        return Target.validate(target)
