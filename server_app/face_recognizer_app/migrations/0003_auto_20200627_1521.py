# Generated by Django 3.0.6 on 2020-06-27 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('face_recognizer_app', '0002_auto_20200627_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_model',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
