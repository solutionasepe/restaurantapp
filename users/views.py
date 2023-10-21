from django.shortcuts import render
from .models import User
from .serializers import UserSerializers
from rest_framework import generics, authentication
from rest_framework_simplejwt import authentication as jwtauthentication
from restaurant.permissions import IsStaffEditor
# Create your views here.

class userview(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class userDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field ='username'
    authentication_classes = [
        jwtauthentication.JWTAuthentication,
        authentication.SessionAuthentication,                
                              ]
    permission_classes = [IsStaffEditor]