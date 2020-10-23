from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self , request , format=None):
        """Returns a list of API features"""
        an_apiView = [
            'Uses Http Methods',
            'Similar to Django View',
            'Takes control over url'
        ]

        return Response({'message':'Hello!' , 'apiView':an_apiView})
