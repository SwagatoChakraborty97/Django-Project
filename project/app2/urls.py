from django.urls import path
from app2 import views

urlpatterns = [
    path('hello2/',views.func2)
]
