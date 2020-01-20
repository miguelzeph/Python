from django.shortcuts import render, redirect

from django.contrib.auth import logout

# Create your views here.

def home(request):

    return render(request, 'home.html')


def logout2(request):
    logout(request)
    #return render(request, 'home.html') #Forma Feia
    return redirect('home') #Forma Bonita
