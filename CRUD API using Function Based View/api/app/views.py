from django.shortcuts import render
from django.http import JsonResponse
import io
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from.models import Teacher
from rest_framework.parsers import JSONParser
from .serializer import TeacherSerializer
from django.views.decorators.csrf import csrf_exempt
from .serializer import TeacherSerializer

# Create your views here.


@csrf_exempt
def apiFunction(request):
    if request.method == 'GET':
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            get_data = Teacher.objects.get(id= id)
            serializer = TeacherSerializer(get_data)
        else:
            get_data = Teacher.objects.all()
            serializer = TeacherSerializer(get_data,many=True)
        return JsonResponse({'success':serializer.data})

    if request.method == 'POST':
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        serializer = TeacherSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Data is post successfully'})
        else:
            return JsonResponse(serializer.errors)

        

