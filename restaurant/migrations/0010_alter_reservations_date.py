# Generated by Django 4.2.6 on 2023-11-12 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_alter_reservations_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 12, 12, 12, 32, 946472)),
        ),
    ]