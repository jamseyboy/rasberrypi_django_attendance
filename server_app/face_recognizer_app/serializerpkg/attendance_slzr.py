from rest_framework import serializers
from face_recognizer_app.models import attendance_model


class attendance_serialize(serializers.ModelSerializer):
    class Meta:
        model=attendance_model
        fields= "__all__"