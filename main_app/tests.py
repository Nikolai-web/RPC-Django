from django.test import TestCase, Client
from django.urls import reverse


class JsonRPCTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_auth_check(self):
        response = self.client.post(reverse('jsonrpc'), {'method': 'auth.check', 'params': '{}'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.context['response_data'])

    def test_string_params(self):
        response = self.client.post(reverse('jsonrpc'), {'method': 'auth.check', 'params': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.context['response_data'])

    def test_dict_params(self):
        response = self.client.post(reverse('jsonrpc'), {'method': 'auth.check', 'params': '{"1": 1}'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.context['response_data'])



