import unittest
from exampleapp import create_app
from bs4 import BeautifulSoup

# LOL THIS PROBABLY WONT WORK :D enabled at web application level
class CSPTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_csp(self):
        # ensure csp is enabled
        resp = self.client.get('/')
        hsts_header = [h for h in resp.headers if h[0] == 'Content-Security-Policy']
        self.assertTrue(hsts_header)
        # ensure that the unsafe-inline is not in our csp
        self.assertFalse('unsafe-inline' in hsts_header)

if __name__ == '__main__':
    unittest.main()
