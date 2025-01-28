from .content_fetcher import fetch_all_content

def recommend_content_for_user(user_preferences):
    all_content = fetch_all_content()
    preferred_content = [
        content for content in all_content 
        if content["category"] in user_preferences["preferred_categories"]
    ]
    return preferred_content
