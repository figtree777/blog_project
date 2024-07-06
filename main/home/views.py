from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_test(request):
    return HttpResponse("Hello, World!")
