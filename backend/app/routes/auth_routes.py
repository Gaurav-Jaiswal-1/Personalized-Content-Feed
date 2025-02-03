from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user import User  # Ensure you have a method to verify a user

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    # Replace this with your actual user authentication logic
    user = User.authenticate(username, password)
    if not user:
        return jsonify({"msg": "Bad username or password"}), 401
    
    access_token = create_access_token(identity=user.user_id)
    return jsonify(access_token=access_token), 200
