from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        """Set up initial data for testing"""
        self.registration_url = reverse('register')
        self.valid_user_data = {
            'username': 'testuser',
            'first_name': 'testfname',
            'last_name': 'testlname',
            'email': 'testuser@example.com',
            'phone_number': '09777 555666',
            'password1': 'Test@1234',
            'password2': 'Test@1234',
        }
        self.invalid_user_data = {
            'username': '',  # Missing username
            'first_name': '',
            'last_name': '',
            'email': 'invalid-email',  # Invalid email format
            'phone_number': '',
            'password1': 'Test@1234',
            'password2': 'Mismatch@5678',  # Password mismatch
        }

    def test_successful_registration(self):
        """Test user can register with valid details"""
        response = self.client.post(self.registration_url, self.valid_user_data)
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful registration
        self.assertTrue(User.objects.filter(username='testuser').exists())  # Check if user is created

    def test_registration_with_invalid_data(self):
        """Test registration fails with invalid data"""
        response = self.client.post(self.registration_url, self.invalid_user_data)
        self.assertEqual(response.status_code, 200)  # Should return to the registration page
        self.assertFalse(User.objects.filter(email='invalid-email').exists()) # Check if user is created
        