from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from wishes.models import WishList


class WishApiTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username='first', password='Strong-pass-9384')
        self.other = user_model.objects.create_user(username='second', password='Strong-pass-9384')
        self.wish_list = WishList.objects.create(user=self.user)
        self.other_wish_list = WishList.objects.create(user=self.other)
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_lists_are_limited_to_owner(self):
        response = self.client.get('/api/v1/wishlists/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['uuid'], str(self.wish_list.uuid))
        self.assertNotIn('user', response.data[0])

    def test_other_list_is_not_available(self):
        response = self.client.get(f'/api/v1/wishlists/{self.other_wish_list.uuid}/')
        self.assertEqual(response.status_code, 404)

    def test_wish_cannot_be_added_to_other_list(self):
        response = self.client.post('/api/v1/wishes/', {
            'wish_list': str(self.other_wish_list.uuid),
            'product': None,
        }, format='json')
        self.assertEqual(response.status_code, 403)

    def test_owner_can_create_list_and_wish(self):
        list_response = self.client.post('/api/v1/wishlists/', {}, format='json')
        self.assertEqual(list_response.status_code, 201)
        self.assertEqual(WishList.objects.get(uuid=list_response.data['uuid']).user, self.user)

        wish_response = self.client.post('/api/v1/wishes/', {
            'wish_list': list_response.data['uuid'],
            'product': None,
        }, format='json')
        self.assertEqual(wish_response.status_code, 201)

    def test_authentication_is_required(self):
        self.client.force_authenticate(None)
        response = self.client.get('/api/v1/wishlists/')
        self.assertIn(response.status_code, (401, 403))
