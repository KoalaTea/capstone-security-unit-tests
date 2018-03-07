import unittest
from exampleapp import create_app
from bs4 import BeautifulSoup

# LOL THIS PROBABLY WONT WORK :D enabled at web application level
class HSTSTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def hsts(self, resp):
        # check each header to see if one is HSTS
        hsts_headers = [h for h in resp.headers if h[0] == 'Strict-Transport-Security']
        self.assertTrue(hsts_headers)

    def cert_pinning(self, resp):
        # TODO expand
        hsts_headers = [h for h in resp.headers if h[0] == 'Public-Key-Pins']
        self.assertTrue(hsts_headers)

    def test_https(self):
        resp = self.client.get('/')
        # test for https being the connection method
        self.assertEquals(resp.status_code, 302)
        self.assertTrue('https' in resp.data.decode('utf-8'))

    def test_hsts(self):
        # test for https working False for testing purposes
        resp = self.client.get('/', base_url='https://localhost')
        self.assertEqual(resp.status_code, 200)
        self.hsts(resp)

    def test_hpkp(self):
        # TODO test for a specific cert
        # cert_pinning(resp)
        pass

if __name__ == '__main__':
    unittest.main()
