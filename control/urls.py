"""
URL configuration for djangoRequerimientos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from requerimientos import views
from requerimientos.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    
    path('', RequerimientosList.as_view(), name='requerimientos'),
    path('create/', RequerimientosCreate.as_view(), name='crear'),
    path('edit/<int:pk>/', RequerimientosUpdate.as_view(), name='editar'),
    path('historicos/',Historico.as_view(),name='historicos'),
]
