from django.urls import path
from app import views

urlpatterns = [
    path('', views.home),
    path('hello/', views.func),
    path('namaste/', views.func2)
]