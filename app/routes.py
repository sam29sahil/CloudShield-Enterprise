from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint("main", __name__)

<<<<<<< HEAD

@main.route("/")
@login_required
def home():
    return render_template("index.html")
=======
@main.route("/")
@login_required
def home():
    return render_template("index.html")
>>>>>>> ced70e1725c55fe0379baaf4f6a4ee392ae289d5
