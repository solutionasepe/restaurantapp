from rest_framework import serializers
from .models import *
import random 
import os
import string
import smtplib
from django.db import transaction
my_email = os.getenv('EMAIL_HOST_USER')
password = os.getenv('EMAIL_HOST_PASSWORD')

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

        try:
            with transaction.atomic():
                reservation = Reservations.objects.create(**validated_data)

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
                    connection.ehlo()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(
                        from_addr=my_email, to_addrs=validated_data['email'],
                        msg="Subject:weldone\n\n Congratuations you have booked a table with ticket number: {}".format(ticket_number)
                    )
        except Exception:
            reservation.delete()
            
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