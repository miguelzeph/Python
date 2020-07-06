from django.contrib import admin

# Register your models here.
from .models import Post, Contact


class PostAdmin(admin.ModelAdmin):
    list_display=['title','sub_title','approved','imagem']
    search_fields = ['title','sub_title']

#Registar sua Aplicação
admin.site.register(Post,PostAdmin)
admin.site.register(Contact)
