from django.db import IntegrityError, transaction
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import User


class AccountTests(APITestCase):
    def setUp(self) -> None:
        # User Tests
        self.user_query = {"username": 'test_1', "email": 'test1@example.com', 'password': '12345678',
                           'profession': 'E'}
        self.create = reverse('user_register')
        self.auth_login = reverse('user_login')
        # Profile Tests
        self.profile_query = {"first_name": "string",
                              "last_name": "string",
                              "about": "string",
                              "birthday": "2021-12-15",
                              "gender": "M"}
        self.profile_create = reverse('profile_create')
        self.profile_list = reverse('profile_list')
        self.user = User.objects.create(email='test@gmail.com', password='12345678', username='helloworld',
                                        profession='E')
        self.user.save()

        # self.profile_update = reverse('profile_update')

    def test_create_account(self):
        r = self.client.post(self.create, self.user_query)
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        # Unique test
        r = self.client.post(self.create, self.user_query)
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        # EmailField test
        self.user_query['email'] = 'abcd'
        r = self.client.post(self.create, self.user_query)
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        # password 8 characters test
        self.user_query['email'] = 'test_3@example.com'
        self.user_query['password'] = '1234567'
        r = self.client.post(self.create, self.user_query)
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_account(self):
        # User login test

        self.client.post(self.create, self.user_query)
        r = self.client.post(self.auth_login, {'email': self.user_query['email'],
                                               'password': self.user_query['password']})
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        r = self.client.post(self.auth_login, {'email': 'smthing@example.com',
                                               'password': self.user_query['password']})
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)
        r = self.client.post(self.auth_login, {'email': 'something',
                                               'password': self.user_query['password']})
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)

    def test_profile(self):
        # PROFILE CREATION TEST

        # Create User
        user = User.objects.create(username='test_2', email='test_2@gmail.com', password='12345678')

        # Login client
        self.client.force_login(user)
        response = self.client.post(self.profile_create, self.profile_query)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test OneToOneField
        try:
            with transaction.atomic():
                self.client.post(self.profile_create, self.profile_query)
        except IntegrityError:
            pass
        user_2 = User.objects.create(username='test_3', email='test_3@gmail.com', password='12345678')
        user_2.save()
        # Profile creation test

        self.client.logout()
        response = self.client.post(self.profile_create, self.profile_query)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # END PROFILE CREATION TEST

        # Profile List

        # IsAuthenticated test
        response = self.client.get(self.profile_list)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.force_login(user)
        response = self.client.get(self.profile_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
