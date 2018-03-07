import unittest
from exampleapp import create_app
from bs4 import BeautifulSoup
from IPython import embed

# LOL THIS PROBABLY WONT WORK :D enabled at web application level
class HeadersTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.debug = True
        self.client = self.app.test_client()

    def headers(self, resp):
        # check each header to see if one is HSTS
        headers = ['X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options',
                   'X-Permitted-Cross-Domain-Policies', 'Expected-CT', 'Referrer-Policy']
        found_headers = [h for h in resp.headers if h[0] in headers]
        # TODO make this test actually work
        # currently finds X-Frame, X-XSS-Protection, X-Content-Type-Options, Referrer-Policy
        self.assertEqual(len(headers), len(found_headers))

    def test_headers(self):
        # test for
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.headers(resp)
        # TODO test for a specific cert

if __name__ == '__main__':
    unittest.main()
