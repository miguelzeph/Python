from django.db import models

#Toda vez que você alterar algo aqui: makemigrations !!!!!!
#E depois faça: migrate !!!!

# Create your models here.


class Documento(models.Model):
    num_doc = models.CharField(max_length = 50)

    def __str__(self):

        return self.num_doc


class Person(models.Model):
    #obs: transforma campo opcional==> null = True, blank = True
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True,blank=True)
    salary = models.DecimalField(max_digits=7, decimal_places=2, null = True, blank = True)
    bio = models.TextField(null=True,blank=True)
    photo = models.ImageField(upload_to='client_photos', null= True, blank = True) #pip install Pillow

    #referenciando a classe de outros documentos (1 para 1 apenas)
    doc = models.OneToOneField(Documento,null = True, blank = True, on_delete = models.CASCADE)


    def __str__(self):  # Funcao Display do usuario
        return self.first_name +' '+ self.last_name

class Produto(models.Model):

    descricao = models.CharField(max_length = 50)
    preco = models.DecimalField(max_digits = 7, decimal_places = 2)

    def __str__(self):

        return self.descricao



class Venda(models.Model):

    numero = models.CharField(max_length = 7)
    valor = models.DecimalField(max_digits=5,decimal_places = 2)
    desconto = models.DecimalField(max_digits=5,decimal_places = 2)
    impostos = models.DecimalField(max_digits=5,decimal_places = 2)

    pessoa = models.ForeignKey(Person, null = True, blank = True, on_delete = models.PROTECT)

    produtos = models.ManyToManyField(Produto, blank = True)

    def __str__(self):

        return self.numero
