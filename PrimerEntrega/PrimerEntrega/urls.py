"""PrimerEntrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app_Entrega.views import inicio, autos, ag3ncias, vendedores, formularioAgencia, busquedaAgencia, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('autos/', autos, name='autos'),
    path('agencias/', ag3ncias,name='agencias'),
    path('vendedores/', vendedores,name='vendedores'),
    path('formulario/', formularioAgencia,name='formagen'),
    path('busquedaAgencia/', busquedaAgencia,name='busqagen'),   
    path('buscar/', buscar,name='buscar'), 
]
