from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email(self):
        '''Tet creating a new user with an email is sucessfull'''
        email = 'test@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password

        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_is_normalize(self):

        email = 'test@DEV.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_email_field_not_empty(self):
        '''Raises Error if email is not provided'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_create_super_user(self):
        '''Test Creating a new Super USer'''
        user = get_user_model().objects.create_super_user(
            'vj"dev.com',
            'tst123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
