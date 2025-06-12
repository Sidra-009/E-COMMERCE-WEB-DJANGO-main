# shop/tests.py
from django.test import TestCase, Client

class HomeTest(TestCase):
    def test_home_page(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)