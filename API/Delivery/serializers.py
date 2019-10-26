from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from cloudinary.templatetags import cloudinary


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

class RestauranteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Restaurante
        fields = ('id', 'nome', 'cnpj', 'slug' ,'localizacao', 'descricao_breve', 
                  'descricao_longa', 'status', 'telefone', )
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

        

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pedido
        fields = '__all__'

class PedidoRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pedido_Restaurante
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comentario
        fields = '__all__'


class ClassificacaoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classificacao_Usuario
        fields = '__all__'

class ClassificacaoRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classificacao_Restaurante
        fields = '__all__'

class ClassificacaoRestauranteFNSerializer(serializers.Serializer):
    class Meta:
        model = models.Restaurante
        fields = ('id', )
        

class FotosRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fotos_Restaurante
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(FotosRestauranteSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation

class FotosComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fotos_Comida
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(FotosComidaSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation

class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredientes
        fields = '__all__'

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comida
        fields = '__all__'

class CardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cardapio
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = '__all__'

class TagRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = ['id']
