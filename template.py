import os
from pathlib import Path

# Define the new project structure
list_of_files = [
    "backend/src/__init__.py",
    "backend/src/main.py",
    "backend/src/config.py",
    "backend/src/services/__init__.py",
    "backend/src/services/youtube_api.py",
    "backend/src/services/recommender.py",
    "backend/src/models/__init__.py",
    "backend/src/models/video.py",
    "backend/src/utils/__init__.py",
    "backend/src/utils/logger.py",
    "backend/tests/test_youtube_api.py",
    "backend/tests/test_recommender.py",
    "backend/requirements.txt",
    "backend/.env",
    "backend/README.md",
    "extension/src/manifest.json",
    "extension/src/popup.html",
    "extension/src/popup.js",
    "extension/src/background.js",
    "extension/src/content.js",
    "extension/src/styles.css",
    "extension/icons/icon16.png",
    "extension/icons/icon48.png",
    "extension/icons/icon128.png",
    "extension/README.md",
    "deployment/docker-compose.yml",
    "deployment/cloud-deployment.md",
    ".gitignore",
    "LICENSE",
    "README.md"
]

# Create the directory structure
for file_path in list_of_files:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)

print("Project structure created successfully!")


# Optimal Chrome Extension Solution
# The extension should modify YouTube's video feed based on user input keywords
# Steps:
# 1. Use content.js to manipulate the YouTube DOM and filter videos.
# 2. background.js listens for user input and stores preferences.
# 3. popup.js provides a UI for users to enter keywords/tags.
# 4. youtube_api.py fetches and filters video recommendations via YouTube Data API.
# 5. recommender.py uses NLP to refine search results and filter video suggestions.

# Example content.js (Injects script to filter videos based on user input)
# document.addEventListener('DOMContentLoaded', function () {
#     chrome.storage.sync.get(['keywords'], function(result) {
#         let keywords = result.keywords || [];
#         let videos = document.querySelectorAll("ytd-video-renderer");
#         videos.forEach(video => {
#             let title = video.querySelector("#video-title").innerText;
#             if (!keywords.some(keyword => title.toLowerCase().includes(keyword.toLowerCase()))) {
#                 video.style.display = 'none';
#             }
#         });
#     });
# });