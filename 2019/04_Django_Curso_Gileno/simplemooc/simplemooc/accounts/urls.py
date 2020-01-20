from django.urls import path

from django.contrib.auth.views import LoginView

#-----------------
#from simplemooc.accounts.views import register #tambem funciona
from .views import register
#-----------------

urlpatterns = [
    path('entrar/',
         LoginView.as_view(template_name = 'accounts_templates/login.html'),
         name = 'login'),
    path('cadastre-se/',register, name = 'register')
]