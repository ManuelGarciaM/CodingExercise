from rest_framework.response import Response

from rest_framework.views import APIView


class POIList(APIView):
    def get(self, request, format=None):
        # If this were a real application, this would be in the database
        poi = {
            'Name': 'Sahel Market',
            'Latitude': 49.264579,
            'Longitude': -123.176254
        }
        return Response(poi)
