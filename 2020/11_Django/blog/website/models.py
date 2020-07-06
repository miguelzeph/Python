from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()

    approved = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='posts', null = True, blank = True)

    # Agora no Admin ele mostra como Título... e não "Post Object (1) ... "
    def __str__(self):
        return self.title