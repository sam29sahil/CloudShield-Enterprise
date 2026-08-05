"""
CloudShield Enterprise
Docker Containers
"""

from app.docker.docker_service import DockerService


class DockerContainers:

    def __init__(self):

        self.docker = DockerService()

    def list(self):

        return self.docker.containers()

    def details(self, container_id):

        return self.docker.container(container_id)

    def logs(self, container_id):

        return self.docker.logs(container_id)

    def stats(self, container_id):

        return self.docker.stats(container_id)

    def start(self, container_id):

        return self.docker.start(container_id)

    def stop(self, container_id):

        return self.docker.stop(container_id)

    def restart(self, container_id):

        return self.docker.restart(container_id)

    def remove(self, container_id):

<<<<<<< HEAD
        return self.docker.remove(container_id)
=======
        return self.docker.remove(container_id)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
