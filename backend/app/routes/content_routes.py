from flask import Blueprint, request, jsonify

content_blueprint = Blueprint("content", __name__)

@content_blueprint.route("/", methods=["GET"])
def get_content():
    return jsonify({"message": "List of content"})

@content_blueprint.route("/recommend", methods=["POST"])
def recommend_content():
    data = request.json
    return jsonify({"message": "Recommended content", "data": data})
