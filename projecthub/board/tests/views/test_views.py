from django.test import TestCase
from django.urls import reverse


class ViewsTests(TestCase):

    def test_user_registration_view(self):
        response = self.client.get(reverse('user_registration'))
        self.assertEqual(response.status_code, 200)

    def test_user_login_view(self):
        response = self.client.get(reverse('user_login'))
        self.assertEqual(response.status_code, 200)
