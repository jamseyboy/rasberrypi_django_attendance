# Generated by Django 3.0.6 on 2020-07-05 16:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('face_recognizer_app', '0005_auto_20200703_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance_model',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
