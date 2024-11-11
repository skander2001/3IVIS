from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class AuthTests(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_login_view(self):
        # Test the login page loads correctly
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        # Test login with correct credentials
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'})
        self.assertRedirects(response, reverse('chart-view'))

    def test_logout_view(self):
        # First, log in the user
        self.client.login(username='testuser', password='password123')

        # Test the logout page works
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))

    def test_access_protected_chart_view(self):
        # Test accessing chart without login (should redirect to login)
        response = self.client.get(reverse('chart-view'))
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('chart-view'))

        # Now log in and test access to chart page
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('chart-view'))
        self.assertEqual(response.status_code, 200)
