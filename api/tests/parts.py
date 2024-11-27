from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Part


class PartAPITestCase(APITestCase):
    def test_create_part(self):
        """Parça ekleme işlemi testi"""
        data = {
            'name': 'Part 1',
            'description': 'This is a description for Part 1.',
            'aircraft': 'Aircraft 1',
            'team': 'Team A',
        }
        response = self.client.post(self.url, data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])

    def test_get_parts(self):
        """Parçaların listelenmesi testi"""
        Part.objects.create(name='Part 1', description='Description for Part 1', aircraft='Aircraft 1', team='Team A')
        Part.objects.create(name='Part 2', description='Description for Part 2', aircraft='Aircraft 2', team='Team B')
        response = self.client.get(self.url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_part(self):
        """Tek bir parçanın getirilmesi testi"""
        part = Part.objects.create(name='Part 1', description='Description for Part 1', aircraft='Aircraft 1', team='Team A')
        response = self.client.get(f'{self.url}{part.id}/', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], part.name)

    def test_delete_part(self):
        """Parçanın silinmesi testi"""
        part = Part.objects.create(name='Part 1', description='Description for Part 1', aircraft='Aircraft 1', team='Team A')
        response = self.client.delete(f'{self.url}{part.id}/', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Silinen parçanın tekrar listede olmaması gerekir
        response = self.client.get(self.url, **self.headers)
        self.assertEqual(len(response.data), 0)
