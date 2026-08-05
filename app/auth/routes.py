from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user

from app.auth import auth
from app.auth.forms import RegisterForm, LoginForm
from app.extensions import db, bcrypt
from app.models import User


@auth.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

<<<<<<< HEAD
        existing_username = User.query.filter_by(username=form.username.data).first()
=======
        existing_username = User.query.filter_by(
            username=form.username.data
        ).first()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        if existing_username:
            flash("Username already exists!", "danger")
            return redirect(url_for("auth.register"))

<<<<<<< HEAD
        existing_email = User.query.filter_by(email=form.email.data).first()
=======
        existing_email = User.query.filter_by(
            email=form.email.data
        ).first()
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

        if existing_email:
            flash("Email already registered!", "danger")
            return redirect(url_for("auth.register"))

<<<<<<< HEAD
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )

        new_user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
=======
        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")

        return redirect(url_for("auth.login"))

<<<<<<< HEAD
    return render_template("register.html", form=form)
=======
    return render_template(
        "register.html",
        form=form
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

<<<<<<< HEAD
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
=======
        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and bcrypt.check_password_hash(
            user.password,
            form.password.data
        ):
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5

            login_user(user)

            flash("Login successful!", "success")

            return redirect(url_for("dashboard.home"))

        flash("Invalid email or password.", "danger")

<<<<<<< HEAD
    return render_template("login.html", form=form)
=======
    return render_template(
        "login.html",
        form=form
    )
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


@auth.route("/logout")
def logout():

    logout_user()

    flash("Logged out successfully.", "info")

<<<<<<< HEAD
    return redirect(url_for("auth.login"))
=======
    return redirect(url_for("auth.login"))
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
