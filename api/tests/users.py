from rest_framework.test import APITestCase
from rest_framework import status
from authentication.models import User
from rest_framework.authtoken.models import Token


class UserAPITestCase(APITestCase):
    def setUp(self):
        """Kullanıcılar için test verileri oluşturma"""
        self.user_data = {
            'email': 'testuser@test.com',
            'password': 'testpassword123'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.token = Token.objects.create(user=self.user)
        self.url = '/api/users/'
        self.headers = {'Authorization': f'Bearer {self.token.key}'}

    def test_create_user(self):
        """Yeni bir kullanıcı oluşturulması testi"""
        data = {'email': 'newuser@test.com', 'password': 'newpassword123'}
        response = self.client.post(self.url, data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])

    def test_login_user(self):
        """Kullanıcının giriş yapması testi"""
        data = {'email': self.user_data['email'], 'password': self.user_data['password']}
        response = self.client.post('/api/auth/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
