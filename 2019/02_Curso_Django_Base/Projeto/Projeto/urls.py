"""Projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from .views import hello
from .views import fname2


#importar das urls clientes
from clientes import urls as clients_urls


#Gambiarra para importar imagem pelo Django (SOMENTE EM DESENVOLVIMENTO)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello),
    path('pessoa/',fname2),
    path('person/', include(clients_urls)),#Sempre chamo da pasta clientes agora
] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
