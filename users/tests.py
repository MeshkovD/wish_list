from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient


class UserApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_model = get_user_model()

    def test_registration_hashes_and_hides_password(self):
        response = self.client.post('/api/v1/users/', {
            'username': 'new-user',
            'email': 'new@example.com',
            'password': 'Strong-pass-9384',
        }, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertNotIn('password', response.data)
        user = self.user_model.objects.get(username='new-user')
        self.assertTrue(user.check_password('Strong-pass-9384'))
        self.assertTrue(hasattr(user, 'profile'))

    def test_user_cannot_read_another_user(self):
        user = self.user_model.objects.create_user(username='first', password='Strong-pass-9384')
        other = self.user_model.objects.create_user(username='second', password='Strong-pass-9384')
        self.client.force_authenticate(user)

        own_response = self.client.get(f'/api/v1/users/{user.uuid}/')
        other_response = self.client.get(f'/api/v1/users/{other.uuid}/')
        list_response = self.client.get('/api/v1/users/')

        self.assertEqual(own_response.status_code, 200)
        self.assertNotIn('password', own_response.data)
        self.assertEqual(other_response.status_code, 404)
        self.assertEqual(list_response.status_code, 405)
