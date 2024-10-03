from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from board.models.board import Board


User = get_user_model()


class UserAuthenticationViewTests(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='random_user', email='testuser@example.com', password='testpassword'
        )

    def test_user_registration(self):
        """Test that a user can register successfully."""
        response = self.client.post(reverse('user_registration'), {
            'username': 'new_user',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        if response.status_code == 200:
            # Print the form errors to help debug why registration failed
            print(response.content.decode())
        if response.status_code == 400:
            print(response.context['form'].errors)

        # Check if the user was created
        self.assertEqual(response.status_code, 302)  # Redirect to home page after registration
        self.assertTrue(User.objects.filter(username='new_user').exists())

    def test_default_board_assigned_on_user_creation(self):
        user = User.objects.create_user(username='testuser', password='testpassword')

        self.assertTrue(Board.objects.filter(user=user, default=True).exists(), "User should have a default board assigned on creation")

        # Additional checks to ensure the default board has correct properties
        default_board = Board.objects.get(user=user, default=True)
        self.assertEqual(default_board.name, "testuser's Default Board", "The default board should have the correct name")
