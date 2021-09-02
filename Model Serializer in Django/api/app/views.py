from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import re
from .serializer import TeacherSerializer
from .models import Teacher
import io
from rest_framework.parsers import JSONParser
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class TeacherAPI(View):
    def get(self,request,*ar,**arg):
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
    
    def post(self,request,*arg,**args):
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        serializer = TeacherSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Data is post successfully'})
        else:
            return JsonResponse(serializer.errors)

    def put(self,request,*arg,**args):
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        obj = Teacher.objects.get(id = id)
        print(obj)
        print(obj.full_name)
        serializer = TeacherSerializer(obj,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            obj = Teacher.objects.get(id = id)
            return JsonResponse({'message':'Data is updated successfully!'})
        else:
            return JsonResponse(serializer.errors)
    
    def delete(self,request,*arg,**args):
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        obj = Teacher.objects.get(id = python_data.get('id'))
        if python_data.get('id') is not None:
            obj.delete()
            return JsonResponse({'Message':'Data is deleted successfully! '})
        else:
            return JsonResponse({'Message':'Cannot delete!'})