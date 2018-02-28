from exampleapp import create_app
import unittest

class BasicWebTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index(self):
        resp = self.client.get('/index')
        self.assertEqual(resp.status_code, 200)
