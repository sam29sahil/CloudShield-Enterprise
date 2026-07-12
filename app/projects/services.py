"""
CloudShield Enterprise
Project Service
"""

from app.extensions import db
from app.models.project import Project


class ProjectManager:

    def all_projects(self):

        return (

            Project.query

            .order_by(Project.created_at.desc())

            .all()

        )

    def get(self, project_id):

        return Project.query.get_or_404(project_id)

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

        db.session.add(project)

        db.session.commit()

        return project

    def update_project(

        self,

        project_id,

        name,

        description,

        owner

    ):

        project = Project.query.get_or_404(project_id)

        project.name = name
        project.description = description
        project.owner = owner

        db.session.commit()

        return project

    def delete_project(self, project_id):

        project = Project.query.get_or_404(project_id)

        db.session.delete(project)

        db.session.commit()