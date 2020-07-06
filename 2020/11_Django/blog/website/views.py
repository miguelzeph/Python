from django.shortcuts import render

from .models import Post
# Create your views here.
def hello_blog(request):

    lista = [
        'Python',
        'Git',
        'Django'
    ]

    list_post = Post.objects.all()

    data = {
        'name':'Curso de Django 3',
        'lista_tecnologia':lista,
        'posts': list_post,
         }

    return render(request, 'index.html',data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request,'post_detail.html',{'post':post})
