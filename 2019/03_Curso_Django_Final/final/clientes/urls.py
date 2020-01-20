from django.urls import path


#from .views import * #MAIS INTELIGENTE FAZER ASSIM....
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete
from .views import hello

urlpatterns = [
    path('list/', persons_list, name= 'person_list'), #name = apelido para url (usamos no arquivo.html)
    path('new/', persons_new, name= 'person_new'),
    path('update/<int:id>/', persons_update, name = 'person_update'),
    path('delete/<int:id>/', persons_delete, name = 'person_delete'),
    path('hello/', hello),
]
