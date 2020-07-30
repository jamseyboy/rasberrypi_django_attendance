from rest_framework import serializers
from face_recognizer_app.models import student_model
class stud_serialize(serializers.ModelSerializer):
    class Meta:
        model = student_model
        fields = "__all__"
