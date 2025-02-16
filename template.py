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
