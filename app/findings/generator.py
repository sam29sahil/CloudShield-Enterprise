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

        return FindingParser.parse(

            scan,

            result

        )