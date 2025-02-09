"""
Tests for Model
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Tests for Model"""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email"""
        email = 'test@gmail.com'
        password = 'pass123'
        user =get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email normalized"""
        sample_email = [
            ['test@gmail.com', 'test@gmail.com'],
            ['test3@gmail.com', 'test3@gmail.com'],
            ['test4@gmail.com', 'test4@gmail.com'],
            ['test5@gmail.com', 'test5@gmail.com'],
            ['test6@gmail.com', 'test6@gmail.com']
        ]
        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email, 'pass123')
            self.assertEqual(user.email, expected)

    def test_new_without_email(self):
      """user without email"""
      with self.assertRaises(ValueError):
          get_user_model().objects.create_user('', 'pass123')

    def test_create_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'user@gmail.com',
            'user123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
