# Generated by Django 3.0.6 on 2020-06-27 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face_recognizer_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_model',
            name='stud_name',
            field=models.CharField(max_length=250),
        ),
    ]
