import requests
import os

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

def fetch_videos(keyword):
    params = {
        "part": "snippet",
        "q": keyword,
        "type": "video",
        "key": YOUTUBE_API_KEY,
        "maxResults": 10
    }
    
    try:
        response = requests.get(YOUTUBE_SEARCH_URL, params=params)
        response.raise_for_status()  # Raises error if the request fails
        data = response.json()
        return data.get("items", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching videos: {e}")
        return []
    

import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def fetch_videos(keyword):
    cache_key = f"youtube:{keyword}"
    cached_data = redis_client.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    params = {
        "part": "snippet",
        "q": keyword,
        "type": "video",
        "key": YOUTUBE_API_KEY,
        "maxResults": 10
    }

    try:
        response = requests.get(YOUTUBE_SEARCH_URL, params=params)
        response.raise_for_status()
        data = response.json()
        videos = data.get("items", [])
        
        redis_client.setex(cache_key, 3600, json.dumps(videos))  # Cache for 1 hour
        return videos
    except requests.exceptions.RequestException as e:
        print(f"Error fetching videos: {e}")
        return []

