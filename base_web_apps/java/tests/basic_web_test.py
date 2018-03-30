from exampleapp import create_app
import unittest
import requests

class BasicWebTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = requests

    def test_index(self):
        resp = self.client.get('/index', follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

if __name__ == '__main__':
    unittest.main()
