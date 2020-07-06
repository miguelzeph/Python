from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display=['title','sub_title','approved','imagem']
    search_fields = ['title','sub_title']

admin.site.register(Post,PostAdmin)