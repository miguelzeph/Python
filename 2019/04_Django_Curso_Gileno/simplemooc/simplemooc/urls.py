"""simplemooc URL Configuration

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

#---------------------------------------------------------
from core import urls as core_urls
from courses import urls as courses_urls
from simplemooc.accounts import urls as accounts_urls

#ou, apesar de ficar vermelho em cima... o django acha, mas o correto é...

#from simplemooc.core import urls as core_urls
#from simplemooc.courses import urls as courses_urls
#from simplemooc.simplemooc.accounts import urls as accounts_urls
#---------------------------------------------------------------------

#Gambiarra para exibir imagens
from django.conf import settings
from django.conf.urls.static import static

#from .views import teste

urlpatterns = [
    path('',include(core_urls)),
    path('cursos/',include(courses_urls)),
    path('admin/', admin.site.urls),
    #path('teste', teste),
    path('conta/', include(accounts_urls))

]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)