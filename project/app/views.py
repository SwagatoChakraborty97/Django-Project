from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def func(request):
    return HttpResponse("Hello World")

def func2(request):
    a = input("Enter Name: ")
    return HttpResponse(f"Namaste {a}")
