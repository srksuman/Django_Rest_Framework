from .serializer import TeacherSerializer
from .models import Teacher
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def teacherAPI(request,id=None):
    if request.method == 'GET':
        if id is not None:
            obj = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(obj)
        else:
            obj = Teacher.objects.all()
            serializer = TeacherSerializer(obj,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        dt = request.data
        serializer = TeacherSerializer(data = dt)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Detail is posted!'})
        else:
            return Response({'message':'Something went wrong'})
    
    if request.method == 'PUT':
        data = request.data
        id = request.data.get('id')
        obj = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data is updated completely!!'})
        else:
            return Response(serializer.errors)

    if request.method == 'PATCH':
        data = request.data
        id = request.data.get('id')
        obj = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data is updated partially!!'})
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        if id is not None:
            obj = Teacher.objects.get(id = id)
            obj.delete()
            return Response({"message":"Data is deleted successfully!"})
        else:
            return Response({"message":"Data is deleted not deleted!"})
    



