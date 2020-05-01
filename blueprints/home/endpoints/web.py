from flask import Blueprint, request
from flask import make_response, jsonify

web = Blueprint("home.web", __name__)


@web.route("/", methods=["GET", "POST", ])
def index():
    return make_response(jsonify(mesg="GRE is Running ..."), 200)
