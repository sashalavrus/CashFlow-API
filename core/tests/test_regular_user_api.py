from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('core:signup')
GENERATE_USER_TOKEN = reverse('core:token')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class CRUDRegUserTest(TestCase):
    """This class test Creation, Updating, Delete and Reading regular user"""

    def setUp(self):
        self.client = APIClient()
        self.payload = {
            "username": "user",
            "email": "test@mail.com",
            "password": "qwerty123",
            }

    def test_create_user(self):
        """Creation regular user"""

        res = self.client.post(CREATE_USER_URL, self.payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(self.payload['password']))
        self.assertNotIn('password', res.data)

    def test_create_exists_user(self):
        """Test checks that you can't create already existing user"""

        create_user(**self.payload)

        res = self.client.post(CREATE_USER_URL, self.payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_user(self):
        """Test checks if token has been created for user"""

        create_user(**self.payload)

        res = self.client.post(GENERATE_USER_TOKEN, self.payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_with_invalid_credentials(self):
        """Test checks if token has not been created for user with invalid credentials"""

        create_user(**self.payload)
        self.payload.update({"password": 'invalid_password'})

        res = self.client.post(GENERATE_USER_TOKEN, self.payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_with_no_user(self):
        """Test checks if token has not been created for not created user"""

        res = self.client.post(GENERATE_USER_TOKEN, self.payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

