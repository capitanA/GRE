from flask import Blueprint, render_template

seccond = Blueprint("seccond", __name__, static_folder="static", template_folder="templates")


@seccond.route("/home")
@seccond.route("/")
def home():
    return render_template("home.html")
