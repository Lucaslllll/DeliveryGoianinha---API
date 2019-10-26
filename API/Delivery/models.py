from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import os
from cloudinary.models import CloudinaryField



def get_path_restaurante(self, instance, filename):
    return os.path.join('Fotos/Restaurantes', str(instance.id), filename)
def get_path_comida(self, instance, filename):
    return os.path.join('Fotos/Comida', str(instance.id), filename)


class Ingredientes(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome

class Comida(models.Model):
    nome = models.CharField(max_length=120)
    ingredientes = models.ManyToManyField(Ingredientes)
    preço = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.nome

   


class Usuario(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    localizacao = models.CharField(max_length=500)
    
    def __str__(self):
        return self.nome.username

class Restaurante(models.Model):
    nome = models.CharField(max_length=500)
    cnpj = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    slug = models.SlugField(max_length=1000, unique=True)
    localizacao = models.CharField(max_length=1000)
    descricao_breve = models.CharField(max_length=100, null=True)
    descricao_longa = models.CharField(max_length=500, null=True)
    status = models.BooleanField(default=True, null=True)
    telefone = PhoneNumberField(region='BR')

    def __str__(self):
        return self.nome

class Tags(models.Model):
    nome = models.CharField(max_length=500)
    
    def __str__(self):
        return self.nome    

class Restaurante_Tag(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag.nome+" "+self.restaurante.nome

class Cardapio(models.Model):
    restaurante = models.OneToOneField(Restaurante, on_delete=models.CASCADE, blank=True, null=True)
    comidas = models.ManyToManyField(Comida)

    def __str__(self):
        return self.restaurante.nome+" "+self.comidas.nome

class Classificacao_Usuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
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
    comida = models.ForeignKey(Comida, on_delete=models.CASCADE, blank=True, null=True)
    foto = CloudinaryField('foto', null=True)

    def __str__(self):
        return self.comida.nome


class Pedido(models.Model):
    nome = models.ForeignKey(Comida, on_delete=models.CASCADE)
    unidades = models.IntegerField()
    entrega = models.DateTimeField()

    def __str__(self):
        return self.nome


class Pedido_Restaurante(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)



    

class Comentario(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, blank=True, null=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)

    def __str__(self):
        return self.titulo





