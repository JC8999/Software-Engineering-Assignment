from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class AuthenticationTests(TestCase):
    def setUp(self):
        """Set up test user"""
        self.user = User.objects.create_user(username='testuser', email="testuser@example.com", password='Test@1234')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.protected_url = reverse('dashboard')

    def test_successful_login(self):
        """Test user can log in with correct credentials"""
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'Test@1234'})
        self.assertEqual(response.status_code, 302)  # Should redirect after login
        self.assertTrue('_auth_user_id' in self.client.session)  # User should be logged in

    def test_failed_login(self):
        """Test login fails with incorrect credentials"""
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'WrongPassword123!'})
        self.assertEqual(response.status_code, 200)  # Should stay on the login page
        self.assertFalse('_auth_user_id' in self.client.session)  # User should not be logged in

    def test_logout(self):
        """Test user logout functionality"""
        self.client.login(username='testuser', password='Test@1234')
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Should redirect after logout
        self.assertFalse('_auth_user_id' in self.client.session)  # Session should be cleared

    def test_protected_page_without_login(self):
        """Test access to protected page without login"""
        response = self.client.get(self.protected_url)
        self.assertNotEqual(response.status_code, 200)  # Should be redirected to login

    def test_protected_page_after_login(self):
        """Test access to protected page after login"""
        self.client.login(username='testuser', password='Test@1234')
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, 200)  # Should access successfully after login
