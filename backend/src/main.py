# backend/src/main.py
from fastapi import FastAPI
from backend.src.services.youtube_api import fetch_videos
from backend.src.services.recommender import filter_videos

app = FastAPI()

@app.get("/recommendations")
def get_recommendations(keyword: str):
    videos = fetch_videos(keyword)
    filtered_videos = filter_videos(videos, keyword)
    return {"videos": filtered_videos}


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to specific domains if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


