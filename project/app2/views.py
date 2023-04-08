from django.shortcuts import render
from django.http import HttpResponse

def func2(request):
    return HttpResponse("Hello World 2")