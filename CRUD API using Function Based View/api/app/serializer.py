from app.models import Teacher
from rest_framework import serializers

class TeacherSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    salary = serializers.IntegerField()
    def create(self,validated_data):
        return Teacher.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.full_name = validated_data.get('full_name',instance.full_name)
        instance.address = validated_data.get('address',instance.address)
        instance.salary = validated_data.get('salary',instance.salary)
        instance.save()
        return instance
