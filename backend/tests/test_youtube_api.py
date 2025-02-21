import unittest
from backend.src.services.youtube_api import fetch_videos

class TestYouTubeAPI(unittest.TestCase):
    def test_fetch_videos(self):
        videos = fetch_videos("technology")
        self.assertIsInstance(videos, list)
        self.assertGreater(len(videos), 0)

if __name__ == "__main__":
    unittest.main()
