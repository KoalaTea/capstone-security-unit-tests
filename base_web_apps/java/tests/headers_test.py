import unittest
from bs4 import BeautifulSoup
import requests

class HeadersTest(unittest.TestCase):
    def setUp(self):
        self.client = requests
        self.url = "http://127.0.0.1:8080"
        self.resp = self.client.get(self.url+'/')
        self.headers = {}
        self._headers()

    def _headers(self):
        for h in self.resp.headers:
            if h[0] == 'X-Frame-Options':
                if h[0] in self.headers:
                    self.headers['X-Frame-Options'].append(h[1:])
                else:
                    self.headers['X-Frame-Options'] = [h[1:]]
            elif h[0] == 'X-XSS-Protection':
                if h[0] in self.headers:
                    self.headers['X-XSS-Protection'].append(h[1:])
                else:
                    self.headers['X-XSS-Protection'] = [h[1:]]
            elif h[0] == 'Referrer-Policy':
                if h[0] in self.headers:
                    self.headers['Referrer-Policy'].append(h[1:])
                else:
                    self.headers['Referrer-Policy'] = [h[1:]]
            elif h[0] == 'X-Content-Type-Options':
                if h[0] in self.headers:
                    self.headers['X-Content-Type-Options'].append(h[1:])
                else:
                    self.headers['X-Content-Type-Options'] = [h[1:]]
            elif h[0] == 'X-Permitted-Cross-Domain-Policies':
                if h[0] in self.headers:
                    self.headers['X-Permitted-Cross-Domain-Policies'].append(h[1:])
                else:
                    self.headers['X-Permitted-Cross-Domain-Policies'] = [h[1:]]
            elif h[0] == 'Expected-CT':
                if h[0] in self.headers:
                    self.headers['Expected-CT'].append(h[1:])
                else:
                    self.headers['Expected-CT'] = [h[1:]]

    def test_X_FRAME_OPTIONS(self):
        self.assertTrue('X-Frame-Options' in self.headers)

    def test_X_XSS_Protection(self):
        self.assertTrue('X-XSS-Protection' in self.headers)

    def test_Referrer_Policy(self):
        self.assertTrue('Referrer-Policy' in self.headers)

    def test_X_Content_Type_Options(self):
        self.assertTrue('X-Content-Type-Options' in self.headers)

    def test_X_Permitted_Cross_Domain_Policies(self):
        self.assertTrue('X-Permitted-Cross-Domain-Policies' in self.headers)

    def test_Expected_CT(self):
        self.assertTrue('Expected-CT' in self.headers)

if __name__ == '__main__':
    unittest.main()
