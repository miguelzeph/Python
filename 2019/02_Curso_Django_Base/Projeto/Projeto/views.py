from django.http import HttpResponse

from django.shortcuts import render


def hello(request):
    #return HttpResponse("Hello World")
    return render(request, 'index.html')

def fname2(request):
    return render(request, 'pessoa.html',{'idade_func':5})

