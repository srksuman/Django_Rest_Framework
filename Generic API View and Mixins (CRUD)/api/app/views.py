from .serializer import TeacherSerializer
from .models import Teacher
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.

class ListTeacherAPIGP(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    def get(self,request,*arg,**kwargs):
        return self.list(request,*arg,**kwargs)

    def post(self,request,*arg,**kwargs):
        return self.create(request,*arg,**kwargs)

    

class ListTeacherAPIPRD(UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin,GenericAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

