"""
CloudShield Enterprise
Project Service
"""

from app.extensions import db
from app.models.project import Project


class ProjectService:

    def all(self):

        return Project.query.all()

    def get(self, project_id):

        return Project.query.get(project_id)

<<<<<<< HEAD
    def create(self, name, description, owner):

        project = Project(name=name, description=description, owner=owner)
=======
    def create(

        self,

        name,

        description,

        owner

    ):

        project = Project(

            name=name,

            description=description,

            owner=owner

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        db.session.add(project)

        db.session.commit()

        return project

    def delete(self, project_id):

        project = self.get(project_id)

        if project:

            db.session.delete(project)

<<<<<<< HEAD
            db.session.commit()
=======
            db.session.commit()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
