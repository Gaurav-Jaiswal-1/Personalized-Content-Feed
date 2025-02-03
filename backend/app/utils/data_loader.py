import json
from pathlib import Path

def load_json_data(filename):
    filepath = Path(__file__).parent.parent.parent / filename  # Adjust relative path if needed
    with open(filepath, "r") as f:
        return json.load(f)

# Usage:
# content_data = load_json_data("dataset/sample_data.json")
