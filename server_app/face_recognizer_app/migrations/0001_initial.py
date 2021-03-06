# Generated by Django 3.0.6 on 2020-06-27 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.EmailField(max_length=250)),
                ('rollNumber', models.CharField(max_length=20, unique=True)),
                ('phoneNumber', models.CharField(max_length=15, unique=True)),
                ('student_class', models.CharField(max_length=10)),
                ('folderLabel', models.CharField(max_length=20, unique=True)),
                ('nameRecog', models.CharField(max_length=20)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
