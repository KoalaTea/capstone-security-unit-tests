import unittest
from exampleapp import create_app
from bs4 import BeautifulSoup
import re
import requests

class CSRFTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TESTING=True)
        self.app.debug = True
        self.client = requests

    def csrf(self, endpoint, data, fail_text, success_text, fail_status_code, success_status_code):
            # assert token exists
            resp = self.client.get(endpoint)
            soup = BeautifulSoup(resp.data, 'html.parser')
            csrf_token = soup.find('input', {'id': 'csrf_token'})
            self.assertIsNotNone(csrf_token)
            # verify data fails without csrf_token
            resp = self.client.post(endpoint, data=data)
            resp = self.client.post(endpoint, data=data)
            soup = BeautifulSoup(resp.data, 'html.parser')
            # assert fail conditions are present without csrf_token
            if fail_text:
                self.assertIsNotNone(soup.find(text=re.compile(fail_text)))
            if fail_status_code:
                self.assertEqual(resp.status_code, fail_status_code)
            # asset success conditions are not presentn without crsf_token
            if success_text:
                self.assertIsNone(soup.find(text=re.compile(success_text)))
            if success_status_code:
                self.assertNotEqual(resp.status_code, success_status_code)
            # verify csrf token works
            data['csrf_token'] = csrf_token['value']
            resp = self.client.post(endpoint, data=data, follow_redirects=True)
            soup = BeautifulSoup(resp.data, 'html.parser')
            # assert success conditions are present with csrf_token
            if success_text:
                self.assertIsNotNone(soup.find(text=re.compile(success_text)))
            if success_status_code:
                self.assertEqual(resp.status_code, success_status_code)
            # assert fail conditions are not present with csrf_token
            if fail_text:
                self.assertIsNone(soup.find(text=re.compile(fail_text)))
            if success_status_code:
                self.assertNotEqual(resp.status_code, fail_status_code)


    def test_csrf(self):
        # pages that will be tested
        pages = [
                {'endpoint': '/add', 'data': {'data': 'test'}, 'fail_text': 'failed',
                 'success_text': 'success', 'fail_status_code': None, 'success_status_code': None}
            ]
        for page in pages:
            self.csrf(page['endpoint'], page['data'], page['fail_text'], page['success_text'],
                      page['fail_status_code'], page['success_status_code'])

if __name__ == '__main__':
    unittest.main()
