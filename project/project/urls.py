"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views as views_1
from app2 import views as views_2

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home),
    # path('hello/', views.func),
    # path('namaste/', views.func2)
    path('', include('app.urls')),
    path('course/', include([ path('Aloha/', views_1.func2), path('Namaste/',views_2.func2) ]))
]
