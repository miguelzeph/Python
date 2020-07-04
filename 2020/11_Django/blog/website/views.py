from django.shortcuts import render

# Create your views here.
def hello_blog(request):
    return render(request, 'index.html')
