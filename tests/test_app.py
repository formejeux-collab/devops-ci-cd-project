import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_province(self):
        response = self.app.get('/api/province/Estuaire')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('villes', data)

if __name__ == '__main__':
    unittest.main()