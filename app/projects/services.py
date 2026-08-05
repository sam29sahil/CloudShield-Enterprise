"""
CloudShield Enterprise
Project Service
"""

from app.extensions import db
from app.models.project import Project


class ProjectManager:

    def all_projects(self):

<<<<<<< HEAD
        return Project.query.order_by(Project.created_at.desc()).all()
=======
        return (

            Project.query

            .order_by(Project.created_at.desc())

            .all()

        )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

    def get(self, project_id):

        return Project.query.get_or_404(project_id)

<<<<<<< HEAD
    def create_project(self, name, description, owner):

        project = Project(name=name, description=description, owner=owner)
=======
    def create_project(

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

<<<<<<< HEAD
    def update_project(self, project_id, name, description, owner):
=======
    def update_project(

        self,

        project_id,

        name,

        description,

        owner

    ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        project = Project.query.get_or_404(project_id)

        project.name = name
        project.description = description
        project.owner = owner

        db.session.commit()

        return project

    def delete_project(self, project_id):

        project = Project.query.get_or_404(project_id)

        db.session.delete(project)

<<<<<<< HEAD
        db.session.commit()
=======
        db.session.commit()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
