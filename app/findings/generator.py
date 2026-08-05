"""
CloudShield Enterprise
Finding Generator
"""

from app.findings.parser import FindingParser


class FindingGenerator:
    """
    Universal Finding Generator
    """

    @staticmethod
    def generate(scan, result):

<<<<<<< HEAD
        return FindingParser.parse(scan, result)
=======
        return FindingParser.parse(

            scan,

            result

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
