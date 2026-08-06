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

    def create(self, name, description, owner):

        project = Project(name=name, description=description, owner=owner)

        db.session.add(project)

        db.session.commit()

        return project

    def delete(self, project_id):

        project = self.get(project_id)

        if project:

            db.session.delete(project)

            db.session.commit()
