from django.urls import path

from .views import index
from .views import details



urlpatterns = [
    path('', index, name = 'index'),
    #path('<int:pk>', details, name = 'details'),# pelo PK
    path('<str:slug>',details, name = 'details'),
]