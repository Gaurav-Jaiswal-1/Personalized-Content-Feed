# backend/app/services/recommender.py
from app.utils.data_loader import load_json_data

def recommend_content_for_user(user_preferences):
    content_data = load_json_data("dataset/sample_data.json")
    preferred_categories = user_preferences.get("preferred_categories", [])
    preferred_tags = user_preferences.get("preferred_tags", [])
    
    # Compute a score for each content item based on matching tags
    def score_content(content):
        score = 0
        if content["category"] in preferred_categories:
            score += 1
        # Count the matching tags
        score += sum(1 for tag in content.get("tags", []) if tag in preferred_tags)
        return score

    # Filter and sort the content
    recommended = [content for content in content_data if content["category"] in preferred_categories]
    recommended = sorted(recommended, key=score_content, reverse=True)
    return recommended
