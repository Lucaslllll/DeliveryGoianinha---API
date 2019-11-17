from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import os
from cloudinary.models import CloudinaryField

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser


def get_path_restaurante(self, instance, filename):
    return os.path.join('Fotos/Restaurantes', str(instance.id), filename)
def get_path_comida(self, instance, filename):
    return os.path.join('Fotos/Comida', str(instance.id), filename)


# Ingredientes principais do tipo
class Ingredientes(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome

# grande, medio, pequeno
class Tamanho(models.Model):
    nome = models.CharField(max_length=120)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

# extras
class Codimentos(models.Model):
    nome = models.CharField(max_length=120)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

# acai, pizza, hamburger.
class Tipo(models.Model):
    nome = models.CharField(max_length=120)
    foto = models.ImageField(upload_to='Fotos/Tipo_Comida')
    ingredientes = models.ManyToManyField(Ingredientes) 
    
    def __str__(self):
        return self.nome


class Usuario(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    x = models.CharField(max_length=100, null=True, blank=True)
    y = models.CharField(max_length=100, null=True, blank=True)
    foto = models.ImageField(upload_to='Fotos/Usuario', null=True, blank=True)
    
    def __str__(self):
        return self.nome.username


class Tags(models.Model):
    nome = models.CharField(max_length=500, unique=True)
    
    def __str__(self):
        return self.nome

class Restaurante(models.Model):
    nome = models.CharField(max_length=500)
    cnpj = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    slug = models.SlugField(max_length=1000, unique=True)
    descricao_breve = models.CharField(max_length=100, null=True)
    descricao_longa = models.CharField(max_length=500, null=True)
    inicio = models.TimeField(null=True, blank=True)
    fim = models.TimeField(null=True, blank=True)
    x = models.CharField(max_length=100, null=True, blank=True)
    y = models.CharField(max_length=100, null=True, blank=True)
    status = models.BooleanField(default=True, null=True)
    telefone = PhoneNumberField(region='BR')
    foto = models.ImageField(upload_to='Fotos/Restaurante')
    # tags = models.ManyToManyField(Tags, through='Restaurante_Tag')

    def __str__(self):
        return self.nome

class Restaurante_Tag(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag.nome+" "+self.restaurante.nome


class Classificacao_Usuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField()
    
    def __str__(self):
        return str(self.nota)

class Classificacao_Restaurante(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nota = models.IntegerField()
    
    def __str__(self):
        return str(self.nota)


 

class Fotos_Restaurante(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, blank=True, null=True)
    foto = CloudinaryField('foto', null=True)
    
    def __str__(self):
        return self.restaurante.nome

class Fotos_Comida(models.Model):
    comida = models.ForeignKey(Tipo, on_delete=models.CASCADE, blank=True, null=True)
    foto = CloudinaryField('foto', null=True)

    def __str__(self):
        return self.comida.nome


class Pedido(models.Model):
    detalhes = models.CharField(max_length=500)
    nome = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    codimentos = models.ManyToManyField(Codimentos)
    unidades = models.IntegerField()
    tempo = models.DateTimeField()
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.detalhes

class Pedido_Restaurante(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, blank=True, null=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, blank=True, null=True)


class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, blank=True, null=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)

    def __str__(self):
        return self.titulo





