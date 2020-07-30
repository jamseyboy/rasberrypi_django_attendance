from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register.as_view()),
    path('testDb/',testDb.as_view()),
    path('getAttendance/',getAttendance.as_view())
]