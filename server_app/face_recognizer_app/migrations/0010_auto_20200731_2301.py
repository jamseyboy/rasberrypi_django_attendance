# Generated by Django 3.0.6 on 2020-07-31 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_recognizer_app', '0009_auto_20200730_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_model',
            name='created_time',
            field=models.TimeField(default=datetime.time(23, 1)),
        ),
    ]
