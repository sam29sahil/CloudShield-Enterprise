from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
<<<<<<< HEAD
from wtforms.validators import DataRequired, Email, EqualTo, Length
=======
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length
)
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5


class RegisterForm(FlaskForm):

    username = StringField(
<<<<<<< HEAD
        "Username", validators=[DataRequired(), Length(min=3, max=20)]
    )

    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])

    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
=======
        "Username",
        validators=[
            DataRequired(),
            Length(min=3, max=20)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8)
        ]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password")
        ]
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):

<<<<<<< HEAD
    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Login")
=======
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Login")
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
