"""
CloudShield Enterprise
Asset Routes
"""

from flask import Blueprint, render_template, redirect, url_for, flash, request

from flask_login import login_required
from app.models.project import Project
from app.assets.forms import AssetForm
from app.assets.services import AssetManager

from app.assets import assets

manager = AssetManager()


@assets.route("/")
@login_required
def home():

    search = request.args.get("search", "").strip()

    risk = request.args.get("risk", "")

    asset_type = request.args.get("type", "")

    project = request.args.get("project", "")

    assets = manager.filter_assets(
        search=search, risk=risk, asset_type=asset_type, project=project
    )

    projects = manager.projects()

    return render_template(
        "assets/index.html",
        assets=assets,
        projects=projects,
        search=search,
        risk=risk,
        asset_type=asset_type,
        project=project,
    )


@assets.route("/new", methods=["GET", "POST"])
@login_required
def new_asset():

    form = AssetForm()
    form.project_id.choices = [
        (project.id, project.name)
        for project in Project.query.order_by(Project.name).all()
    ]

    if form.validate_on_submit():

        manager.create_asset(
            name=form.name.data,
            target=form.target.data,
            asset_type=form.asset_type.data,
            project_id=form.project_id.data,
        )

        flash("Asset added successfully.", "success")

        return redirect(url_for("assets.home"))

    return render_template("assets/new.html", form=form)


@assets.route("/view/<int:asset_id>")
@login_required
def view(asset_id):

    asset = manager.get(asset_id)

    return render_template("assets/view.html", asset=asset)


@assets.route("/edit/<int:asset_id>", methods=["GET", "POST"])
@login_required
def edit(asset_id):

    asset = manager.get(asset_id)

    form = AssetForm(obj=asset)
    form.project_id.choices = [
        (project.id, project.name)
        for project in Project.query.order_by(Project.name).all()
    ]

    if form.validate_on_submit():

        manager.update_asset(
            asset_id=asset.id,
            name=form.name.data,
            target=form.target.data,
            asset_type=form.asset_type.data,
            project_id=form.project_id.data,
        )

        flash("Asset updated successfully.", "success")

        return redirect(url_for("assets.view", asset_id=asset.id))

    return render_template("assets/edit.html", form=form, asset=asset)


@assets.route("/delete/<int:asset_id>")
@login_required
def delete(asset_id):

    manager.delete_asset(asset_id)

    flash("Asset deleted successfully.", "success")

    return redirect(url_for("assets.home"))
