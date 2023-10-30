from typing import Any
from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from .models import Reservations, Menu, Image, FoodCategories
import datetime
from rest_framework import filters
from django.core.management import BaseCommand
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import ReservationsSerializer, MenuSerializer, ImageSerializer, FoodCategoriesSerializer
from .permissions import IsStaffEditor
from rest_framework_simplejwt import authentication as jwtauthentication

# Create your views here.
class Reservationviews(generics.ListCreateAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["ticket_number", "name"]
    # lookup_field = 'ticket_number'
    def perform_create(self, serializer):
        date = serializer.validated_data.get('date')
        print(date)
        print(datetime.date.today())
        if date < datetime.date.today():
            raise serializers.ValidationError({'error':"Invalid date - date in the past"})
        serializer.save(date=date)
        

class ReservationDetailViews(generics.RetrieveDestroyAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    lookup_field = 'ticket_number'

    # def perform_destroy(self, instance):
    #     expiration_time = instance.expiration

    #     if expiration_time is True:
    #         instance.delete()
    #         return Response("This ticket is deleted")
    #     else:
    #         return Response("This ticket has not expired")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        expiration = instance.expiration

        if expiration is True:
            instance.delete()
            return Response("This ticket is deleted")
        else:
            return Response("This hasn't expirer")

        return super().destroy(request, *args, **kwargs)
    
   

class MenuListCreatViews(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [
                              jwtauthentication.JWTAuthentication,
                              authentication.SessionAuthentication
                              ]
    permission_classes = [IsStaffEditor]

class MenuRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [
        jwtauthentication.JWTAuthentication,
        authentication.SessionAuthentication,
                              
                              ]
    permission_classes = [IsStaffEditor]
    # lookup_field = 'menu'

class ImageViews(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [
        jwtauthentication.JWTAuthentication,
        authentication.SessionAuthentication,
                              
                              ]
    permission_classes = [IsStaffEditor]
    
class ImageDetailViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [
        jwtauthentication.JWTAuthentication,
        authentication.SessionAuthentication,
                              
                              ]
    permission_classes = [IsStaffEditor]

class FoodCategoryViews(generics.ListCreateAPIView):
    queryset = FoodCategories.objects.all()
    serializer_class = FoodCategoriesSerializer
    permission_classes = [IsStaffEditor]
    authentication_classes = [
        jwtauthentication.JWTAuthentication,
        authentication.SessionAuthentication,
    ]

class FoodCategoriesDetailViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodCategories.objects.all()
    serializer_class = FoodCategoriesSerializer
    permission_classes = [IsStaffEditor]
    authentication_classes = [
        jwtauthentication.JWTAuthentication,
        authentication.SessionAuthentication,
    ]