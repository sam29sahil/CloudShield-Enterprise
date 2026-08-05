"""
CloudShield Enterprise
Docker Images
"""

from app.docker.docker_service import DockerService


class DockerImages:

    def __init__(self):

        self.docker = DockerService()

    # ----------------------------------
    # List Images
    # ----------------------------------

    def list(self):

        return self.docker.images()

    # ----------------------------------
    # Image Summary
    # ----------------------------------

    def summary(self):

        images = self.list()

        total_size = 0

        image_list = []

        for image in images:

            size = image.attrs.get("Size", 0)

            total_size += size

<<<<<<< HEAD
            image_list.append(
                {
                    "id": image.short_id,
                    "tags": image.tags,
                    "size": round(size / 1024 / 1024, 2),
                    "created": image.attrs.get("Created"),
                }
            )

        return {
            "count": len(images),
            "total_size_mb": round(total_size / 1024 / 1024, 2),
            "images": image_list,
        }
=======
            image_list.append({

                "id": image.short_id,

                "tags": image.tags,

                "size": round(size / 1024 / 1024, 2),

                "created": image.attrs.get("Created")

            })

        return {

            "count": len(images),

            "total_size_mb": round(

                total_size / 1024 / 1024,

                2

            ),

            "images": image_list

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
