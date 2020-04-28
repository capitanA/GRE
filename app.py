from flask import Flask, render_template
from application import create_app
from os import getenv
from config import UATConfig, DevelopConfig, ProductionConfig
from seccond import seccond


configuration = ProductionConfig
environment = getenv("ENV") or "PRODUCTION"

if environment == "DEVELOPMENT":
    configuration = DevelopConfig
elif environment == "UAT":
    configuration = UATConfig

app = create_app(configuration)
app.register_blueprint(seccond,url_prefix="")


# @app.route("/")
# def home():
#     return render_template("home.html")
#
#
# @app.route("/about")
# def about():
#     return render_template("about.html")


if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"], threaded=True)
