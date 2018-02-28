import unittest
from exampleapp import create_app
from bs4 import BeautifulSoup

# LOL THIS PROBABLY WONT WORK :D enabled at web application level
class CSRFTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def hsts(self, resp):
        # check each header to see if one is HSTS
        hsts_headers = [h for h in resp.headers if h[0] == 'Strict-Transport-Security']
        self.assertTrue(hsts_headers)

    def test_https(self):
        resp = self.client.get('/')
        # test for https being the connection method
        self.assertEquals(resp.status_code, 301)
        self.assertEquals(resp.text.find('https'), 0)
        # test for https working False for testing purposes
        resp = self.client.get('/', base_url='https://localhost', verify=False)
        self.assertEqual(resp.status_code, 200)
        hsts(resp)
        # TODO test for a specific cert
