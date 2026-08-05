"""
CloudShield Enterprise
Prowler Tool
"""

from app.security.tools.common.base import BaseTool

from app.security.tools.cloud.constants import PROWLER_DEFAULT


class ProwlerTool(BaseTool):
    """
    AWS Security Scanner
    """

    name = "prowler"

    default_arguments = PROWLER_DEFAULT

    def aws(self):

<<<<<<< HEAD
        return self.scan("", ["aws"])

    def cis(self):

        return self.scan("", ["aws", "--compliance", "cis"])

    def pci(self):

        return self.scan("", ["aws", "--compliance", "pci"])

    def info(self):

        return {"name": self.name, "category": "Cloud", "provider": "AWS"}
=======
        return self.scan(

            "",

            [

                "aws"

            ]

        )

    def cis(self):

        return self.scan(

            "",

            [

                "aws",

                "--compliance",

                "cis"

            ]

        )

    def pci(self):

        return self.scan(

            "",

            [

                "aws",

                "--compliance",

                "pci"

            ]

        )

    def info(self):

        return {

            "name": self.name,

            "category": "Cloud",

            "provider": "AWS"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
