from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def apiFunction(request):
    if request.method == 'GET':
        return JsonResponse({'success':'got it'})
