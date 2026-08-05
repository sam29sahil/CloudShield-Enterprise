"""
CloudShield Enterprise
Asset Routes
"""

<<<<<<< HEAD
from flask import Blueprint, render_template, redirect, url_for, flash, request
=======
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

from flask_login import login_required
from app.models.project import Project
from app.assets.forms import AssetForm
from app.assets.services import AssetManager

from app.assets import assets
<<<<<<< HEAD

=======
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
manager = AssetManager()


@assets.route("/")
@login_required
def home():

    search = request.args.get("search", "").strip()

    risk = request.args.get("risk", "")

    asset_type = request.args.get("type", "")

    project = request.args.get("project", "")

    assets = manager.filter_assets(
<<<<<<< HEAD
        search=search, risk=risk, asset_type=asset_type, project=project
=======

        search=search,

        risk=risk,

        asset_type=asset_type,

        project=project

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )

    projects = manager.projects()

    return render_template(
<<<<<<< HEAD
        "assets/index.html",
        assets=assets,
        projects=projects,
        search=search,
        risk=risk,
        asset_type=asset_type,
        project=project,
    )

=======

        "assets/index.html",

        assets=assets,

        projects=projects,

        search=search,

        risk=risk,

        asset_type=asset_type,

        project=project

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@assets.route("/new", methods=["GET", "POST"])
@login_required
def new_asset():

    form = AssetForm()
    form.project_id.choices = [
<<<<<<< HEAD
        (project.id, project.name)
        for project in Project.query.order_by(Project.name).all()
=======

        (project.id, project.name)

        for project in Project.query.order_by(Project.name).all()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    ]

    if form.validate_on_submit():

        manager.create_asset(
<<<<<<< HEAD
            name=form.name.data,
            target=form.target.data,
            asset_type=form.asset_type.data,
            project_id=form.project_id.data,
        )

        flash("Asset added successfully.", "success")

        return redirect(url_for("assets.home"))

    return render_template("assets/new.html", form=form)
=======

            name=form.name.data,
            target=form.target.data,
            asset_type=form.asset_type.data,
            project_id=form.project_id.data

        )

        flash(
            "Asset added successfully.",
            "success"
        )

        return redirect(
            url_for("assets.home")
        )

    return render_template(
        "assets/new.html",
        form=form
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@assets.route("/view/<int:asset_id>")
@login_required
def view(asset_id):

    asset = manager.get(asset_id)

<<<<<<< HEAD
    return render_template("assets/view.html", asset=asset)

=======
    return render_template(
        "assets/view.html",
        asset=asset
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@assets.route("/edit/<int:asset_id>", methods=["GET", "POST"])
@login_required
def edit(asset_id):

    asset = manager.get(asset_id)

    form = AssetForm(obj=asset)
    form.project_id.choices = [
<<<<<<< HEAD
        (project.id, project.name)
        for project in Project.query.order_by(Project.name).all()
=======
        
        (project.id, project.name)

        for project in Project.query.order_by(Project.name).all()

>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    ]

    if form.validate_on_submit():

        manager.update_asset(
<<<<<<< HEAD
            asset_id=asset.id,
            name=form.name.data,
            target=form.target.data,
            asset_type=form.asset_type.data,
            project_id=form.project_id.data,
        )

        flash("Asset updated successfully.", "success")

        return redirect(url_for("assets.view", asset_id=asset.id))

    return render_template("assets/edit.html", form=form, asset=asset)

=======

            asset_id=asset.id,

            name=form.name.data,

            target=form.target.data,

            asset_type=form.asset_type.data,

            project_id=form.project_id.data

        )

        flash(

            "Asset updated successfully.",

            "success"

        )

        return redirect(

            url_for("assets.view", asset_id=asset.id)

        )

    return render_template(

        "assets/edit.html",

        form=form,

        asset=asset

    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

@assets.route("/delete/<int:asset_id>")
@login_required
def delete(asset_id):

    manager.delete_asset(asset_id)

<<<<<<< HEAD
    flash("Asset deleted successfully.", "success")

    return redirect(url_for("assets.home"))
=======
    flash(
        "Asset deleted successfully.",
        "success"
    )

    return redirect(
        url_for("assets.home")
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
