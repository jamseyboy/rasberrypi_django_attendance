# Generated by Django 3.0.6 on 2020-08-05 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_recognizer_app', '0011_auto_20200731_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_model',
            name='created_time',
            field=models.TimeField(default=datetime.time(17, 24)),
        ),
    ]
