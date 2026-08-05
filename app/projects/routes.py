"""
CloudShield Enterprise
Project Routes
"""

<<<<<<< HEAD
from flask import render_template, redirect, url_for, flash
=======
from flask import (
    render_template,
    redirect,
    url_for,
    flash
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

from flask_login import login_required

from app.projects import projects
from app.projects.forms import ProjectForm
from app.projects.services import ProjectManager

<<<<<<< HEAD
=======

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
manager = ProjectManager()


@projects.route("/")
@login_required
def home():

<<<<<<< HEAD
    return render_template("projects/index.html", projects=manager.all_projects())
=======
    return render_template(

        "projects/index.html",

        projects=manager.all_projects()

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@projects.route("/new", methods=["GET", "POST"])
@login_required
def new_project():

    form = ProjectForm()

    if form.validate_on_submit():

        manager.create_project(
<<<<<<< HEAD
            name=form.name.data,
            description=form.description.data,
            owner=form.owner.data,
        )

        flash("Project created successfully.", "success")

        return redirect(url_for("projects.home"))

    return render_template("projects/new.html", form=form)
=======

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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@projects.route("/view/<int:project_id>")
@login_required
def view(project_id):

    project = manager.get(project_id)

<<<<<<< HEAD
    return render_template("projects/view.html", project=project)
=======
    return render_template(

        "projects/view.html",

        project=project

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@projects.route("/edit/<int:project_id>", methods=["GET", "POST"])
@login_required
def edit(project_id):

    project = manager.get(project_id)

    form = ProjectForm(obj=project)

    if form.validate_on_submit():

        manager.update_project(
<<<<<<< HEAD
            project_id=project.id,
            name=form.name.data,
            description=form.description.data,
            owner=form.owner.data,
        )

        flash("Project updated successfully.", "success")

        return redirect(url_for("projects.view", project_id=project.id))

    return render_template("projects/edit.html", form=form, project=project)
=======

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
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@projects.route("/delete/<int:project_id>")
@login_required
def delete(project_id):

    manager.delete_project(project_id)

<<<<<<< HEAD
    flash("Project deleted successfully.", "success")

    return redirect(url_for("projects.home"))
=======
    flash(

        "Project deleted successfully.",

        "success"

    )

    return redirect(

        url_for("projects.home")

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
