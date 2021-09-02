from app.models import Teacher
from rest_framework import serializers

class TeacherSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    salary = serializers.IntegerField()
    def create(self,validated_data):
        return Teacher.objects.create(**validated_data)