from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from .models import Reservations, Menu, Image, FoodCategories
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import ReservationsSerializer, MenuSerializer, ImageSerializer, FoodCategoriesSerializer
from .permissions import IsStaffEditor

# Create your views here.
class Reservationviews(generics.ListCreateAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
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

class MenuListCreatViews(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditor]

class MenuRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditor]
    # lookup_field = 'menu'

class ImageViews(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditor]
    
