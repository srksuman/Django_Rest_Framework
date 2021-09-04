from .serializer import TeacherSerializer
from .models import Teacher
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
# Create your views here.


class ListTeacherAPI(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CreateTeacherAPI(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class RetriveTeacherAPI(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class UpdateTeacherAPI(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class DestroyTeacherAPI(DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer