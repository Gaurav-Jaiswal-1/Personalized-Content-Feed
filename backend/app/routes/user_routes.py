from flask import Blueprint, jsonify

user_blueprint = Blueprint("user_routes", __name__)

@user_blueprint.route("/", methods=["GET"])
def list_users():
    # Retrieve user data from the database
    users = []  # Replace with actual query, e.g., User.query.all()
    return jsonify({"users": [user.serialize() for user in users]})
