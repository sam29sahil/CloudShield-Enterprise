"""
CloudShield Enterprise
ScoutSuite Tool
"""

from app.security.tools.common.base import BaseTool

from app.security.tools.cloud.constants import SCOUTSUITE_DEFAULT


class ScoutSuiteTool(BaseTool):
    """
    Multi-Cloud Security Scanner
    """

    name = "scoutsuite"

    default_arguments = SCOUTSUITE_DEFAULT

    def aws(self):

<<<<<<< HEAD
        return self.scan("", ["aws"])

    def azure(self):

        return self.scan("", ["azure"])

    def gcp(self):

        return self.scan("", ["gcp"])

    def info(self):

        return {"name": self.name, "category": "Cloud", "provider": "AWS/Azure/GCP"}
=======
        return self.scan(

            "",

            [

                "aws"

            ]

        )

    def azure(self):

        return self.scan(

            "",

            [

                "azure"

            ]

        )

    def gcp(self):

        return self.scan(

            "",

            [

                "gcp"

            ]

        )

    def info(self):

        return {

            "name": self.name,

            "category": "Cloud",

            "provider": "AWS/Azure/GCP"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
