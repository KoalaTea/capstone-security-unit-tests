import unittest
from bs4 import BeautifulSoup
import requests

# LOL THIS PROBABLY WONT WORK :D enabled at web application level
class CSPTest(unittest.TestCase):
    def setUp(self):
        self.client = requests
        self.url = 'http://127.0.0.1:8080'

    def test_csp(self):
        # ensure csp is enabled
        resp = self.client.get(self.url+'/')
        hsts_header = [h for h in resp.headers if h[0] == 'Content-Security-Policy']
        self.assertTrue(hsts_header)
        # ensure that the unsafe-inline is not in our csp
        self.assertFalse('unsafe-inline' in hsts_header)

if __name__ == '__main__':
    unittest.main()
