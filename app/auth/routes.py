from sqlalchemy.exc import IntegrityError
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

        username = form.username.data.strip()
        email = form.email.data.strip().lower()

        existing_username = User.query.filter_by(username=username).first()

        if existing_username:
            flash("That username is already in use.", "danger")
            return redirect(url_for("auth.register"))

        existing_email = User.query.filter_by(email=email).first()

        if existing_email:
            flash("An account with this email already exists.", "danger")
            return redirect(url_for("auth.register"))

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )

        new_user = User(
            username=username, email=email, password=hashed_password
        )

        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("An account with those details already exists.", "danger")
            return redirect(url_for("auth.register"))
        except Exception:
            db.session.rollback()
            flash("We could not create your account. Please try again.", "danger")
            return redirect(url_for("auth.register"))

        flash("Registration successful! Please login.", "success")

        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):

            login_user(user)

            flash("Login successful!", "success")

            return redirect(url_for("dashboard.home"))

        flash("Invalid email or password.", "danger")

    return render_template("login.html", form=form)


@auth.route("/logout")
def logout():

    logout_user()

    flash("Logged out successfully.", "info")

    return redirect(url_for("auth.login"))
