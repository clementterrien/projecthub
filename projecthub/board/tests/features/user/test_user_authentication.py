from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class UserAuthenticationViewTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='random_user', email='testuser@example.com', password='testpassword'
        )

    def test_user_login(self):
        """Test that a user can log in with valid credentials."""
        response = self.client.post(reverse('user_login'), {
            'username': 'random_user',  # Username field corresponds to email in our setup
            'password': 'testpassword',
        })

        # Check if login is successful and user is redirected
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('home'))  # Check redirection to home
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_user_logout(self):
        """Test that a logged-in user can log out successfully."""
        # Log in the user
        self.client.login(email='testuser@example.com', password='testpassword')

        # Log out the user
        response = self.client.post(reverse('user_logout'))
        self.assertEqual(response.status_code, 302)  # Check for redirect after logout
        self.assertEqual(response.url, reverse('home'))  # Should redirect to home
        self.assertFalse(response.wsgi_request.user.is_authenticated)  # User should be logged out
