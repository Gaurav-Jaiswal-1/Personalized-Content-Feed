import os
from pathlib import Path

# Define the project structure
list_of_files = [
    "backend/app/__init__.py",
    "backend/app/main.py",
    "backend/app/routes/__init__.py",
    "backend/app/routes/user_routes.py",
    "backend/app/routes/content_routes.py",
    "backend/app/services/__init__.py",
    "backend/app/services/content_fetcher.py",
    "backend/app/services/recommender.py",
    "backend/app/models/__init__.py",
    "backend/app/models/user.py",
    "backend/app/models/content.py",
    "backend/app/utils/__init__.py",
    "backend/app/utils/config.py",
    "backend/app/utils/logger.py",
    "backend/app/tests/test_routes.py",
    "backend/app/tests/test_services.py",
    "backend/requirements.txt",
    "backend/Dockerfile",
    "backend/README.md",
    "backend/.env",
    "chrome-extension/manifest.json",
    "chrome-extension/popup.html",
    "chrome-extension/popup.js",
    "chrome-extension/style.css",
    "chrome-extension/background.js",
    "chrome-extension/content.js",
    "chrome-extension/icons/icon16.png",
    "chrome-extension/icons/icon48.png",
    "chrome-extension/icons/icon128.png",
    "dataset/sample_data.json",
    "docs/API_Documentation.md",
    "docs/Chrome_Extension.md",
    "docs/Architecture_Diagram.png",
    "docs/README.md",
    ".gitignore",
    "README.md",
    "requirements.txt",
    "docker-compose.yml",
]

# Create the directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directories if they do not exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)

    # Create files if they do not exist or are empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
