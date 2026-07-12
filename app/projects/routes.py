"""
CloudShield Enterprise
Project Routes
"""

from flask import (
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import login_required

from app.projects import projects
from app.projects.forms import ProjectForm
from app.projects.services import ProjectManager


manager = ProjectManager()


@projects.route("/")
@login_required
def home():

    return render_template(

        "projects/index.html",

        projects=manager.all_projects()

    )


@projects.route("/new", methods=["GET", "POST"])
@login_required
def new_project():

    form = ProjectForm()

    if form.validate_on_submit():

        manager.create_project(

            name=form.name.data,

            description=form.description.data,

            owner=form.owner.data

        )

        flash(

            "Project created successfully.",

            "success"

        )

        return redirect(

            url_for("projects.home")

        )

    return render_template(

        "projects/new.html",

        form=form

    )


@projects.route("/view/<int:project_id>")
@login_required
def view(project_id):

    project = manager.get(project_id)

    return render_template(

        "projects/view.html",

        project=project

    )


@projects.route("/edit/<int:project_id>", methods=["GET", "POST"])
@login_required
def edit(project_id):

    project = manager.get(project_id)

    form = ProjectForm(obj=project)

    if form.validate_on_submit():

        manager.update_project(

            project_id=project.id,

            name=form.name.data,

            description=form.description.data,

            owner=form.owner.data

        )

        flash(

            "Project updated successfully.",

            "success"

        )

        return redirect(

            url_for(

                "projects.view",

                project_id=project.id

            )

        )

    return render_template(

        "projects/edit.html",

        form=form,

        project=project

    )


@projects.route("/delete/<int:project_id>")
@login_required
def delete(project_id):

    manager.delete_project(project_id)

    flash(

        "Project deleted successfully.",

        "success"

    )

    return redirect(

        url_for("projects.home")

    )