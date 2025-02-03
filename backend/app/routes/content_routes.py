from flask import Blueprint, request, jsonify
from app.services.recommender import recommend_content_for_user
from app.utils.data_loader import load_json_data

content_blueprint = Blueprint("content_routes", __name__)

@content_blueprint.route("/", methods=["GET"])
def get_all_content():
    content = load_json_data("dataset/sample_data.json")
    return jsonify(content)

@content_blueprint.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    user_id = data.get("user_id")
    # Retrieve user preferences from database or dataset
    # For demo, load from JSON file:
    user_data = load_json_data("dataset/user_preferences.json")
    user_pref = next((user for user in user_data if user["user_id"] == str(user_id)), None)
    if not user_pref:
        return jsonify({"error": "User not found"}), 404
    recommendations = recommend_content_for_user(user_pref)
    return jsonify(recommendations)
