from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class TestApi(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api(self):
        response = self.client.get('/api/')

        expected = {
            'Name': 'Sahel Market',
            'Latitude': 49.264579,
            'Longitude': -123.176254
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)
