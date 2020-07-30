from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class student_model(models.Model):
    stud_name=models.CharField(max_length=250)
    rollNumber=models.CharField(max_length=20,unique=True)
    phoneNumber=models.CharField(max_length=15,unique=True)
    student_class=models.CharField(max_length=10)
    folderLabel=models.CharField(max_length=20,unique=True)
    nameRecog=models.CharField(max_length=20)
    created_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.rollNumber,self.phoneNumber

class attendance_model(models.Model):

    stud_name=models.CharField(max_length=250)
    rollNumber=models.CharField(max_length=20,unique=True)
    label=models.IntegerField(unique=True)
    created_date=models.DateField(default=datetime.date.today)
    created_time=models.TimeField(default=datetime.time(16,00))

    def __str__(self):
        return self.stud_name,self.rollNumber,self.created_date,self.created_time