import requests
import os

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetch_videos(query):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if "items" in data:
        return [item["snippet"]["title"] for item in data["items"]]
    return []
