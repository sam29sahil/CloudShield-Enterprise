"""
CloudShield Enterprise
Docker Runtime
"""

from app.docker.docker_service import DockerService


class DockerRuntime:

    def __init__(self):

        self.docker = DockerService()

    def information(self):

        return self.docker.info()

    def version(self):

        return self.docker.version()

    def running(self):

        return self.docker.running_containers()

    def health(self):

        return {
<<<<<<< HEAD
            "running": self.docker.is_running(),
            "containers": len(self.docker.running_containers()),
            "images": len(self.docker.images()),
            "networks": len(self.docker.networks()),
            "volumes": len(self.docker.volumes()),
        }
=======

            "running": self.docker.is_running(),

            "containers": len(

                self.docker.running_containers()

            ),

            "images": len(

                self.docker.images()

            ),

            "networks": len(

                self.docker.networks()

            ),

            "volumes": len(

                self.docker.volumes()

            )

        }
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
