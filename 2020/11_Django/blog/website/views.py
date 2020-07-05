from django.shortcuts import render

# Create your views here.
def hello_blog(request):

    lista = [
        'Python',
        'Git',
        'Django'
    ]

    data = {'name':'Curso de Django 3', 'lista_tecnologia':lista}

    return render(request, 'index.html',data)
