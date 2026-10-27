"""
URL configuration for mainproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/',form,name="form"),
    path('delete_Student/<int:id>/',delete_Student,name="delete_Student"),
    path('header/',header,name="header"),
    path('update/<int:id>/',update,name="update"),
    path('table/',table,name="table"),
    path('header2/',header2,name="header2"),
    path('project/',project,name="project"),
    path('project2/',project2,name="project2"),
    path('dashboard/',dashboard,name="dashboard"),
    path("detail/", detail, name="detail"),
    path('delete_Data/<int:id>/',delete_data,name="delete_Data"),
    path('update2/<int:id>/',update2,name="update2"),
    
]

