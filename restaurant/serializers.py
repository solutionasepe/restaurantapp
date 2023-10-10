from rest_framework import serializers
from .models import *
import random 
import string
class ReservationsSerializer(serializers.ModelSerializer):
    ticket_number = serializers.CharField(read_only=True)

    class Meta:
        model = Reservations
        fields = "__all__"

    def create(self, validated_data):
        while True:
            ticket_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

            if not Reservations.objects.filter(ticket_number=ticket_number).exists():
                break

        validated_data['ticket_number'] = ticket_number
        reservation = Reservations.objects.create(**validated_data)
        return reservation



class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"

class FoodCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodCategories
        fields = "__all__"