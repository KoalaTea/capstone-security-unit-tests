import unittest
from bs4 import BeautifulSoup
import requests
from IPython import embed

class HeadersTest(unittest.TestCase):
    def setUp(self):
        self.client = requests
        self.url = "http://127.0.0.1:8081"
        self.resp = self.client.get(self.url+'/')
        self.headers = {}
        self._headers()
        #embed()

    def test_X_FRAME_OPTIONS(self):
        self.assertTrue('X-Frame-Options' in self.resp.headers)

    def test_X_XSS_Protection(self):
        self.assertTrue('X-XSS-Protection' in self.resp.headers)

    def test_Referrer_Policy(self):
        self.assertTrue('Referrer-Policy' in self.resp.headers)

    def test_X_Content_Type_Options(self):
        self.assertTrue('X-Content-Type-Options' in self.resp.headers)

    def test_X_Permitted_Cross_Domain_Policies(self):
        self.assertTrue('X-Permitted-Cross-Domain-Policies' in self.resp.headers)

    def test_Expected_CT(self):
        self.assertTrue('Expected-CT' in self.resp.headers)

if __name__ == '__main__':
    unittest.main()
