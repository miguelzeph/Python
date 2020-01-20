from django.urls import path


#from .views import * #MAIS INTELIGENTE FAZER ASSIM....
from .views import home
from .views import logout2

urlpatterns = [
    path('', home, name= 'home'), #name = apelido para url (usamos no arquivo.html)
    path('logout/', logout2, name ='logout')
]