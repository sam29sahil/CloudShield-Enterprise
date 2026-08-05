"""
CloudShield Enterprise
CloudSplaining Tool
"""

from app.security.tools.common.base import BaseTool


class CloudSplainingTool(BaseTool):
    """
    AWS IAM Analysis
    """

    name = "cloudsplaining"

<<<<<<< HEAD
    default_arguments = ["scan"]

    def iam(self):

        return self.scan("", ["scan"])

    def permissions(self):

        return self.scan("", ["permissions"])

    def report(self):

        return self.scan("", ["report"])

    def info(self):

        return {"name": self.name, "category": "Cloud", "provider": "AWS"}
=======
    default_arguments = [

        "scan"

    ]

    def iam(self):

        return self.scan(

            "",

            [

                "scan"

            ]

        )

    def permissions(self):

        return self.scan(

            "",

            [

                "permissions"

            ]

        )

    def report(self):

        return self.scan(

            "",

            [

                "report"

            ]

        )

    def info(self):

        return {

            "name": self.name,

            "category": "Cloud",

            "provider": "AWS"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
