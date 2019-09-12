from rest_framework.response import Response

from rest_framework.views import APIView


class POIList(APIView):
    def get(self, request):
        # If this were a real application, this would be in the database
        poi = {
            'name': 'Sahel Market',
            'location': [-123.176254, 49.264579],
        }
        return Response(poi)
