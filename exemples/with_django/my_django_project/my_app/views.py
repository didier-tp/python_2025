from django.shortcuts import render

# Create your views here.

# from hello-world tuto:
from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello, World!')
