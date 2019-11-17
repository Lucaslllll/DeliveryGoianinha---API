from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Mensagem, Remetente
from Delivery.models import Restaurante

class MensagemSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    cliente = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    restaurante = serializers.SlugRelatedField(many=False, slug_field='nome', queryset=Restaurante.objects.all())
    remetente = serializers.SlugRelatedField(many=False, slug_field='nome', queryset=Remetente.objects.all())
    class Meta:
        model = Mensagem
        fields = ['cliente', 'restaurante', 'mensagem', 'remetente', 'hora_envio']