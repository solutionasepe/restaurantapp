# Generated by Django 4.2.6 on 2023-10-30 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_reservations_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 30, 14, 49, 58, 372190)),
        ),
    ]
