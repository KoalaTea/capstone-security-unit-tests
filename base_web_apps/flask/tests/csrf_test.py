import unittest
from exampleapp import create_app
from bs4 import BeautifulSoup

class CSRFTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def csrf(self, endpoint, data, fail_text, success_text, fail_status_code, success_status_code):
            # verify data fails without csrf_token
            resp = self.client.post(endpoint, data=data)
            soup = BeautifulSoup(resp.data, 'html.parser')
            # assert success text not present without csrf_token TODO
            # assert fail conditions are present without csrf_token
            if fail_text:
                self.assertEqual(soup.find(text=fail_text), fail_text)
            if fail_status_code:
                self.assertEqual(resp.status_code, fail_status_code)
            # verify csrf token works
            resp = self.client.get(endpoint)
            soup = BeautifulSoup(resp.data, 'html.parser')
            csrf_token = soup.find('input', {'id': 'csrf_token'})['value']
            # what if there is no csrf_token at all in the text? TODO
            login_data['csrf_token'] = csrf_token
            resp = self.client.post(endpoint, data=data)
            # assert fail conditions are missing TODO
            # assert success conditions are present with csrf_token
            if success_text:
                self.assertEqual(soup.find(text=success_text), success_text)
            if success_status_code:
                self.assertEqual(resp.status_code, success_status_code)


    def test_csrf(self):
        # pages that will be tested
        pages = [
                {'endpoint': '/add', 'data': {'data': 'test'}, 'fail_text': 'failed',
                 'success_text': 'success', 'fail_status_code': None, 'success_status_code': None}
            ]
        for page in pages:
            self.csrf(page['endpoint'], page['data'], page['fail_text'], page['success_text'],
                      page['fail_status_code'], page['success_status_code'])
