from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Course
from .forms import ContactCourse

# Create your views here.



def index(request):

    courses = Course.new_objects.all()
    context = {'courses': courses}
    template_name = 'courses/index.html'

    return render(request, template_name, context)

""" ------------------------pelo PK ------------------
def details(request,pk):
    #try:
        #course = Course.new_objects.get(pk=pk) #Antigo
        course = get_object_or_404(Course, pk=pk)

        return render(request, 'courses/details.html',{'course':course}) #não preciso do Try assim...
    #except:

    #    return HttpResponse("Não foi encontrado o valor do 'pk'")
"""

#--------------------- Pelo SLUG ---------------------

def details(request,slug):

        course = get_object_or_404(Course, slug=slug)
        context = {}

        if request.method == 'POST':
            form = ContactCourse(request.POST)

            if form.is_valid():
                context['is_valid'] = True
                #print(form.cleaned_data['name'])
                #print(form.cleaned_data['email'])
                #print(form.cleaned_data['message'])

                form.send_EEEmail(course)

                form = ContactCourse()

        else:
            form = ContactCourse()

        context['form'] = form
        context['course'] = course

        template_name = 'courses/details.html'
        return render(request, template_name, context)




