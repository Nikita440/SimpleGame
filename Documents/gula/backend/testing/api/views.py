from rest_framework_simplejwt.settings import api_settings
from typing import Any
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
# auth_app/views.py
from .service import ManageUser
from rest_framework.renderers import JSONRenderer
from .serializer import SerializerForUserInfo
from django.contrib.auth.decorators import user_passes_test
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import TokenRefreshSerializer,TokenResponseSerializer,Serializename
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import UserRegistrationSerializer
from django.shortcuts import render, redirect
# your_app/views.py

from ..models import UserInfo, Shop,Position
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



import json
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username       
        token['role'] = "Buyer"
        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class =  MyTokenObtainPairSerializer



@api_view(['GET'])
def routes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
        

    ]
    return Response(routes)

@api_view(['POST'])
def register(request):
    new_name = request.data.get('name')
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
        

        # Save the user info with the name
        user_info = UserInfo(user=user,name=new_name)
        user_info.save()
        
        # Generate JWT token for the registered user and send it as a response
        token = RefreshToken.for_user(user)
        return Response({'token': str(token.access_token)}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getuserinfo(request):

    user = request.user
    infos = UserInfo.objects.filter(user=user)
    serializer = SerializerForUserInfo(infos,many=True)
    return Response(serializer.data)
@api_view(['PATCH'])

def changename(request):
    
    User = ManageUser()

    user = request.user
    
    # Get the new name from the request data
    new_name = request.data.get('name')
    
    User.changeName(new_name,user)
        
    return Response({'message': 'Name updated successfully'})
    
    

    #userinfochange = UserInfo(user=user,name=name)
    #userinfochange.save()
#def createShop():
#    Shop.objects.create("myShop",,10,)


