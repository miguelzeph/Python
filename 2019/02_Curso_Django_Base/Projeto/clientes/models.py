from django.db import models

#Toda vez que você alterar algo aqui: makemigrations !!!!!!
#E depois faça: migrate !!!!

# Create your models here.

class Person(models.Model):
    #obs: transforma campo opcional==> null = True, blank = True
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True,blank=True)
    salary = models.DecimalField(max_digits=7, decimal_places=2, null = True, blank = True)
    bio = models.TextField(null=True,blank=True)
    photo = models.ImageField(upload_to='client_photos', null= True, blank = True) #pip install Pillow

    def __str__(self):  # Funcao Display do usuario
        return self.first_name +' '+ self.last_name