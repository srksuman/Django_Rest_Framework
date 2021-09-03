from .serializer import TeacherSerializer
from .models import Teacher
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


class TeacherAPI(APIView):
    def get(self,request,id=None,format=None):
        if id is not None:
            obj = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(obj)
        else:
            obj = Teacher.objects.all()
            serializer = TeacherSerializer(obj,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        dt = request.data
        serializer = TeacherSerializer(data = dt)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Detail is posted!'})
        else:
            return Response({'message':'Something went wrong'})
    
    def put(self,request,format=None):
        data = request.data
        id = request.data.get('id')
        obj = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data is updated completely!!'})
        else:
            return Response(serializer.errors)

    def patch(self,request,format=None):
        data = request.data
        id = request.data.get('id')
        obj = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data is updated partially!!'})
        else:
            return Response(serializer.errors)

    def delete(self,request,id=None,format=None):
        if id is not None:
            obj = Teacher.objects.get(id = id)
            obj.delete()
            return Response({"message":"Data is deleted successfully!"})
        else:
            return Response({"message":"Data is deleted not deleted!"})
    



