from rest_framework import serializers

class TeacherSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    salary = serializers.BigIntegerField()
    