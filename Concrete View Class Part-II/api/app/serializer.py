from django.db.models import fields
from app.models import Teacher
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','full_name','salary','address']
    

