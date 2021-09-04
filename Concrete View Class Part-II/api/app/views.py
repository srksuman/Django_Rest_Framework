from .serializer import TeacherSerializer
from .models import Teacher
from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.


class ListCreateTeacherAPI(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class RetrieveDestroyTeacherAPI(RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class RetrieveUpdateTeacherAPI(RetrieveUpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class RetrieveUpdateDestroyTeacherAPI(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
