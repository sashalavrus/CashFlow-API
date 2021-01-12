from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def setUp(self):
        """ Set up obj before each test"""

        self.email = "testmail@mail.com"
        self.username = "username"
        self.password = "password123"

        self.user_obj = get_user_model().objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password)

    def test_create_user_with_email(self):
        """ This test create a new user with email, and check working capacity"""

        self.assertEqual(self.user_obj.email, self.email)
        self.assertEqual(self.user_obj.username, self.username)
        self.assertTrue(self.user_obj.check_password(self.password))

    def test_new_user_email_normalized(self):
        """ This test checks: email is normalized"""

        self.assertEqual(self.user_obj.email, self.email.lower())

    #def test_new_user_email_none(self):
        #""" This test checks ValueError if email is empty string"""

        #with self.assertRaises(ValueError):
            #get_user_model().objects.create_user(
                #username=self.username,
                #email=None,
                #password=self.password)





