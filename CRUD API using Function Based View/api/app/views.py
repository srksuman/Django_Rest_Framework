from django.shortcuts import render
from django.http import JsonResponse
import io

from rest_framework import serializers
from.models import Teacher
from rest_framework.parsers import JSONParser
from .serializer import TeacherSerializer
# Create your views here.

def apiFunction(request):
    if request.method == 'GET':
        data_json = request.body
        stream = io.BytesIO(data_json)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            get_data = Teacher.objects.get(id= id)
            serializer = TeacherSerializer(get_data)
        else:
            get_data = Teacher.objects.all()
            serializer = TeacherSerializer(get_data,many=True)
        return JsonResponse({'success':serializer.data})
        

