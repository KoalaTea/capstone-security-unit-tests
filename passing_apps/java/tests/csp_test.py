import unittest
from bs4 import BeautifulSoup
import requests

# LOL THIS PROBABLY WONT WORK :D enabled at web application level
class CSPTest(unittest.TestCase):
    def setUp(self):
        self.client = requests
        self.url = 'http://127.0.0.1:8081'

    def test_csp(self):
        # ensure csp is enabled
        resp = self.client.get(self.url+'/', verify=False)
        self.assertTrue('Content-Security-Policy' in resp.headers)
        # ensure that the unsafe-inline is not in our csp
        self.assertFalse('unsafe-inline' in resp.headers['Content-Security-Policy'])

if __name__ == '__main__':
    unittest.main()
