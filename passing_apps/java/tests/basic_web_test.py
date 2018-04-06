import unittest
import requests

class BasicWebTest(unittest.TestCase):
    def setUp(self):
        self.client = requests
        self.url = "http://127.0.0.1:8081"

    def test_index(self):
        resp = self.client.get(self.url+'/')
        self.assertEqual(resp.status_code, 200)

if __name__ == '__main__':
    unittest.main()
