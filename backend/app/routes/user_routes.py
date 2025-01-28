from flask import Blueprint, request, jsonify

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/", methods=["GET"])
def get_users():
    return jsonify({"message": "List of users"})

@user_blueprint.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify({"message": f"Details of user {user_id}"})
