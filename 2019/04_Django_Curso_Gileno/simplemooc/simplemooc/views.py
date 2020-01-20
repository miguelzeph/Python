from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def teste(request):

    course = render(request, 'teste.html')
    return course