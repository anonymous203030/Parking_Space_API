from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import BookTime
from user.models import User


class BookingTests(APITestCase):
    def setUp(self) -> None:
        self.book_time_query = {'floor': -1, 'parking_space_id': 23, 'booking_start_time': '2020-01-02',
                                'booking_end_time': '2021-01-02'}
        self.b_t_create = reverse('create_book_time')
        self.b_t_list = reverse('list_book_time')
        self.r_t_create = reverse('reserve_create')
        self.r_t_list = reverse('reserve_list')

    def test_book_time(self):
        # Test Manager book_time creation
        user = User.objects.create(email='test@gmail.com', password='12345678', profession='M')
        user.save()
        self.client.force_login(user)
        r = self.client.post(self.b_t_create, self.book_time_query)
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)

        # parking_space_id unique test
        r = self.client.post(self.b_t_create, self.book_time_query)
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)

        self.client.logout()
        # AnonymousUser cannot access test
        r = self.client.post(self.b_t_create, self.book_time_query)
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)

        # Employee cannot create BookTime test
        user.profession = 'E'
        user.save()
        self.client.force_login(user)
        self.book_time_query['parking_space_id'] = 24
        r = self.client.post(self.b_t_create, self.book_time_query)
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)

        # Test booking end time
        user.profession = 'M'
        user.save()
        self.client.force_login(user)
        self.book_time_query['parking_space_id'] = 25
        self.book_time_query['booking_end_time'] = '2000-12-12'
        r = self.client.post(self.b_t_create, self.book_time_query)
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)

    def test_reserve(self):
        b_t_1 = BookTime.objects.create(floor=-1, parking_space_id=200,
                                        booking_start_time='2020-01-01', booking_end_time='2021-01-01')
        b_t_1.save()

        user_1 = User.objects.create(username='test1', email='test1@mail.com', password='12345678', profession='E')
        user_1.save()

        self.client.force_login(user_1)
        r = self.client.post(self.r_t_create, {"book_time": b_t_1.id})
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)

        # book_time UNIQUE test
        r = self.client.post(self.r_t_create, {"book_time": b_t_1.id})
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)

