from django.urls import path
from .views import apiFunction
urlpatterns = [
    path('api/',apiFunction,name='api')
]
