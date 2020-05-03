from flask import Blueprint, request

web = Blueprint("account.web", __name__, url_prefix="/account/api")


@web.route("/v1/login", methods=["POST", ])
def login():
    print(request.headers)
