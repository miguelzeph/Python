from django.urls import path

from .views import hello_blog, post_detail, save_form

urlpatterns = [
    path('', hello_blog),
    path('post/<int:id>/',post_detail, name = 'post_detail'),
    path('save_form/',save_form,name='save_form'),
]