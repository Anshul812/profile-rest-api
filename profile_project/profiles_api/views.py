from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets 
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self , request , format=None):
        """Returns a list of API features"""
        an_apiView = [
            'Uses Http Methods',
            'Similar to Django View',
            'Takes control over url'
        ]

        return Response({'message':'Hello!' , 'apiView':an_apiView})


    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    
    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSets(viewsets.ViewSet):
    """Test viewset API"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        
        a_viewset = [
            'actions like list , create , destroy , retrieve , update , partial_update',
            'automatic map to urls using routers',
            'more funcclationality and less code'
        ]
        return Response({'message':'Hello' , 'a_viewset':a_viewset})

    
    def create(self , request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self , request, pk=None):
        """Handling object by its ID"""
        return Response({'http_response':'GET'})

    
    def update(self, request, pk=None):
        """Handling update of object"""
        return Response({'http_response':'PUT'})

    def partial_update(self, request, pk=None):
        """Handling update of object"""
        return Response({'http_response':'PATCH'})

    def delete(self, request, pk=None):
        """Handling update of object"""
        return Response({'http_response':'DELETE'})

    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handling creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)