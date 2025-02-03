import unittest
from app import create_app
from app.models.user import User
from app.models.content import Content

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome", response.data)

    def test_recommendation_endpoint(self):
        # Adjust as needed; assumes you have sample user data
        response = self.client.post("/content/recommend", json={"user_id": "101"})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
