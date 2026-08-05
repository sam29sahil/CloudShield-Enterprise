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

<<<<<<< HEAD
    default_arguments = ["image"]

    def image(self, image_name):

        return self.scan(image_name, ["image"])

    def filesystem(self, path):

        return self.scan(path, ["fs"])

    def kubernetes(self):

        return self.scan("", ["kubernetes"])

    def config(self, path):

        return self.scan(path, ["config"])
=======
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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def info(self):

        return {
<<<<<<< HEAD
            "name": self.name,
            "category": "Cloud",
            "provider": "Containers/Kubernetes",
        }
=======

            "name": self.name,

            "category": "Cloud",

            "provider": "Containers/Kubernetes"

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
