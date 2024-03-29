from rest_framework import serializers
from .models import (
    Usuario, Restaurante, Classificacao_Usuario, Classificacao_Restaurante, 
    Fotos_Comida, Fotos_Restaurante, Ingredientes, Tipo, Tamanho, Codimentos, 
    Codimentos_Restaurante, Pedido, Pedido_Restaurante, Comentario, Restaurante_Tag,
    Tags, Cardapio, Cor, Comida_Tag
)
from django.contrib.auth.models import User
from cloudinary.templatetags import cloudinary
import cloudinary.uploader
from cloudinary.forms import CloudinaryFileField


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super(UsuarioSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation        

class UsuarioFNSerializer(serializers.Serializer):
    class Meta:
        model = Usuario
        fields = ('id', )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']



class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }

    def to_representation(self, instance):
        representation = super(RestauranteSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation


class RestauranteFNSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = 'id'
        
class CorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cor
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class PedidoRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_Restaurante
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class FiltrarComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id',]


class CardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardapio
        fields = '__all__'

class FiltrarCardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardapio
        fields = ['id',]


# classificacao

class ClassificacaoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classificacao_Usuario
        fields = '__all__'

class ClassificacaoUsuarioFNSerializer(serializers.Serializer):
    class Meta:
        model = Usuario
        fields = ('id', )

class ClassificacaoRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classificacao_Restaurante
        fields = '__all__'

class ClassificacaoRestauranteFNSerializer(serializers.Serializer):
    class Meta:
        model = Restaurante
        fields = ('id', )
        

# comida

class FotosRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos_Restaurante
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(FotosRestauranteSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation

class FotosComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos_Comida
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(FotosComidaSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation

class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes
        fields = '__all__'

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ComidaSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation

class TamanhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamanho
        fields = '__all__'

class CodimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codimentos
        fields = '__all__'

class CodimentosRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codimentos_Restaurante
        fields = '__all__'

class CodimentosRestauranteFNSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codimentos_Restaurante
        fields = ['id']

# tags

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

class TagRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante_Tag
        fields = '__all__'


class TagRestauranteFiltrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id']


class TagComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comida_Tag
        fields = '__all__'


class TagComidaFiltrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id']
