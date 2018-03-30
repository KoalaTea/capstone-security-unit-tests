import unittest
from exampleapp import create_app
from bs4 import BeautifulSoup
import requests

# LOL THIS PROBABLY WONT WORK :D enabled at web application level
class HSTSTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = requests

    def hsts(self, resp):
        # check each header to see if one is HSTS
        hsts_headers = [h for h in resp.headers if h[0] == 'Strict-Transport-Security']
        self.assertTrue(hsts_headers)

    def cert_pinning(self, resp):
        # TODO expand I do not have an actual cert so I will defer this one this will raise
        # an error and get caught by the framework if it fails
        resp = self.client.get('/', base_url='https://localhost', cert=('/path/server.crt',
                               '/path/key'))
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
