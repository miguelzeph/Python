from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm #nao tem email, neste formulario

from django.conf import settings

from .forms import RegisterForm


def register(request):
    template_name = 'accounts_templates/register.html'
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)

    else:
        #form = UserCreationForm()
        form = RegisterForm(request.POST)
    context = {
        'form':form
    }

    return render(request, template_name, context)