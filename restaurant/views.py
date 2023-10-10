from django.shortcuts import render
from rest_framework import generics
from .models import Reservations, Menu, Image, FoodCategories
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import ReservationsSerializer, MenuSerializer, ImageSerializer, FoodCategoriesSerializer


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
    
