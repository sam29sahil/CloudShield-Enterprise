"""
CloudShield Enterprise
Trivy Tool
"""

from app.security.tools.common.base import BaseTool


class TrivyTool(BaseTool):
    """
    Trivy Scanner
    """

    name = "trivy"

    default_arguments = [

        "image"

    ]

    def image(self, image_name):

        return self.scan(

            image_name,

            [

                "image"

            ]

        )

    def filesystem(self, path):

        return self.scan(

            path,

            [

                "fs"

            ]

        )

    def kubernetes(self):

        return self.scan(

            "",

            [

                "kubernetes"

            ]

        )

    def config(self, path):

        return self.scan(

            path,

            [

                "config"

            ]

        )

    def info(self):

        return {

            "name": self.name,

            "category": "Cloud",

            "provider": "Containers/Kubernetes"

        }