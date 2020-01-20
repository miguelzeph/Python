from django.db import models

# Create your models here.


from django.urls import reverse




class CourseManager(models.Manager):

    def search(self,query):
        return self.get_queryset().filter(name__icontains = query)



class Course(models.Model):

    name = models.CharField('Nome', max_length = 30)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank = True)
    about = models.TextField("Sobre o Curso",blank = True)
    start_date = models.DateField(
        'Data de Início',null=True,blank=True
    )
    #As imagens do Django não ficam no Banco de Dados e sim em
    #um diretório (pasta) Físico...
    image = models.ImageField(upload_to ="images", verbose_name = "Imagem",
                              null=True, blank=True)

    created_at = models.DateTimeField("Criado em",auto_now_add = True)
    updated_at = models.DateTimeField("Atualizado em", auto_now= True)

    new_objects = CourseManager()

    def __str__(self):

        return self.name

    #NO ADMIN ELE FAZ UMA ALTERACAO LEGAL - botão: "VER NO SITE"
    def get_absolute_url(self):
        return reverse('details', kwargs={'slug': self.slug})


    class Meta:

        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['name'] #"-name" = ordem decrescente