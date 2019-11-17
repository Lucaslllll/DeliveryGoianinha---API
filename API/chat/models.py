from django.contrib.auth.models import User
from django.db import models
from Delivery.models import Restaurante

class Remetente(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    

class Mensagem(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='receiver')        
    mensagem = models.CharField(max_length=1200)
    hora_envio = models.DateTimeField(auto_now_add=True)
    remetente = models.ForeignKey(Remetente, on_delete=models.CASCADE, null=True, blank=True)
    lida = models.BooleanField(default=False)
    
    def __str__(self):
        return self.mensagem
    
    class Meta:
        ordering = ('hora_envio',)